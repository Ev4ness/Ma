# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
"https://mallucampaign.in/images/img_1708089817.jpg",
"https://mallucampaign.in/images/img_1708089807.jpg",
"https://mallucampaign.in/images/img_1708089809.jpg",
"https://mallucampaign.in/images/img_1708089810.jpg",
"https://mallucampaign.in/images/img_1708089810.jpg",
"https://mallucampaign.in/images/img_1708089812.jpg",
"https://mallucampaign.in/images/img_1708089813.jpg",
"https://mallucampaign.in/images/img_1708089814.jpg",
"https://mallucampaign.in/images/img_1708089815.jpg",
"https://mallucampaign.in/images/img_1708089818.jpg",
]

HEY_IMG = "https://mallucampaign.in/images/img_1708089814.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

FIRST_PART_TEXT = "*Hello* `{}` . . ."

PM_START_TEXT = "*Hai, saya adalah bot manajemen grup bertema Anime. Di bangun untuk membantu memudahkan anda mengelola group dan channels*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="ADD ME",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="Miko_"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="more_ai_handler"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="𝖨𝖭𝖥𝖮", callback_data="ai_more_ai_handler"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="ADD ME",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Usern4meDoesNotExist404"),
        ib(text="SUPPORT", url="https://t.me/SpotifyStream_Id"),
    ],
    [
        ib(
            text="ADD ME",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
*Bee - Robot*

*Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
