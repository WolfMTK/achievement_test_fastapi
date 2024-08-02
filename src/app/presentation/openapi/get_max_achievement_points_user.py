EXAMPLE_GET_MAX_ACHIEVEMENT_POINTS_USER_RESPONSE = {
    200: {
        'description': 'Successful Response',
        'content': {
            'application/json': {
                'example': {
                    'id': 'd7b62fbd-63d8-491e-ba08-12d8e403b54a',
                    'name': 'Иван',
                    'totalPoints': 2870
                }
            }
        }
    },
    404: {
        'description': 'Not Found',
        'content': {
            'application/json': {
                'example': {
                    'detail': 'Пользователя с максимальными '
                              'очками достижений не найден'
                }
            }
        }
    }
}
