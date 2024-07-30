EXAMPLE_GET_ADVANCES_RESPONSE = {
    200: {
        'description': 'Successful Response',
        'content': {
            'application/json': {
                'example': {
                    'total': 11,
                    'limit': 2,
                    'offset': 0,
                    'advances': [
                        {
                            'id': 'c9770083-b15b-4ad2-9294-de5a1808a31f',
                            'name': 'Сердце на рукаве|A heart on a sleeve',
                            'numberPoints': 150,
                            'description': 'Отреагируйте на что-либо на '
                                           'GitHub с помощью эмодзи ❤️|React '
                                           'to something on GitHub with '
                                           'an emoji ❤️'
                        },
                        {
                            'id': '6f4fa6fe-9b7e-4d5e-825e-7ee44b75c6fe',
                            'name': 'Открытый источник|The Open Source',
                            'numberPoints': 50,
                            'description': 'Вы сделали PR в несколько '
                                           'общедоступных репозиториев и '
                                           'эти PR были смёржены|You made PR '
                                           'to several publicly available '
                                           'repositories and those PR were '
                                           'smirked away'
                        }
                    ]
                }
            }
        }
    }
}
