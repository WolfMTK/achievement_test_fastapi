EXAMPLE_ADD_ACHIEVEMENT_USER_RESPONSE = {
    201: {
        'description': 'Created',
        'content': {
            'application/json': {
                'example': {
                    'userId': '7d36544c-f868-4f62-aee0-823c0d050001',
                    'achievementId': 'c6a64c3f-b387-4c0e-bae7-a1c1fd558b9c',
                    'dateOn': '2024-08-02 14:04'
                }
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

EXAMPLE_ADD_ACHIEVEMENT_USER_BODY = {
  'userId': '7d36544c-f868-4f62-aee0-823c0d050001',
  'achievementId': 'c6a64c3f-b387-4c0e-bae7-a1c1fd558b9c'
}
