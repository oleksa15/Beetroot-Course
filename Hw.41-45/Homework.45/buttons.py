from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# --- Menu ---
btnWallpaper = InlineKeyboardButton('🖼 Wallpaper', callback_data='/wallpaper')
btnASCII = InlineKeyboardButton('🎨ASCII Art', callback_data='/ascii')
btnMenu = InlineKeyboardMarkup().add(btnWallpaper, btnASCII)