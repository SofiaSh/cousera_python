# Напишите декоратор to_json,
# который можно применить к различным функциям,
# чтобы преобразовывать их возвращаемое значение в JSON-формат.

import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped


