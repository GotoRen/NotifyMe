# notify-me
## 📚 Introduction
- RaspberryPiとLINE Notify API, OpenJTalk などを使用した侵入検知者検知システム
- 侵入者を捉えるとLINEへ画像を送信
- WEBアプリケーションを使用することで、備え付けのスピーカを利用して侵入者へ警告
  - オリジナルのメッセージを送信することもできる
- 取得した画像は圧縮して一定期間ファイルサーバで保存

## 💡 Overview
![poster](https://user-images.githubusercontent.com/63791288/99535123-cd19b700-29eb-11eb-87ed-bc09257cdd92.png)

## 🚀 Reserve
```
$ pip3 install python-dotenv 
$ cp .env{.sample,}
```