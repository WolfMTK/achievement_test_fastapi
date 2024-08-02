import emoji


def check_text(text: str, key: str) -> bool:
    """ Проверка текста. """
    text = emoji.replace_emoji(text, '')
    return not set(key).isdisjoint(text.lower())
