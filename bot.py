# bot.py

import logging

from telegram.ext import (
    Application
)

from config import (
    BOT_TOKEN,
    check_config
)

from database import (
    init_database
)


# Handler importları

from handlers.start import get_start_handlers
from handlers.help import get_help_handlers
from handlers.settings import get_settings_handlers
from handlers.files import get_file_handlers


# =========================
# LOG AYARLARI
# =========================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


logger = logging.getLogger(
    __name__
)



# =========================
# BOT BAŞLAT
# =========================

def main():

    print(
        "🚀 PythonUtilityBot başlatılıyor..."
    )


    # Config kontrol

    errors = check_config()

    if errors:

        for error in errors:
            print(
                "❌",
                error
            )

        return



    # Database hazırla

    init_database()


    # Telegram uygulaması

    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )



    # =========================
    # HANDLERLAR
    # =========================

    handlers = []


    handlers.extend(
        get_start_handlers()
    )


    handlers.extend(
        get_help_handlers()
    )


    handlers.extend(
        get_settings_handlers()
    )


    handlers.extend(
        get_file_handlers()
    )



    for handler in handlers:

        app.add_handler(
            handler
        )



    print(
        "✅ Bot aktif!"
    )


    # Bot çalıştır

    app.run_polling(
        drop_pending_updates=True
    )



# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print(
            "\n🛑 Bot kapatıldı."
        )

    except Exception as e:

        logger.exception(
            e
        )