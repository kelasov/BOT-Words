from pyexpat.errors import messages

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_bot import VkBot
game = False
cities_list = ['Абинск', 'Алжир', 'Амстердам', 'Анкара', 'Атланта', 'Астана', 'Анталия',
               'Александровск', 'Анапа', 'Балашиха', 'Баку', 'Барнаул', 'Белград',
               'Белгород', 'Берлин', 'Бишкек', 'Бразилиа', 'Брест', 'Будапешт', 'Бухарест',
               'Брянск', 'Видное', 'Варшава', 'Вашингтон', 'Венеция', 'Владивосток',
               'Владикавказ', 'Владимир', 'Волгоград', 'Воронеж', 'Гусев', 'Гуково',
               'Гамбург', 'Гонконг', 'Гуанчжоу', 'Детройт', 'Днепропетровск',
               'Донецк', 'Дубай', 'Дублин', 'Ереван', 'Евпатория', 'Екатеринбург', 'Ессентуки',
               'Женева', 'Железноводск', 'Жуков', 'Житомир', 'Заволжск', 'Забже', 'Зеленоград',
               'Зардоб', 'Иваново', 'Иерусалим', 'Ижевск', 'Иркутск', 'Ибица',
               'Ибадан', 'Идку', 'Изра', 'Йошкар-Ола', 'Йоханнесбург', 'Йезд',
               'Йоэнсуу', 'Йилове', 'Киев', 'Казань', 'Каир', 'Калининград', 'Калуга', 'Киров',
               'Клин', 'Кавала', 'Котор', 'Кемер', 'Кишинёв', 'Кёльн', 'Катания', 'Казань'
               'Копенгаген', 'Краков', 'Каунас', 'Львов', 'Липецк', 'Луганск', 'Лондон',
               'Лос-Анджелес', 'Лиссабон', 'Лиссабон', 'Лион', 'Лас-Вегас', 'Москва',
               'Минск', 'Муром', 'Магадан', 'Мадрид', 'Мытищи', 'Мюнхен', 'Мурманск',
               'Магнитогорск', 'Малага', 'Марбелья', 'Мцхета', 'Майами', 'Мекка',
               'Медина', 'Мехико', 'Марса-Алам', 'Майкоп', 'Находка', 'Нью-Йорк',
               'Нижний Новгород', 'Новосибирск', 'Нячанг', 'Нетания', 'Ницца',
               'Нарва', 'Нагасаки', 'Ниш', 'Нюрнберг', 'Назарет', 'Ното', 'Никосия',
               'Одесса', 'Орёл', 'Омск', 'Ош', 'Оренбург', 'Орджоникидзе', 'Осло', 'Осака',
               'Олюдениз', 'Ольбия', 'Орландо', 'Орлеан', 'Париж', 'Прага', 'Пенза',
               'Пятигорск', 'Пекин', 'Питкяранта', 'Псков', 'Пафос', 'Полтава', 'Плес',
               'Рим', 'Рига', 'Ростов-на-Дону', 'Римини', 'Ровно', 'Рыбинск', 'Родос',
               'Рио-де-Жанейро', 'Рустави', 'Ретимно', 'Руан', 'Санкт-Петербург', 'Сочи',
               'Смоленск', 'Саратов', 'Самара', 'Сергиев Посад', 'Стамбул', 'Сусс', 'Сингапур',
               'Тула', 'Токио', 'Ташкент', 'Тунис', 'Тамбов', 'Тиват', 'Тольятти', 'Тель-Авив',
               'Тбилиси', 'Таганрог', 'Таллин', 'Уфа', 'Ухта', 'Углич', 'Улан-Удэ',
               'Ужгород', 'Утрехт', 'Урбино', 'Уотерфорд', 'Уагадугу', 'Удонтхани', 'Ушуайя',
               'Флоренция', 'Фамагуста', 'Фетхие', 'Фантьет', 'Феодосия', 'Форос', 'Филадельфия',
               'Фес', 'Фонтенбло', 'Харьков', 'Хабаровск', 'Ханой', 'Хаммамет', 'Херсон', 'Хельсинки',
               'Харбин', 'Хум', 'Ханчжоу', 'Хеб', 'Цюрих', 'Циндао', 'Цетинье', 'Цюйфу',
               'Целье', 'Чикаго', 'Чернигов', 'Честер', 'Чианграй', 'Череповец', 'Честер',
               'Чианграй', 'Чунцин', 'Черчилл', 'Шанхай', 'Шарм-эль-Шейх', 'Шымкент',
               'Шеки', 'Штутгарт', 'Шлиссельбург', 'Шахрисабз', 'Шеффилд', 'Шибеник',
               'Шефшауен', 'Щавница', 'Щёкино', 'Щецин', 'Щирк', 'Щучинск', 'Эйлат',
               'Энгельс', 'Элиста', 'Эрдэнэт', 'Эдинбург', 'Эр-Рияд', 'Этрета', 'Эдмонтон',
               'Южно-Сахалинск', 'Юрьев-Польский', 'Южная Тарава', 'Юрмала', 'Якутск',
               'Ялта', 'Янгон', 'Ямусукро', 'Яунде', 'Ясотхон', 'Ярен']
available_cities = []
f=0
g = False
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(1, 12345)})
def send(user_id, attachment):
    random_id = random.randint(-2147483648, +2147483648)
    vk.messages.send(
        peer_id=user_id,
        random_id=random_id,
        message="Новый пост в группе!",
        attachment=attachment
        )

# API-ключ созданный ранее
token = "7f01bd30503c6569890e7db68405eda188e37e1ac78225632b62fc07da571e27e3048881ba4fef08a93f8"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
print("Server started")
bot_answer = random.choice(cities_list)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if(f==0):
                write_msg(event.user_id, 'Инструкция https://m.vk.com/wall-203348139_4')
                f=1


            bot = VkBot(event.user_id)
            if((event.text!= "Начать" and event.text!= "начать") and g ==False):
                write_msg(event.user_id, bot.new_message(event.text))
            elif((event.text== "Начать" or event.text== "начать") and g ==False):
                g = True
                write_msg(event.user_id, 'Игра началась')
                bot_answer = random.choice(cities_list)
                available_cities.append(bot_answer)
                write_msg(event.user_id, bot_answer)

            elif(g==True):
                a = bot_answer[-1]
                if (a == "ы" or a == "ь"):
                    a = bot_answer[-2]

                if event.text == 'Конец'or event.text == 'конец':
                    g = False
                    available_cities = []
                    write_msg(event.user_id, 'Спасибо за игру!')
                elif event.text[0].upper() != a.upper():
                    write_msg(event.user_id, 'Город должен начинаться с буквы ' + bot_answer[-1].upper() + '.')
                else:
                    event.text = event.text[0].upper() + event.text[1:]

                    if event.text not in cities_list:
                        write_msg(event.user_id, 'Я не знаю такого города.')
                    elif event.text in available_cities:
                        write_msg(event.user_id, 'Этот город уже называли.')
                    else:
                        available_cities.append(event.text)
                        b = event.text[-1]
                        if (b == "ы" or b == "ь"):
                            b = event.text[-2]

                        for option_bot_answer in cities_list:
                            if option_bot_answer.lower()[0] == b and option_bot_answer not in available_cities:
                                bot_answer = option_bot_answer
                                available_cities.append(option_bot_answer)
                                write_msg(event.user_id, option_bot_answer)
                                break
                        else:
                            g = False
                            available_cities = []
                            write_msg(event.user_id, 'Я не знаю больше городов на букву "' + b + '". Ты победил!')



