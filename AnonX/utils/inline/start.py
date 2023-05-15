from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_GROUP, OWNER_ID

def start_pannel(_, BOT_USERNAME):
    buttons = [       
        [
            InlineKeyboardButton(text="𝐂ommands 📚", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="𝐒ettings ⚙", callback_data="settings_helper"),
        ],
        ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝐀dd 𝐌e 𝐓o 𝐘our 𝐂hat ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            ),           
        ],
        [
            InlineKeyboardButton(text="𝐂ommands 📚", callback_data="settings_back_helper"),
        ],
                
    ]
    return buttons

close_key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝐂lose 🗑", callback_data="close"
                    )
                ]
            ]
        )
