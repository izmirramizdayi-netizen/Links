# database.py

import sqlite3
from pathlib import Path
from datetime import datetime

from settings import DATABASE_PATH


# =========================
# DATABASE BAĞLANTISI
# =========================

def get_connection():

    return sqlite3.connect(
        DATABASE_PATH
    )


# =========================
# TABLOLARI OLUŞTUR
# =========================

def init_database():

    conn = get_connection()
    cursor = conn.cursor()


    # Kullanıcılar
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY,

        username TEXT,

        first_name TEXT,

        joined_at TEXT,

        requests INTEGER DEFAULT 0,

        status TEXT DEFAULT 'active'

    )
    """)


    # Loglar
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        action TEXT,

        created_at TEXT

    )
    """)


    # Dosyalar
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        filename TEXT,

        size TEXT,

        uploaded_at TEXT

    )
    """)


    conn.commit()
    conn.close()



# =========================
# USER EKLE
# =========================

def add_user(
    user_id,
    username,
    first_name
):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    INSERT OR IGNORE INTO users
    (
        id,
        username,
        first_name,
        joined_at
    )

    VALUES (?,?,?,?)
    """,
    (
        user_id,
        username,
        first_name,
        datetime.now().isoformat()
    ))


    conn.commit()
    conn.close()



# =========================
# USER GETİR
# =========================

def get_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM users WHERE id=?",
        (user_id,)
    )


    user = cursor.fetchone()

    conn.close()

    return user



# =========================
# TÜM KULLANICILAR
# =========================

def get_users():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM users"
    )


    users = cursor.fetchall()

    conn.close()

    return users



# =========================
# LOG EKLE
# =========================

def add_log(
    user_id,
    action
):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO logs
    (
        user_id,
        action,
        created_at
    )

    VALUES (?,?,?)
    """,
    (
        user_id,
        action,
        datetime.now().isoformat()
    ))


    conn.commit()
    conn.close()



# =========================
# İSTATİSTİK
# =========================

def get_stats():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    users = cursor.fetchone()[0]


    cursor.execute(
        "SELECT COUNT(*) FROM logs"
    )

    logs = cursor.fetchone()[0]


    conn.close()


    return {
        "users": users,
        "logs": logs
    }



# =========================
# BAŞLAT
# =========================

if __name__ == "__main__":

    init_database()

    print(
        "✅ Database hazır."
    )