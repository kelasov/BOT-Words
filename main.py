from pyexpat.errors import messages
import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_bot import VkBot
game = False
cities_list = [[''], [''], [''], [''], [''], [''], ['']]

available_words = [[''], [''], [''], [''], [''], [''], ['']]

users=[]
f=[0]*10
GAME = [0] * 10
TEMA = [0] * 10
СHOISE_TEMA = [0] * 10

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(1, 12345)})
def write_photo(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': "", "attachment": "photo-203348139_457239021", "random_id": random.randint(1, 12345)})

def write_klav(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': "Меню вызвано", "keyboard": keyboard, "random_id": random.randint(1, 12345)})
def write_klav1(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': "Меню тем вызвано", "keyboard": keyboard1, "random_id": random.randint(1, 12345)})
def write_klav2(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': "Игровое меню вызвано", "keyboard": keyboard2, "random_id": random.randint(1, 12345)})

# API-ключ созданный ранее
token = "7f01bd30503c6569890e7db68405eda188e37e1ac78225632b62fc07da571e27e3048881ba4fef08a93f8"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Инструкция"
            },
            "color": "negative"
        }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Темы"
                },
                "color": "positive"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Начать"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Материалы c GitHub"
                },
                "color": "secondary"
            }]

    ]
}
keyboard1 = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "1"
            },
            "color": "negative"
        }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "2"
                },
                "color": "positive"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "3"
                },
                "color": "primary"
            }]
    ]
}

keyboard2 = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Конец"
            },
            "color": "negative"
        }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Использованные слова"
                },
                "color": "primary"
            }]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

keyboard1 = json.dumps(keyboard1, ensure_ascii=False).encode('utf-8')
keyboard1 = str(keyboard1.decode('utf-8'))

keyboard2 = json.dumps(keyboard2, ensure_ascii=False).encode('utf-8')
keyboard2 = str(keyboard2.decode('utf-8'))

# Работа с сообщениями
longpoll = VkLongPoll(vk)
print("Server started")
bot_answer = random.choice(cities_list)
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:


            if(event.user_id not in users):
                users.append(event.user_id)
                print(users)
            if(f[users.index(event.user_id)]==0):
                write_photo(event.user_id,"")
                write_klav(event.user_id, "Кнопка")


                f[users.index(event.user_id)] = 1
            START=0
            INSTR=0
            print(GAME[users.index(event.user_id)])

            if(((event.text).upper()).find("НАЧАТЬ")!= -1 or ((event.text).upper()).find("ЗАПУС") != -1
                        or ((event.text).upper()).find("НАЧАЛО")!= -1
                        or ((event.text).upper()).find("ИГР")!= -1
                        or ((event.text).upper()).find("ПОЕХАЛИ")!= -1):
                START = 1
            if (((event.text).upper()).find("ИНСТРУКЦИЯ") != -1 or ((event.text).upper()).find("ПРАВИЛА") != -1
                    or ((event.text).upper()).find("ЧТО") != -1):
                INSTR=1

            bot = VkBot(event.user_id)
            if((START==0) and (INSTR==0) and GAME[users.index(event.user_id)] == 0 and СHOISE_TEMA[users.index(event.user_id)] ==0):
                write_msg(event.user_id, bot.new_message(event.text))
            if ((START == 0) and (INSTR == 1) and GAME[users.index(event.user_id)] == 0 and СHOISE_TEMA[
                users.index(event.user_id)] == 0):
                write_photo(event.user_id,"")



            elif (START == 1 and GAME[users.index(event.user_id)] == 0 and СHOISE_TEMA[users.index(event.user_id)] ==0):
                write_msg(event.user_id, 'Игра началась')
                write_msg(event.user_id, 'Выберите тему:'
                                         '\n1)Города'
                                         '\n2)Животные'
                                         '\n3)Машины'
                                         '\n(напишите необходимое число)')
                write_klav1(event.user_id, "Кнопка")

                СHOISE_TEMA[users.index(event.user_id)] = 1

            elif(GAME[users.index(event.user_id)] == 0 and TEMA[users.index(event.user_id)] == 0
                  and СHOISE_TEMA[users.index(event.user_id)] == 1):
                write_klav2(event.user_id, 'Игра')
                if(((event.text).upper()).find("1")!= -1):
                    TEMA[users.index(event.user_id)] = 1
                    file = open('cities.txt', encoding='utf-8')
                    contents = file.read().split()
                    cities_list[users.index(event.user_id)] = contents
                    СHOISE_TEMA[users.index(event.user_id)] == 2
                    write_msg(event.user_id, 'Выбрана тема 1')
                    GAME[users.index(event.user_id)] = 1
                    bot_answer = random.choice(cities_list[users.index(event.user_id)])
                    available_words[users.index(event.user_id)].append(bot_answer)
                    write_msg(event.user_id, bot_answer)
                elif(((event.text).upper()).find("2")!= -1):
                    TEMA[users.index(event.user_id)] = 2
                    file = open('amimals.txt', encoding='utf-8')
                    contents = file.read().split()
                    cities_list[users.index(event.user_id)] = contents
                    СHOISE_TEMA[users.index(event.user_id)] == 2
                    write_msg(event.user_id, 'Выбрана тема 2')
                    GAME[users.index(event.user_id)] = 1

                    bot_answer = random.choice(cities_list[users.index(event.user_id)])
                    available_words[users.index(event.user_id)].append(bot_answer)
                    write_msg(event.user_id, bot_answer)
                elif (((event.text).upper()).find("3") != -1):
                    TEMA[users.index(event.user_id)] = 3
                    file = open('cars.txt', encoding='utf-8')
                    contents = file.read().split()
                    cities_list[users.index(event.user_id)] = contents
                    СHOISE_TEMA[users.index(event.user_id)] == 2
                    write_msg(event.user_id, 'Выбрана тема 3')
                    GAME[users.index(event.user_id)] = 1

                    bot_answer = random.choice(cities_list[users.index(event.user_id)])
                    available_words[users.index(event.user_id)].append(bot_answer)
                    write_msg(event.user_id, bot_answer)
                else:
                    write_msg(event.user_id, 'Напишите номер темы')



            elif(GAME[users.index(event.user_id)]==1):

                a = bot_answer[-1]
                if (a == "ы" or a == "ь"):
                    a = bot_answer[-2]

                if (((event.text).upper()).find("КОНЕЦ")!= -1 or ((event.text).upper()).find("ВСЁ") != -1
                        or ((event.text).upper()).find("ЗАКОНЧИТЬ")!= -1
                        or ((event.text).upper()).find("ХВАТИТ") != -1
                        or ((event.text).upper()).find("НЕ ЗНАЮ") != -1):
                    GAME[users.index(event.user_id)] = 0
                    СHOISE_TEMA[users.index(event.user_id)] = 0
                    TEMA[users.index(event.user_id)] = 0
                    available_words[users.index(event.user_id)] = []
                    write_msg(event.user_id, 'Спасибо за игру!')
                    write_klav(event.user_id, 'Игра')
                elif ((event.text).upper()).find("СЛОВА") != -1:
                    slist = ""
                    for i in range(len(available_words[users.index(event.user_id)])):
                        if(available_words[users.index(event.user_id)][i] != ""):
                            slist+= available_words[users.index(event.user_id)][i] + ", "
                    slist = slist[0:len(slist) - 2]
                    write_msg(event.user_id, slist)
                elif event.text[0].upper() != a.upper():
                    write_msg(event.user_id, 'Слово должно начинаться с буквы ' + a + '.')
                else:
                    event.text = event.text[0].upper() + event.text[1:]

                    if event.text not in cities_list[users.index(event.user_id)]:
                        write_msg(event.user_id, 'Я не знаю такого слова.')
                    elif event.text in available_words[users.index(event.user_id)]:
                        write_msg(event.user_id, 'Это слово уже называли.')

                    else:
                        available_words[users.index(event.user_id)].append(event.text)
                        b = event.text[-1]
                        if (b == "ы" or b == "ь"):
                            b = event.text[-2]

                        for option_bot_answer in cities_list[users.index(event.user_id)]:
                            if option_bot_answer.lower()[0] == b and option_bot_answer not in available_words[users.index(event.user_id)]:
                                bot_answer = option_bot_answer
                                available_words[users.index(event.user_id)].append(option_bot_answer)
                                write_msg(event.user_id, option_bot_answer)
                                break
                        else:
                            GAME[users.index(event.user_id)] = 0
                            СHOISE_TEMA[users.index(event.user_id)] = 0
                            TEMA[users.index(event.user_id)] = 0

                            available_words[users.index(event.user_id)] = []
                            write_msg(event.user_id, 'Я не знаю больше слов на букву "' + b + '". Ты победил!')
                            write_klav(event.user_id, 'Игра')



