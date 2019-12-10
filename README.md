# gdlab util?

requirements.txt作成する際は，仮想環境において試してみることをオススメする．
仮想環境の構築方法は以下に示す．

```
# 仮想環境を作成
$ python3 -m venv heroku_dev

# 仮想環境をアクティベート
$ source heroku_dev/bin/activate
$ source heroku_dev/bin/activate.fish ### fishの人はこちら

# 必要なライブラリをインストール
$ pip install 〇〇

# requirements.txtを作成
$ pip freeze > requirements.txt
```