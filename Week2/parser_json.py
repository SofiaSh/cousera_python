# Напишите декоратор to_json,
# который можно применить к различным функциям,
# чтобы преобразовывать их возвращаемое значение в JSON-формат.


def to_json():
    pass


@to_json
def get_data():
    return {'data': 42}


get_data()