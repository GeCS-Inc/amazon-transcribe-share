# Amazon Transcribe 手順

## S3 バケットを作成

[このサイト](https://892copy.jp/japanese-ok-amazon-transcribe-mojiokoshi/)
が画像つきで参考になると思います

注意点として、リージョンは `us-west-2` にしましょう

## 必要ライブラリのインストール

```
$ pip3 install boto3
$ pip3 install awscli
```

## 認証周り

アクセスキーの取得

https://docs.aws.amazon.com/ja_jp/powershell/latest/userguide/pstools-appendix-sign-up.html

作成するアクセスキーには次の権限を与えます。

- S3 フルアクセス
- transcribe フルアクセス

<img src="https://github.com/GeCS-Inc/amazon-transcribe-share/blob/main/screenshots/1.png?raw=true" width=600 />
<img src="https://github.com/GeCS-Inc/amazon-transcribe-share/blob/main/screenshots/2.png?raw=true" width=600 />
<img src="https://github.com/GeCS-Inc/amazon-transcribe-share/blob/main/screenshots/3.png?raw=true" width=600 />
<img src="https://github.com/GeCS-Inc/amazon-transcribe-share/blob/main/screenshots/4.png?raw=true" width=600 />


作成したアクセスキーを環境変数としてセットするために、次を実行します。

```
$ aws configure
```

上記で取得したアクセスキーを入力します

## プログラムの実行

`sample.wav` をサンプルファイルとして用意しました。
`amazon_transcribe.py` の `BUCKET_NAME` , `AUDIO_FILE` を必要に応じて書き換えてください。

```
$ python3 amazon_transcribe.py
```

## エラー

```
An error occurred (AllAccessDisabled) when calling the PutObject operation: All access to this object has been disabled
```

`BUCKET_NAME` は S3 上に存在するバケット名かどうか確認してみてください。また、アクセスキー関連で `AmazonS3FullAccess` が含まれているか確認してください。
