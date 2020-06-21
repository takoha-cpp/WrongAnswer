# WrongAnswer
Wrong Answer downloads test data of specified AtCoder contest's test cases.

![Wrong Answer Demo](https://takoha-cpp.github.io/WrongAnswer/demo.gif)

(日本語の説明は英語の下。Japanese README is below English)

### Warning/警告

This is unofficial tool. Please don't ask AtCoder for anything about this.

このツールは非公式なものです。AtCoder社様へのお問い合わせは絶対にお控え下さい。

## Install

```
pip install wrong-answer
```

## Requirements

You need Python3 (>= v3.6)

```
online-judge-tools
requests
```

These pkgs might be installed with WrongAnswer (if you haven't installed online-judge-tools yet).

## How-to

```
wa [contest-name] problem-name [testcase-name]
wa --cotest contest-name problem
wa --updatedb
wa --list
```

Specify what you want to download by arguments.

If you omit contest-name, current directory will be used as contest name. (Because I make a direcotry named after contest name always.)

If you don't know what the contest name which you want to download, you can use `--list` option, or you can just ask like `wa --contest t`. That will display contest names including `t`.

problem-name must be alphabet. lower-case will be uppered automatically. WA will make a directory as the same name as problem and saves the result into that directory. (See GIF animation above.)

If you specify testcase-name, it will be matched by test-cases, and the 1st one will be downloaded. WA will download both input and output data at the same time, and rename those files as ".in" and ".out" format for using with online-judge-tools.

If you omit testcase-name, all testcase data for one problem will be downloaded. But this can be very huge and slow. Watch out! I warned you.

## How this works

Dropbox has a unique URL for every single file and folder. I made a crawler and collect all URLs for data set. Why? Because Dropbox's URL uses hash values so you can't estimate what file has what URL.

All URLs are gathered and uploaded to this repository. And WA will download URL from this repository at first. Then download test cases from Dropbox. This is wierd, but at least it works!

WA will make copy of URLs into your local folder (as `.problems` and `.wrong-answer`). So once you download specific URL, it won't download again from this repository.

When AtCoder Inc. add another data set, I should upload that URL and there should be time gap for WA being able to download those data set. Please be patient and report to me if there are test data that already on AtCoder's Dropbox but WA cant' download them.

When new contest info comes to this repository, you must use `--updatedb` option to update contest data.

Thank you.

---

## インストール

```
pip install wrong-answer
```

一部のOSでは`pip3`を利用して下さい。Python2には対応していません。`python --version`で確認できます。

## 依存パッケージ

依存パッケージはpip3が同時にインストールするはずです.

```
online-judge-tools
requests
```

online-judge-toolsが必須です。中でコードを勝手に呼んでいます。(いつもお世話になっております。開発者様、貢献者様方、ありがとうございます)


## 使い方

指定したテストをDLするだけの単機能です。

```
wa problem
wa problem test-case
wa contest problem test-case
wa --contest contest-name problem
wa --updatedb
wa --list
```

コンテスト名にはabc160等を指定します。もしコンテスト名がわからない場合には`--list`を用いて一覧を表示するか、`wa --contest t`等と入力すると`t`を含むコンテスト名一覧が表示されます。

コンテスト名は省略するとカレントディレクトリ名がコンテスト名として自動的に利用されます。

問題名はアルファベットのAからF等ですがコンテストによってはC1とかC2とかもあり利用可能です。小文字でかまいませんが大文字に勝手に変換されます。

テストケース名は適当に入力するとファイル名にmatchする最初のテストケースがDLされます。

テストケースを省略すると1つの問題に対する全てのテストケースをDLします。A問題なら大丈夫ですが、D以降になると恐しくテストデータがでかくなる傾向があり1つで60MBとかも出てきます。そのため全部DLするというのはあまりお勧めできません。WAを食らった憎い問題のテストケースだけDLしたほうが良いです。

DLされたテストケースはonline-judge-toolsでテストするために1つのディレクトリに".in"と".out"の拡張子にリネームされて保存されます。例えばA問題のテストケースをDLした場合で、A問題を解くプログラム、a.outがカレントディレクトリにある場合ならば、

```
oj test -d A
```

とすればテストができます。

うまく行かない場合はお知らせ下さい。

## 中身の話

Dropboxは公開フォルダの中のファイル、フォルダ全てのURLにhash値が割り振られております。これは恐らくDropboxの巨大な分散ファイルシステム上では`*nix`系のpathを用いてはいないのかと思います。これによりユーザはWeb上で公開されたデータがどこにあるのかpathが分かっていてもURLを推測することはできなくなっています。

そのため全てのテストケースのファイルのURLを収集してこのリポジトリに登録してpathの関係からURLを検索できるようにしました。

なぜこのような面倒な手段を選んだのかについてはお察しください。

ファイルのURLには必ずdl=0とのGETパラメータが付いていますが、見てわかる通り1にするだけでその中身をDLすることが可能です。WAでもdl=1に変更した上でzipをDLし、自動でリネームしながら伸展しています。

URL登録式のため、AtCoder社がDropboxを更新してからこちらのDBを更新するまでに時差ができると思います。新規コンテスト情報が無いと思われる場合、ご連絡下さい。

Dropbox上のテストデータのURLはここ数年変更が無かったのですがつい先日、何かしらの理由で移転が行われた模様です。トップのフォルダのURLが動くと必然的に全てのファイルのURLが変更されます。このためクローラーによるスキャンが再度必要になりました。今後も同様の事態は起こるかと思います。そのような場合には一時的に利用が不可能になりますが、ご了承下さい。

新しいコンテストが追加された場合には--updatedbオプションを利用してコンテストデータを更新する必要があります。これを用いてもDLできない場合、連絡を下さい。なお、コンテストによってはそもそもデータが公開されていない場合もあります。またABCのデータは同日開催のARCにのみある場合があります。通常、自動的にARCからDLを行うようコード上で努力しているのですが、探すのに失敗するケースもあるかと思います。


## Dropbox上公開データの問題

AtCoderによるテストケースデータ公開には一部、問題が残っている場合があります。
例えば、

- ゴミファイルの存在
- `in`フォルダはあるが`out`フォルダが無い
- 入力データはあるが出力データが無い

等です。できるだけクローラー側で処理していますが、まだ問題に当たるかもしれません。何かありましたらご連絡願います。


クローラーが何かしらエラーに当たった物
```
2020_hitachi
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
