# ✨ HANGOVER_RADIO ✨

<p align="center">
  <img src="https://telegra.ph/file/21c43178aecc3b67ab468.jpg">
</p>
- An Telegram Bot to Play Radio/Music in Channel or Group Voice Chats.
- A Telegram Bot to Play Audio in Voice Chats With Youtube and Deezer support.
- Supports Live streaming from YouTube.

---

## NOTE:

- Make sure you have started a VoiceChat in your Group before deploying.

---

## Features

<details>
  <summary><b>Show the Features</b></summary>
<br/>

- Playlist, queue
- Change VoiceChat title to current playing song name.
- Supports Live streaming from youtube
- Supports both deezer and youtube to search songs.
- Play from telegram file supported.
- Starts Radio after if no songs in playlist.
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing
- Automatic restart even if heroku restarts.

</details>

---

## Variables
<details>
  <summary><b>See Variables</b></summary>
<br/>

### Pre Requisites 
- `API_ID` : Get from [my.telegram.org](https://my.telegram.org/app) or [@UsetTGzKBot](https://telegram.dog/UseTGzKBot)
- `API_HASH` : Get from [my.telegram.org](https://my.telegram.org/app) or [@UseTGzKBot](https://telegram.dog/UseTGzKBot)
- `BOT_TOKEN` : Get From [@Botfather](https://telegram.dog/BotFather)
- `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@S780821/PyrogramSession)
- `CHAT` : ID of Channel/Group where the bot plays Music.
- `LOG_GROUP` : Group to send Playlist, if CHAT is a Group
- `ADMINS` : ID of users who can use admin commands.
- `ARQ_API` : Get it for free from [@ARQRobot](https://telegram.dog/ARQRobot), This is required for /dplay to work.
- `STREAM_URL` : Stream URL of radio station or a youtube live video to stream when the bot starts or with /radio command. Some Streaming Links [Click here.](https://t.me/c/1481808444/143)
- `MAXIMUM_DURATION` : Maximum duration of song to play.(Optional)
- `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature. 
- `ADMIN_ONLY` : Pass `Y` If you want to make /play and /dplay commands only for admins of `CHAT`. By default `N` /play and /dplay is available for all.

</details>

---

## Deploy Now

#### DEPLOY TO HRROKU

<a href="https://heroku.com/deploy?template=https://github.com/S780821/HANGOVER_RADIO">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">


[![Deploy+On+Tg](https://img.shields.io/badge/DEPLOY%20VIA%20TELEGRAM%20BOT-blueviolet?style=for-the-badge&logo=telegram)](https://telegram.dog/XTZ_HerokuBot?start=Uzc4MDgyMS9IQU5HT1ZFUl9SQURJTyBYbWFydHk)

#### DEPLOY TO QOVERY

 <a href="https://console.qovery.com">
    <img height="30px" src="https://img.shields.io/badge/Deploy%20to%20Qovery-blueviolet?style=for-the-badge&logo=qovery">

#### DEPLOY ON RAILWAY
[![Deploy+on+Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/S780821/HANGOVER_RADIO&envs=API_ID,API_HASH,BOT_TOKEN,SESSION_STRING,ADMINS,CHAT,SUDO_USERS)

#### DEPLOY IN YOUR VPS

```sh
git clone https://github.com/S780821/HANGOVER_MUSIC
cd HANGOVER_MUSIC
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 main.py
```

---

## Commands
## How to Use..


- Enable the worker after deploy the project to Heroku.

- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy.(24*7 Music even if heroku restarts, radio stream restarts automatically).

- To play a song use /play as a reply to audio file or a youtube link.

- Use /play <song name> to play song from youtube and /dplay <song name> to play from Deezer.

- Use /help to know about other commands.


---

#### Support

## Join Now Telegram [Support Group](https://t.me/Xmarty_Support)

## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](https://replit.com/@S780821/PyrogramSession) of the account.
- Userbot Needs To Be Admin In The Channel or Group.
- Must Start A Voice Chat In Channel/Group Before Running The Bot.

## License
```sh
#!/usr/bin/env python3
# Copyright (C) @S780821
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

---

## Credits

- [Xmarty](https://github.com/S780821) [Dev]
