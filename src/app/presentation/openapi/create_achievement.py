EXAMPLE_CREATE_ACHIEVEMENT_RESPONSE = {
    201: {
        'description': 'Created',
        'content': {
            'application/json': {
                'example': {
                    'id': 'c9770083-b15b-4ad2-9294-de5a1808a31f',
                    'name': 'Сердце на рукаве | A heart on a sleeve',
                    'numberPoints': 150,
                    'description': 'Отреагируйте на что-либо на GitHub '
                                   'с помощью эмодзи ❤️ | React to something '
                                   'on GitHub with an emoji ❤️'
                }
            }
        }
    },
    404: {
        'description': 'Bad Request',
        'content': {
            'application/json': {
                'example': {
                    'detail': 'Достижение с таким названием уже создано'
                }
            }
        }
    }
}

EXAMPLE_CREATE_ACHIEVEMENT_BODY = {
    'name': 'Сердце на рукаве | A heart on a sleeve',
    'numberPoints': 150,
    'description': 'Отреагируйте на что-либо на GitHub '
                   'с помощью эмодзи ❤️ | React to something '
                   'on GitHub with an emoji ❤️'
}
