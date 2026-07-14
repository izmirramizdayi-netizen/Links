# keyboards.py

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


# =========================
# ANA MENÜ
# =========================

def main_menu_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "👤 Profil",
                callback_data="profile"
            ),

            InlineKeyboardButton(
                "📊 İstatistik",
                callback_data="stats"
            )
        ],

        [
            InlineKeyboardButton(
                "📂 Dosyalar",
                callback_data="files"
            )
        ],

        [
            InlineKeyboardButton(
                "⚙️ Ayarlar",
                callback_data="settings"
            )
        ],

        [
            InlineKeyboardButton(
                "❓ Yardım",
                callback_data="help"
            )
        ]

    ]

    return InlineKeyboardMarkup(
        keyboard
    )


# =========================
# ADMİN MENÜ
# =========================

def admin_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "👥 Kullanıcılar",
                callback_data="users"
            )
        ],

        [
            InlineKeyboardButton(
                "📈 Sistem Durumu",
                callback_data="system"
            )
        ],

        [
            InlineKeyboardButton(
                "📜 Loglar",
                callback_data="logs"
            )
        ],

        [
            InlineKeyboardButton(
                "🗑 Dosya Yönetimi",
                callback_data="file_manage"
            )
        ]

    ]

    return InlineKeyboardMarkup(
        keyboard
    )


# =========================
# ONAY BUTONLARI
# =========================

def confirm_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "✅ Onayla",
                callback_data="confirm"
            ),

            InlineKeyboardButton(
                "❌ İptal",
                callback_data="cancel"
            )
        ]

    ]

    return InlineKeyboardMarkup(
        keyboard
    )


# =========================
# GERİ BUTONU
# =========================

def back_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "⬅️ Geri",
                callback_data="back"
            )
        ]

    ]

    return InlineKeyboardMarkup(
        keyboard
    )