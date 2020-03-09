# Synology NAS Bot

🤖 專為 synology NAS 設計的 Telegram Bot 

fork from [idaelhack](https://github.com/idealhack/synologynasbot)

## 功能

- 建立下載任務
- 列出目前的下載任務
- 清除全部的下載任務


## 使用說明

1. [在Heroku上部署](https://heroku.com/deploy?template=https://github.com/idealhack/synologynasbot)
1. 開啟Telegram 透過 [@BotFather](https://t.me/BotFather) 建立一個聊天機器人
1. 打開 Heroku app **Settings** 頁面, 設定以下 **Config Variables**:
    - `SYNOLOGY_NAS_BOT_TOKEN`: Telegram 的API token 可向 @BotFather 索取
    - `SYNOLOGY_NAS_BOT_OWNER`: 你的 Telegram username, *機器人只服從來自主人的命令*
    - `SYNOLOGY_NAS_BOT_URL`: 你的 Synology NAS URL, 格式長這樣: `https://id.synology.me:port/webapi/`
    - `SYNOLOGY_NAS_BOT_ACCOUNT`: Synology NAS 的帳號
    - `SYNOLOGY_NAS_BOT_PASSWORD`: Synology NAS 的密碼
1. 打開你的 Heroku app **Resources** 頁面, 檢查你的機器人是否在運行.
1. 恭喜你！ 完成了 可以開始使用你的機器人了.

## 其他方案 

[moviemagnetbot](https://github.com/magunetto/moviemagnetbot): create (Magnet/eD2k/FTP) download tasks by RSS feed

## 除錯

打開你的 Heroku app **View logs** 頁面, 看看發生了什麼.
