EXAMPLE_GET_USERS_WITH_MAX_POINTS_DIFF_RESPONSE = {
    200: {
        'description': 'Successful Response',
        'content': {
            'application/json': {
                'example': [
                    {
                        'id': 'd7b62fbd-63d8-491e-ba08-12d8e403b54a',
                        'name': 'Иван',
                        'totalPoints': 2870,
                        'maxDiff': 2820
                    },
                    {
                        'id': 'ec6efab8-0816-4dc3-a397-234d1a084796',
                        'name': 'Илья',
                        'totalPoints': 50,
                        'maxDiff': 2820
                    }
                ]
            }
        }
    },
    404: {
        'description': 'Not Found',
        'content': {
            'application/json': {
                'example': {
                    'detail': 'Пользователи с максимальной разностью '
                              'очков достижений не найдены'
                }
            }
        }
    }
}
