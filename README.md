# WrongAnswer
Wrong Answer downloads test data of specified AtCoder contest's test cases.


## Install

DL or Clone this repository. Copy wa to any directory in your PATH.

I have not made this installable via pip3 yet.

## How-to

wa [contest-name] problem-name [testcase-name]

If you omit contest-name, current directory will be used as contest name. (Because I make direcotry named after contest name always.)

problem-name must be alphabet. lower-case will be uppered automatically. WA will make a directory as the same name as problem and saves the result into the directory.

If you specify testcase-name, it will be matched by test-cases, and the 1st one will be downloaded. WA will download both input and output data at the same time, and rename those files as ".in" and ".out" format for using with online-judge-tools.

If you omit testcase-name, all testcase data for one problem will be downloaded. But this can be very huge for some problems. Watch out! I warned you.

## How this works

Dropbox has a unique URL for every single file. I made a crawler and collect all URLs for data set. Why? Because Dropbox's URL uses hash values so you can't estimate what file has what URL.

All URLs are uploaded to this repository. And WA will download URL from this repository.Then download test cases from Dropbox. This is wierd, but at least it works!

WA will make copy of URLs into your local folder. So once you download specific URL, it won't download again from this repository.

When AtCoder Inc. add another data set, I should upload that URL and there should be time gap for WA being able to download those data set. Please be patient and report to me if there are test data that already on AtCoder's Dropbox but WA cant' download them.

Thank you.
