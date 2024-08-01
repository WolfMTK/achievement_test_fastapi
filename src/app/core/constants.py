from string import ascii_lowercase

RU_LOWERCASE = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
EN_LOWERCASE = ascii_lowercase

LENGTH_LANGUAGE = 2
LANGUAGE = {
    'ru': 0,
    'en': 1
}

# Лучше было, если бы данную переменную можно
# было изменять из БД (если в какой-то момент
# изменится бизнес-процесс)
DAYS_STREAK = 7
