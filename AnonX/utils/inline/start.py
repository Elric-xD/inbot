from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_GROUP

def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            ),
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ channel",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            ),
        ],
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"),
        ],
        ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☃️ Aᴅᴅ Mᴇ ɪɴ Yᴏᴜʀ Gʀᴏᴜᴘ ☃️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            ),
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ channel",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            ),
        ],
        [
            InlineKeyboardButton(text="˹ꜱᴜᴘᴘᴏʀᴛ˼", url="https://t.me/Life_Codes"),
            InlineKeyboardButton(text="˹ᴜᴘᴅᴀᴛᴇꜱ˼", url="https://t.me/Life_Codes"),
        ],
        [
            InlineKeyboardButton(text="♡ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ♡", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="• Sᴏᴜʀᴄᴇ •", callback_data="gib_source"),
        ],
    ]
    return buttons

close_key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]
            ]
        )
