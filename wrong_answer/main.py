#!/usr/bin/env python3
import io
import os
import re
import sys
import json
import time
import appdirs
import pathlib
import zipfile
import argparse
import requests
import onlinejudge.dispatch as dispatch
import onlinejudge._implementation.logging as log
import onlinejudge_api.get_contest as get_contest


from enum import Enum, unique, auto
from pathlib import Path, PurePath
from urllib.parse import urlparse

@unique
class Mode(Enum):
    CONTEST = auto()
    PROBLEM = auto()
    TESTCASE = auto()

log.addHandler(log.logging.StreamHandler(sys.stderr))
log.setLevel(log.logging.INFO)

user_data_dir = pathlib.Path(appdirs.user_data_dir('wrong_answer'))
os.makedirs(user_data_dir, exist_ok=True)
GITHUB_URL = 'https://takoha-cpp.github.io/WrongAnswer'
BASE_URLS = f"{user_data_dir}/folders.txt"

session = requests.Session()
agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}

# sizeof_fmt is from https://bit.ly/3c5Lr6Z by Fred Cirera
def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def download(url, saveto):
    log.info(f"Download: {url}")
    r = session.get(url, headers=agent)
    if r.status_code != requests.codes.ok:
        log.error(f"Download '{url}' failed.")
        exit(1)
    else:
        log.success("Succeeded")
    with open(saveto, "w") as f:
        f.write(r.text)

def findContest(contest: str) -> str:
    if not os.path.exists(BASE_URLS):
        download(GITHUB_URL + '/folders.txt', BASE_URLS)
    with open(BASE_URLS) as f:
        lines = [ line.rstrip() for line in f if re.match(contest, line, re.I)]

    if len(lines) == 0:
        log.warning(f"Contest {contest} not found in {BASE_URLS}")
        log.error(f"It seems like test data for {contest} were closed")
        exit(1)

    if len(lines) > 1:
        log.warning("Multi candidates: Choose a contest name from below")
        print()
        for i in lines:
            print(f"{i.split()[0]}", end=" ")
        print()
        exit(1)
    return lines[0]

def downloadSingleCase(url:str, target_dir:str, out:bool=False) -> None: 
    os.makedirs(target_dir, exist_ok=True)
    URL = re.sub(r'dl=0', 'dl=1', url);
    path = urlparse(URL).path
    suffix = PurePath(path).suffix
    filename = PurePath(path).name
    if suffix:
        filename = filename[:-len(suffix)] # Remove suffix
    filename += ".out" if out else ".in"
    log.info(f"Download: {URL}")
    r = session.get(URL, headers=agent)
    if r.status_code != requests.codes.ok:
        log.error("Download failed.")
        exit(1)
    else:
        log.info("Download Succeeded")
    target_file = target_dir + '/' + filename
    log.info(f"Save to: {target_file}")
    with open(target_file, "w") as fw:
        fw.write(r.text)

def main():
    cache_dir = './.wrong_answer'
    target_dir = '.'

# Parse input arguments
    parser = argparse.ArgumentParser(description = """Wrong Answer!! - Download AtCoder system test data""", epilog="""This program downloads the data by using the result of
            its own crawler. Because of this, you might not be able to download the
            latest contest's test data. If you think the data already opened was not
            registered to this program's DB, please leave a issue at the github page.
            Thank you.""", usage = '%(prog)s [contest] problem [test_case]')
    parser.add_argument('-c', '--contest', help='specify contest name explicitly (You can omit this when you use triple)')
    parser.add_argument('-u', '--updatedb', action='store_true', help='update database')
    parser.add_argument('-l', '--list', action='store_true', help='print contest list')
    parser.add_argument('cases', nargs='*')

    args = parser.parse_args()
    contest = args.contest

    if args.updatedb:
        download(GITHUB_URL + '/folders.txt', BASE_URLS)
        log.status(f"{BASE_URLS} updated.")
        if len(args.cases) == 0:
            exit(0)
    if args.list:
        with open(BASE_URLS, "r") as f:
            for X in f:
                X = X.split()[0]
                print(X)
        exit(0)

    argc = len(args.cases)
    if argc == 0:
        if args.contest is not None:
            url = findContest(args.contest).split()[1]
            print("""Downloading whole test sets for a contest could be very huge and slow.
    If you really want to do that, use below URL with a browser.
    But this program does not support whole contest downloading on purpose.
    """)
            URL = re.sub(r'dl=0', 'dl=1', url);
            print(URL)
            exit(0)
        else:
            parser.print_help()
            exit(1)
    elif argc == 1:
        # Download whole test cases of the specified problem.
        problem = args.cases[0].upper()
        MODE = Mode.PROBLEM
    elif argc == 2:
        # Download the test case of the problem.
        problem = args.cases[0].upper()
        case = args.cases[1]
        MODE = Mode.TESTCASE
    elif argc == 3:
        # Download the test case of the problem, of the contest
        contest = args.cases[0].upper()
        problem = args.cases[1].upper()
        case = args.cases[2]
        MODE = Mode.TESTCASE
    else:
        parser.print_help()
        exit(1)

# If contest is not set, use CWD as contest name
# Old ABC has some test data in ARC.
# You can find ARC contest name from the problem's page URL
    if contest is None:
        contest = os.path.basename(os.getcwd()).upper()
        log.warning("Contest name not specified. Use current dir as contest name.")

        # This is my rule. Each problem's web page urls are in '.problems'
        if Path('.problems').exists():
            with open('.problems') as f:
                url = f.readlines()[ord(problem) - ord('A')].rsplit()[0]
                contest = url.split('/')[-1].split('_')[0].upper()
        else:
            url = f"https://atcoder.jp/contests/{contest}"
            result = get_contest.main(dispatch.contest_from_url(url), is_full=False, session=session)
            ps = result['problems']
            for i in ps:
                if i['context']['alphabet'] == problem:
                    url = i['url']
                    break;
            else:
                log.error(f"Specified problem '{problem}' not found in the contest page")
                exit(1)
            contest = url.split('/')[-1].split('_')[0].upper()

# This URL is for whole test cases of a contest. Ignore.
    [contest, URL] = findContest(contest).split()

    if MODE == Mode.TESTCASE:
        testcases_path=f"{cache_dir}/{problem}.json"
        URL=GITHUB_URL + f"/contests/{contest}/{problem}.json"
        if not os.path.exists(testcases_path):
            os.makedirs(cache_dir, exist_ok=True)
            download(URL, testcases_path)

        with open(testcases_path, "r") as f:
            J = json.load(f)

        res = '.*' + case + '.*'
        for i in J:
            if re.match(res, i, re.I):
                URL1 = J[i]['in']
                URL2 = J[i]['out']
                break
        else:
            log.error(f"Test case '{case}' not found in {testcases_path}")
            with open(testcases_path, "r") as f:
                print()
                log.info(f"Problem {problem} has these test cases.")
                for i in J:
                    print(f"{i}", end=" ")
                print()
            exit(1)
        target_dir += '/' + problem
        downloadSingleCase(URL1, target_dir)
        downloadSingleCase(URL2, target_dir, out=True)
        log.success("Succeeded")
        exit(0)

    elif MODE == Mode.PROBLEM:
        cases = f"{cache_dir}/testcases.txt"
        URL = GITHUB_URL + f"/contests/{contest}/testcases.txt"
        if not os.path.exists(cases):
            os.makedirs(cache_dir, exist_ok=True)
            download(URL, cases)
        purls = {}
        found = False
        with open(cases, "r") as f:
            lines = f.readlines()
            for i in lines:
                [p, url] = i.split()
                if p == problem: break
            else:
                log.error(f"Specified problem '{problem}' not found in {cases}.")
                exit(1)
        url = re.sub(r'dl=0', 'dl=1', url);
        log.info(f"Downloading: {url}")
        log.warning("This could be long! They make archive file each time by request.")
        log.info("Waiting a responce...")
        r = session.get(url, headers=agent, stream=True)
        if r.status_code != requests.codes.ok:
            log.error(f"Failed. {r.status_code}")
            exit(1)

        log.info("Got a responce.")
        siz = sizeof_fmt(float(r.headers['Content-Length']))
        log.info(f"Reading... Size: {siz}")
        b = r.raw.read(40960)
        bs = bytearray()
        while b:
            bs += b
            b = r.raw.read(40960)
            sys.stdout.write('\r')
            sys.stdout.write(str(len(bs)))
            sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
        zf = zipfile.ZipFile(io.BytesIO(bs))
        target_dir += f"/{problem}"
        Path(target_dir).mkdir(parents=True, exist_ok=True)

        for i in zf.infolist():
            if i.is_dir(): continue
            path = PurePath(i.filename)
            fn = path.stem
            if path.match("out/*"):
                nfn = f"{target_dir}/{fn}.out"
            else:
                nfn = f"{target_dir}/{fn}.in"
            log.info(f"Create: {nfn}")
            with zf.open(i.filename) as fr:
                with open(nfn, "w") as fw:
                    for line in fr:
                        fw.write(line.decode('utf-8').replace('\r',''))
        log.success(log.green('AC'))
        exit(0)

if __name__ == '__main__':
    main()
