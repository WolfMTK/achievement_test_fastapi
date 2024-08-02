EXAMPLE_GET_ACHIEVEMENTS_USER_RESPONSE = {
    200: {
        'description': 'Successful Response',
        'content': {
            'application/json': {
                'example': {
                    'total': 10,
                    'limit': 2,
                    'offset': 0,
                    'userId': 'd7b62fbd-63d8-491e-ba08-12d8e403b54a',
                    'achievements': [
                        {
                            'id': '3d41dbf7-eff3-4c90-b5ad-12ddcee1b232',
                            'name': 'Сердце на рукаве',
                            'numberPoints': 150,
                            'description': 'Отреагируйте на что-либо '
                                           'на GitHub с помощью эмодзи ❤️'
                        },
                        {
                            'id': '5847d89a-8b9a-46d6-b5f0-483e393c5461',
                            'name': 'Открытый источник',
                            'numberPoints': 150,
                            'description': 'Вы сделали PR в несколько '
                                           'общедоступных репозиториев '
                                           'и эти PR были смёржены'
                        }
                    ]
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
