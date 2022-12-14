import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

START_IMG = "https://telegra.ph/file/e758fc65d2522df6c46c3.jpg"

START_TEXT = """
Hello there 
**I am Assistant bot of [Rishmika Sandanu](https://t.me/ImRishmika)**

My Devoloer @ImRishmika

"""

START_BUTTON = InlineKeyboardMarkup(
               [
                [
                 InlineKeyboardButton("â¤ï¸\u200dð¥Aboutâ¤ï¸\u200dð¥", url='https://t.me/AboutRishmika'),
                 InlineKeyboardButton("â­ï¸Subscribeâ­ï¸", url='https://youtube.com/channel/UCTIprdrvIiMjFdFwJgnmTUg')
                ],
                [
                  InlineKeyboardButton("âââââââââââââââ", callback_data="stats_callback"),
                ],
                [
                  InlineKeyboardButton("ð Help and commands ð", callback_data='helpmenu'),
                ],
                [
                  InlineKeyboardButton("TeamSemmy", callback_data='t.me/TeamSemmy'),
                ],
                [
                  InlineKeyboardButton("Emo Bot Industry", callback_data='t.me/Emo_Bot_Industry'),
                ],
                ]
)

HELP_TEXT = """ Hey thereâï¸
I have some fun and useful tools
So you can get a help about them ð

>> Devoloper :- @ImRishmika
>> Powerd By [TeamSemmy](t.me/TeamSemmy) | [Emo Bot Industry](t.me/Emo_Bot_Industry)

"""

HELP_BUTTON = InlineKeyboardMarkup(
               [
                [
                 InlineKeyboardButton("Logo Maker", callback_data='logomenu'),
                 InlineKeyboardButton("Quote", callback_data='quotemenu')
                ],
                [
                  InlineKeyboardButton("Song Menu", callback_data='songmenu')
                ],
                [
                  InlineKeyboardButton("More Tools", callback_data='toolmenu')
                ],
                [
                  InlineKeyboardButton("Repo", url='https://github.com/RishBropromax/RishBropromax-Assistant-Bot')
                ],
                [
                  InlineKeyboardButton("ðBack", callback_data='startmenu'),
                ],
               ]
)

BOTSTATUS_TEXT = """
**Bá´á´ Sá´á´á´á´s** ```rá´á´á´ : ~ $ bá´sÊ```
Assistant Bot Of [Rishmika Sandanu](t.me/ImRishmika)
"""

BOTSTATUS_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('SÊsá´á´á´ sá´á´á´á´s ð»', callback_data='stats_')
        ]]
)

LOGO_TEXT = """
ð° Help for logo make ð°
* Logo Files By [Sithija Assistant Bot](t.me/ImsithijaBot)

Available commands
>> /logo {text} - create simple random logos
>> /write {text} - write something
>> /mlogo {text} - create srilankan mask logo
"""
LOGO_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ðBack', callback_data='helpmenu')
        ]]
)

TOOLS_TEXT = """
ð§° Help for More Tools ð§°
Here is the additional Tools of this bot.

Available commands
>> /covid - Get the Covid status of Srilanka

More tools add in future.
"""
TOOLS_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ðBack', callback_data='helpmenu')
        ]]
)

SONG_TEXT = """
ð§ Help for song download ð§

Available commands
>> /song {song name} - Download a song simply.
>> /song {youtube link} - Download song using youtube link.
"""
SONG_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ðBack', callback_data='helpmenu')
        ]]
)

QUOTE_TEXT = """
ð¬Help for Quoteð¬

Available commands
â¥ /q - Reply to a message to make it quote.
"""
QUOTE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ðBack', callback_data='helpmenu')
        ]]
)

SITHIJATD_TEXT = """ Heyâï¸,\n you can find Rishmika Sandanu in these social medias."""

SITHIJATD_BUTTONS = InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton('ðµ Telegram ðµ' , url='https://t.me/ImRishmika'),
                ],
                [
                  InlineKeyboardButton('â­ Youtube â­' , url='https://www.youtube.com/channel/UCTIprdrvIiMjFdFwJgnmTUg'),
                ], 
              ]
)
