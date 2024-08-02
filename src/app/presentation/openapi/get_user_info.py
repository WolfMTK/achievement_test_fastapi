EXAMPLE_GET_USER_INFO_RESPONSE = {
    200: {
        'description': 'Successful Response',
        'content': {
            'application/json': {
                'example': {
                    'id': 'd7b62fbd-63d8-491e-ba08-12d8e403b54a',
                    'name': 'Иван',
                    'language': 'ru'
                }
            }
        }
    },
    404: {
        'description': 'Not Found',
        'content': {
            'application/json': {
                'example': {
                    'detail': 'Пользователь не найден'
                }
            }
        }
    }
}
