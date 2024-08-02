EXAMPLE_GET_USERS_WITH_MIN_POINTS_DIFF_RESPONSE = {
    200: {
        'description': 'Successful Response',
        'content': {
            'application/json': {
                'example': [
                    {
                        'id': 'a5faccdd-2144-4584-9728-172a188d8e41',
                        'name': 'Mary',
                        'totalPoints': 320,
                        'minDiff': 70
                    },
                    {
                        'id': 'c9788b61-9291-45ea-9c4c-37e4a5c73cd5',
                        'name': 'Дарина',
                        'totalPoints': 250,
                        'minDiff': 70
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
                    'detail': 'Пользователи с минимальной разностью '
                              'очков достижений не найдены'
                }
            }
        }
    }
}
