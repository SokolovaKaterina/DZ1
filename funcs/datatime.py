import datetime


def gel_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0 <= current_time.hour < 6:
        return "Доброй ночи!🌕"
    if 6 <= current_time.hour < 12:
        return "Доброе утро!⛅️"
    if 12 <= current_time.hour < 18:
        return "Добрый день!☀️"
    else:
        return "Добрый вечер!🌥"
