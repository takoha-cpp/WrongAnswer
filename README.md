# WrongAnswer
Wrong Answer downloads test data of specified AtCoder contest's test cases.

(日本語の説明は英語の下。Japanese README is below English)

## Install

```
pip3 install wrong-answer
```

## Requirements

They might be installed with WrongAnswer. But if they ain't, install them by using pip3.

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

If you omit contest-name, current directory will be used as contest name. (Because I make a direcotry named after contest name always.)

problem-name must be alphabet. lower-case will be uppered automatically. WA will make a directory as the same name as problem and saves the result into the directory.

If you specify testcase-name, it will be matched by test-cases, and the 1st one will be downloaded. WA will download both input and output data at the same time, and rename those files as ".in" and ".out" format for using with online-judge-tools.

If you omit testcase-name, all testcase data for one problem will be downloaded. But this can be very huge for some problems. Watch out! I warned you.

## How this works

Dropbox has a unique URL for every single file and folder. I made a crawler and collect all URLs for data set. Why? Because Dropbox's URL uses hash values so you can't estimate what file has what URL.

All URLs are uploaded to this repository. And WA will download URL from this repository at first. Then download test cases from Dropbox. This is wierd, but at least it works!

WA will make copy of URLs into your local folder. So once you download specific URL, it won't download again from this repository.

When AtCoder Inc. add another data set, I should upload that URL and there should be time gap for WA being able to download those data set. Please be patient and report to me if there are test data that already on AtCoder's Dropbox but WA cant' download them.

When new contest info comes to this repository, you must use `--updatedb` option to update contest data.

Thank you.

---

## インストール

```
pip3 install wrong-answer
```

## 依存パッケージ

依存パッケージはpip3が同時にインストールするはずですが、もしpackageが無いというエラーが出た場合には別途pip3にてインストールしてみて下さい。

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

テストケース名は適当に入力するとファイル名にmatchする最初のテストケースがDLされます。

テストケースをはしょると1つの問題に対する全てのテストケースをDLします。A問題とかなら大丈夫ですが、D以降になると恐しくテストデータがでかくなる傾向があり1つで13MBとかも出てきます。そのため全部DLするというのはあまりお勧めできません。WAを食らった憎い問題のテストケースだけDLしたほうが良いです。

DLされたテストケースはonline-judge-toolsでテストするために1つのディレクトリに".in"と".out"の拡張子にリネームされて保存されます。ですので

```
oj test -d A
```

とかやればテストができます。

こちらでは問題無く動いてますので、うまく行かない場合はお知らせ下さい。

## 中身の話

DropboxはWeb UIはSPAになっていて実は非公開APIを叩くと全ての公開folderとその中身のURLが取れWeb UIはそれを用いて画面を更新しているだけです。しかし全てのフォルダとファイルのURLはハッシュ値をURLに用いており、パスの構造からURLを推測することは不可能になっています。そのため全てのテストケースのファイルのURLを収集してこのリポジトリに登録してpathの関係からURLを検索できるようにしました。
クローラの公開は問題になる可能性が否定できないため見送ります。

ファイルのURLには必ずdl=0とのGETパラメータが付いていますが、見てわかる通り1にするだけでその中身をDLすることが可能です。WAでもdl=1に変更した上でzipをDLし、自動でリネームしながら伸展しています。

URL登録式のため、AtCoder社がDropboxを更新してからこちらのDBを更新するまでに時差ができると思います。無いと思われる場合、ご連絡下さい。

なお、Dropbox上のテストデータのURLはここ数年変更が無かったのですがつい先日、全面的に変更がありました。トップのフォルダのURLが動くと必然的に全てのファイルのURLが変更されます。このためクローラーによるスキャンが再度必要になります。結構、時間がかかるのですがご了承下さい。

新しいコンテストが追加された場合には--updatedbオプションを利用してコンテストデータを更新する必要があります。これを用いてもDLできない場合、連絡を下さい。なお、コンテストによってはそもそもデータが公開されていない場合もあります。またABCのデータは同日開催のARCにのみある場合があります。通常、自動的にARCからDLを行うようコード上で努力しているのですが、探すのに失敗するケースもあるかと思います。


## Dropbox上公開データの問題

AtCoderによるテストケースデータ公開には一部、問題が残っている場合があります。
例えば、

- ゴミファイルの存在
- `in`フォルダはあるがoutフォルダが無い
- 例えば入力データはあるが出力データが無い

等です。できるだけクローラー側で処理していますが、まだ問題に当たるかもしれません。何かありましたらご連絡願います。


クローラーが何かエラーに当たった物
```
ARC058_ABC042 D 新しいテキスト ドキュメント.txt
ARC061 D in
ARC058_ABC042 D subtask2_11.txt
ARC058_ABC042 D subtask2_12.txt
ARC058_ABC042 D subtask2_13.txt
ARC058_ABC042 D subtask2_14.txt
ARC058_ABC042 D subtask2_15.txt
ARC058_ABC042 D subtask2_16.txt
ARC058_ABC042 D subtask2_17.txt
ARC058_ABC042 D subtask2_18.txt
ARC058_ABC042 D subtask2_19.txt
ARC058_ABC042 D subtask2_20.txt
AGC031 A 01-00.txt
AGC031 D etc
AGC027 E 0_01 (競合コピー 2018-09-15).txt
AGC010 E in36.txt
AGC010 E in37.txt
AGC010 E in38.txt
AGC010 E in39.txt
AGC010 E in40.txt
AGC010 E in41.txt
AGC010 E in42.txt
AGC010 E in43.txt
AGC010 E in44.txt
AGC010 E in45.txt
AGC009 E .06.txt.swp
ABC141 D testcase_03.nkftmpjKHWPL
ABC126 D testcase_09
```
