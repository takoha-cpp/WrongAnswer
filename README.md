# WrongAnswer
Wrong Answer downloads test data of specified AtCoder contest's test cases.

(日本語の説明は英語の下。Japanese README is below English)

## Install

DL file "wa" only. or copy paste "wa".
(All you need is "wa" file only, so don't try to clone this repository!)

I have not made this installable via pip3 yet.

## Requirements

```
Python3 >= v3.6
online-judge-tools
requests
```

## How-to

```
wa [contest-name] problem-name [testcase-name]
wa --cotest contest-name problem
wa --updatedb
```

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

## インストール

waだけコピーしてpathの通っているディレクトリにコピーしてください。
まだpip3でインストールできるようにしていません。したこともないのでしばらくかかります。

## 依存パッケージ

online-judge-toolsが必須です。中でこのコードを勝手に呼んでいます。(いつもお世話になっております。開発者様、貢献者様方、ありがとうございます)

requests (PythonでHTTP叩く時、必須なツール。online-judge-toolsも使っているので上を入れれば多分入ってる)

# 使い方


```
wa problem
wa problem test-case
wa contest problem test-case
wa --contest contest-name problem
wa --updatedb
```

コンテスト名は省略するとカレントディレクトリ名が利用されます。私がいつもコンテスト毎にディレクトリを切るためです。

問題名はアルファベットのAからFとかですがコンテストによってはC1とかC2とかあったりします。小文字でかまいませんが大文字に勝手に変換されます。

テストケース名は適当に入力するとファイル名にmatchする最初のテストケースがDLされます。いつか番号指定とかちゃんとできるようにしたいな。

テストケースをはしょると1つの問題に対する全てのテストケースをDLします。A問題とかなら大丈夫ですが、D以降になると恐しくテストデータがでかくなる傾向があり1つで13MBとかも出てきます。そのため全部DLするというのはお勧めできません。WAを食らった憎い問題のテストケースだけDLしたほうが良いです。

DLされたテストケースはonline-judge-toolsでテストするために1つのディレクトリに".in"と".out"の拡張子にリネームされて保存されます。ですので

oj test -d A

とかやればテストができます。こちらでは問題無く動いてますので、うまく行かない場合は適当に聞いて下さい。

# 中身の話

DropboxはWeb UIはSPAになっていて実は非公開APIを叩くと全ての公開folderとその中身のURLが取れWeb UIはそれを用いて画面を更新しているだけです。しかし全てのフォルダとファイルのURLはハッシュ値をURLに用いており、パスの構造からURLを推測することは不可能になっています。そのため全てのテストケースのファイルのURLを収集してこのリポジトリに登録してpathの関係からURLを検索できるようにしました。
クローラの公開は問題になる可能性が否定できないため見送ります。

ファイルのURLには必ずdl=0とのGETパラメータが付いていますが、見てわかる通り1にするだけでその中身をDLすることが可能です。

URL登録式のため、AtCoder社がDropboxを更新してからこちらのDBを更新するまでに時差ができると思います。競技プログラマの皆様なら適当にプログラムを変えて対策されることでしょう。PR待ってます(笑
