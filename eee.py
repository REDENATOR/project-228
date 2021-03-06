from flask import Flask, request
import logging
from flask_ngrok import run_with_ngrok
import json

app = Flask(__name__)
run_with_ngrok(app)

users_storage = {}

plases_list = [
    {'name': "Краеведческий музей", 'img': "1521359/fc83d1d4b77cd349bc0c"},
    {'name': "Дом купца Дьякова", 'img': "1521359/d604230c98feed7e6002"},
    {'name': "Кафедральный собор Михаила Архангела", 'img': "1540737/499a1c2ece58ec6e1062"},
    {'name': "Театральный парк", 'img': "1540737/a75fa0ba207757d69411"},
    {'name': "Парк Имени Куйбешева", 'img': "1533899/8bca41464cee02e14c9f"}
]


def get_first_name(req):
    # перебираем сущности
    for entity in req['request']['nlu']['entities']:
        # находим сущность с типом 'YANDEX.FIO'
        if entity['type'] == 'YANDEX.FIO':
            # Если есть сущность с ключом 'first_name',
            # возвращаем ее значение.
            # Во всех остальных случаях возвращаем None.
            return entity['value'].get('first_name', None)


def start(user_id, reg, res):
    if get_first_name(reg):
        res['response']['text'] = f'Начнем, {get_first_name(reg)}. Первый вопрос: '
        session_state['user_id'] = {
            'state': 2
        }
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1521359/d604230c98feed7e6002",
            "title": "Дом купца Дьякова"
        }
        res['response']['buttons'] = [
            {
                "title": "Дом купца Дьякова",
                "hide": True
            },
            {
                "title": "Дом купца Давыдова",
                "hide": True
            }
        ]
        return
    else:
        res['response']['text'] = f'Представься'


def one_question(user_id, reg, res):
    if 'Дом купца Дьякова' in reg['request']['original_utterance'].lower():
        res['response']['text'] = f'Верно. Следующий вопрос: '
        users_storage[user_id]['ball'] += 1
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1521359/fc83d1d4b77cd349bc0c",
            "title": "Краеведческий музей"
        }
        res['response']['buttons'] = [
            {
                "title": "Музей имени Куйбешева",
                "hide": True
            },
            {
                "title": "Краеведческий музей",
                "hide": True
            }
        ]
    else:
        res['response']['text'] = f'Неверно. Следующий вопрос: '
        users_storage[user_id]['ball'] += 1
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1521359/fc83d1d4b77cd349bc0c",
            "title": "Краеведческий музей"
        }
        res['response']['buttons'] = [
            {
                "title": "Музей имени Куйбешева",
                "hide": True
            },
            {
                "title": "Краеведческий музей",
                "hide": True
            }
        ]

    session_state['user_id'] = {
        'state': 3
    }



def two_question(user_id, reg, res):
    if 'Дом купца Дьякова' in reg['request']['original_utterance'].lower():
        res['response']['text'] = f'Верно. Следующий вопрос: '
        users_storage[user_id]['ball'] += 1
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1521359/fc83d1d4b77cd349bc0c",
            "title": "Краеведческий музей"
        }
        res['response']['buttons'] = [
            {
                "title": "Музей имени Куйбешева",
                "hide": True
            },
            {
                "title": "Краеведческий музей",
                "hide": True
            }
        ]
    else:
        res['response']['text'] = f'Неверно. Следующий вопрос: '
        users_storage[user_id]['ball'] += 1
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1521359/fc83d1d4b77cd349bc0c",
            "title": "Краеведческий музей"
        }
        res['response']['buttons'] = [
            {
                "title": "Музей имени Куйбешева",
                "hide": True
            },
            {
                "title": "Краеведческий музей",
                "hide": True
            }
        ]

    session_state['user_id'] = {
        'state': 3
    }


def three_question(user_id, reg, res):
    if 'Краеведческий музей' in reg['request']['original_utterance'].lower():
        res['response']['text'] = f'Верно. Следующий вопрос: '
        users_storage[user_id]['ball'] += 1
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1540737/499a1c2ece58ec6e1062",
            "title": "Кафедралный собор Михаила Архангела"
        }
        res['response']['buttons'] = [
            {
                "title": "Кафедралный собор Виктора Корнеплодского",
                "hide": True
            },
            {
                "title": "Кафедралный собор Михаила Архангела",
                "hide": True
            }
        ]
    else:
        res['response']['text'] = f'Неверно. Следующий вопрос: '
        users_storage[user_id]['ball'] += 1
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1540737/499a1c2ece58ec6e1062",
            "title": "Кафедралный собор Михаила Архангела"
        }
        res['response']['buttons'] = [
            {
                "title": "Кафедралный собор Виктора Корнеплодского",
                "hide": True
            },
            {
                "title": "Кафедралный собор Михаила Архангела",
                "hide": True
            }
        ]

    session_state['user_id'] = {
        'state': 4
    }


def four_question(user_id, reg, res):
    if 'Кафедралный собор Михаила Архангела' in reg['request']['original_utterance'].lower():
        res['response']['text'] = f'Верно. Следующий вопрос: '
        users_storage[user_id]['ball'] += 1
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1533899/8bca41464cee02e14c9f",
            "title": "Парк Имени Куйбешева"
        }
        res['response']['buttons'] = [
            {
                "title": "Парк Имени Куйбешева",
                "hide": True
            },
            {
                "title": "Парк Имени Данила Можжевельника",
                "hide": True
            }
        ]
    else:
        res['response']['text'] = f'Неверно. Следующий вопрос: '
        users_storage[user_id]['ball'] += 1
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": "1533899/8bca41464cee02e14c9f",
            "title": "Парк Имени Куйбешева"
        }
        res['response']['buttons'] = [
            {
                "title": "Парк Имени Данила Можжевельника",
                "hide": True
            },
            {
                "title": "Парк Имени Куйбешева",
                "hide": True
            }
        ]

    session_state['user_id'] = {
        'state': 5
    }


def otvet(user_id, reg, res):
    if 'Парк Имени Куйбешева' in reg['request']['original_utterance'].lower():
        users_storage[user_id]['ball'] += 1
    res['response']['text'] = f'{get_first_name(reg)} вы набрали {users_storage[user_id]["ball"]} из 5 балов'
    if users_storage[user_id]['ball'] == 5:
        res['response']['text'] = f'Вы отлично знаете город!'
    if users_storage[user_id]['ball'] == 4 or users_storage[user_id]['ball'] == 3:
        res['response']['text'] = f'Вы неплохо знаете город! Но вым не помешало бы по нему погулять'
    if users_storage[user_id]['ball'] <= 2:
        res['response']['text'] = f'Вы вообще в нем были?'
    res['response']['end_session'] = True


@app.route('/post', methods=['POST'])
def get_alice_requests():
    response = {
        'session': request.json['session'],
        'version': request.json['session'],
        'response': {
            'end_session': False
        }
    }

    handle_dialog(request.json, response)
    return json.dumps(response)


def handle_dialog(req, res):
    user_id = req['session']['user_id']
    if req['session']['new']:
        res['response']['text'] = 'Привет я хочу сыграть с тобой в игру. Как тебя зовут?'
        users_storage[user_id] = {
            'ball': 0
        }
        session_state['user_id'] = {
            'state': 1
        }
        return
    states[session_state[user_id]['state']](user_id, req, res)


states = {
    1: start,
    2: one_question,
    3: two_question,
    4: three_question,
    5: four_question,
    6: otvet
}

session_state = {}
if __name__ == '__main__':
    app.run()
