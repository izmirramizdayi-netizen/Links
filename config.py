# config.py

import os
from dotenv import load_dotenv

load_dotenv()


# =========================
# TELEGRAM BOT
# =========================

BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    "8173462789:AAFGwAb6sLywO5kiicssQeFAFaFCXz90wtk"
)


# Admin Telegram ID

ADMIN_ID = int(
    os.getenv(
        "ADMIN_ID",
        "6819423716"
    )
)


# =========================
# BOT BİLGİLERİ
# =========================

BOT_NAME = "𝐀𝐥𝐰𝐚𝐲𝐬𝐄𝐧𝐜𝐨𝐝𝐞"

VERSION = "1.0.0"

DESCRIPTION = (
    "Advanced Telegram Utility Bot"
)


# =========================
# DATABASE
# =========================

DATABASE_NAME = "database.db"

DATABASE_URL = (
    f"sqlite:///{DATABASE_NAME}"
)


# =========================
# DOSYA AYARLARI
# =========================

UPLOAD_FOLDER = "uploads"

MAX_UPLOAD_SIZE = 50  # MB


# =========================
# LOG AYARLARI
# =========================

LOG_FOLDER = "logs"

LOG_LEVEL = "INFO"


# =========================
# GÜVENLİK
# =========================

ENABLE_SECURITY = True

ENABLE_RATE_LIMIT = True

MAX_REQUESTS = 30


# =========================
# DİL
# =========================

DEFAULT_LANGUAGE = "tr"


# =========================
# GELİŞTİRİCİ MODU
# =========================

DEBUG = False


# =========================
# API AYARLARI
# =========================

REQUEST_TIMEOUT = 15


# =========================
# CONFIG KONTROL
# =========================

def check_config():

    errors = []


    if BOT_TOKEN == "BOT_TOKEN_BURAYA":
        errors.append(
            "Bot token ayarlanmamış!"
        )


    if ADMIN_ID == 123456789:
        errors.append(
            "Admin ID ayarlanmamış!"
        )


    return errors