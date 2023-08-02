"""
Apache License 2.0
Copyright (c) 2022 @EDGE_BOTS
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>𝓗𝓔𝓨 {} 👋,
𝓣ʜɪ𝓼 𝓘𝓼 𝓐ɴ 𝓐ᴅᴠᴀɴᴄᴇᴅ 𝓡ᴇɴᴀᴍᴇ 𝓑ᴏᴛ
𝓤𝓼ɪɴɢ 𝓣ʜɪ𝓼 𝓑ᴏᴛ 𝓨ᴏᴜ 𝓒ᴀɴ 𝓡ᴇɴᴀᴍᴇ & 𝓒ʜᴀɴɢᴇ 𝓣ʜᴜᴍʙɴᴀɪʟ 𝓞ꜰ 𝓨ᴏᴜʀ 𝓕ɪʟᴇ
𝓣ʜɪ𝓼 𝓑ᴏᴛ 𝓐ʟꜱᴏ 𝓢ᴜᴘᴘᴏʀᴛ𝓼 𝓒ᴜ𝓼ᴛᴏᴍ 𝓣ʜᴜᴍʙɴᴀɪʟ 𝓐ɴᴅ 𝓒ᴜ𝓼ᴛᴏᴍ 𝓒ᴀᴘᴛɪᴏɴ
𝓣ʜɪ𝓼 𝓑ᴏᴛ 𝓦ᴀ𝓼 𝓒ʀᴇᴀᴛᴇᴅ 𝓑ʏ : @𝓜 @ᴍᴏɴᴋᴇʏ_ᴅ_ʟᴜᴜꜰʏ ⚡️</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├➽ ᴍy ɴᴀᴍᴇ : {}
├➽ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href=https://t.me/Monkey_d_luufy>LUFFY</a> 
├➽ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├➽ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├➽ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>    
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
  
<b>➽</b> /start ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
<b>➽</b> /del_thumb ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
<b>➽</b> /view_thumb ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>
<b>➽</b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>➽</b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>➽</b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}
✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>➽</b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/MONKEY_D_LUUFY>𝑶𝑾𝑵𝑬𝑹</a>
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @MONKEY_D_LUUFY🙏🥲
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ TO Dᴇᴠᴇʟᴏᴩᴇʀ</b></u>
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/owaisnaeem2006/EDGE-RENAME-BOT>𝐄𝐃𝐆𝐄 𝐑𝐄𝐍𝐀𝐌𝐄 𝐁𝐎𝐓</a>
» 𝗛𝗢𝗪 𝗧𝗢 𝗗𝗘𝗣𝗟𝗢𝗬 : <a href=https://youtu.be/GfulqsSnTv4>MᴏTᴇᴄʜ Yᴛ</a>
• ❣️ <a href=https://t.me/Monkey_d_luufy>𝐌𝐎𝐍𝐊𝐄𝐘 𝐃 𝐋𝐔𝐅𝐅𝐘</a>

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣➽ 🗃️ Sɪᴢᴇ: {1} | {2}
┣➽ ⏳️ Dᴏɴᴇ : {0}%
┣➽ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣➽ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


