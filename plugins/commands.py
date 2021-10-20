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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>ʜᴇʟʟᴏ, [{}](tg://user?id={})\n\nI am HANGOVER_RADIO 24×7.\n\nHits /help for more details...</b>"
HELP = """
**User Commands:**
▷/play **[song name]/[yt link]**: Reply to an audio file.
▷/dplay **[song name]:** Play music from Deezer.
▷/player:  Show current playing song.
▷upload: Uploads current playing song as audio file.
▷/help: Show help for commands.
▷/playlist: Shows the playlist.

**Admin Commands:**
▷/skip **[n]** ...  Skip current or n where n >= 2
▷cplay: Play music from a channel's music files.
▷/yplay: Play music from a youtube playlist.
▷/join: Join voice chat.
▷/leave: Leave current voice chat.
▷/shuffle: Shuffle Playlist.
▷/vc: Check which VC is joined.
▷/stop: Stop playing.
▷/radio: Start Radio.
▷/stopradio: Stops Radio Stream.
▷/clearplaylist: Clear the playlist.
▷/export: Export current playlist for future use.
▷/import: Import a previously exported playlist.
▷/replay: Play from the beginning.
▷/clean: Remove unused RAW PCM files.
▷/pause: Pause playing.
▷/resume: Resume playing.
▷/volume: Change volume(0-200).
▷/mute: Mute in VC.
▷/unmute: Unmute in VC.
▷/restart: Restarts the Bot.
"""



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("🔥 Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🔥", url='https://github.com/S780821/HANGOVER_RADIO'),
    ],
    [
        InlineKeyboardButton('👥 Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/xmarty_support'),
        InlineKeyboardButton('ᴄʜɪᴛᴄʜaᴛ ɢʀᴏᴜᴘ', url='https://t.me/welcomefriendclub'),
    ],
    [
        InlineKeyboardButton('🆘 ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs 🆘', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton("🔥 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🔥", url='https://github.com/S780821/HANGOVER_RADIO'),
        ],
        [
            InlineKeyboardButton('👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/xmarty_support'),
            InlineKeyboardButton('ᴄʜɪᴛᴄʜᴀᴛ ɢʀᴏᴜᴘ ', url='https://t.me/welcomefriendclub'),
        ],
        [
            InlineKeyboardButton('🗡️ ᴏᴡɴᴇʀ 🗡️', url='https://t.me/Xmartperson'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await message.delete()
@Client.on_message(filters.command(["restart", f"restart@{U}"]) & filters.user(Config.ADMINS))
async def restart(client, message):
    await message.reply_text("🔄 яєѕταяτιиg...")
    await message.delete()
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
    os.execl(sys.executable, sys.executable, *sys.argv)

