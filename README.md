# notify-me
## 📚 Introduction
This devices intruder detection system using Raspberry Pi（3 model B）and LINE Notify API.<br>
When it catches an intruder, it sends an image to LINE.app. Then, the user performs a simple operation from the web application and uses the built in speaker to warn the intruder. Users can select the original message or template message, or alerts.<br>
The taken image is also saved in LINE.app, but it can be saved in the file server (samba) for a certain period of time by applying compression processing.

## 💡 Overview
![poster](https://user-images.githubusercontent.com/63791288/99535123-cd19b700-29eb-11eb-87ed-bc09257cdd92.png)

## 🚀 Reserve
```
$ pip3 install python-dotenv 
$ cp .env{.sample,}
```

## 📝 License
Released under the [MIT License](https://github.com/GotoRen/notify-me/blob/feature%2Forganize/LICENCE)