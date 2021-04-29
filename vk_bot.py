import bs4
import requests

class VkBot:
    g = False

    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ["ПРИВЕТ", "ПОКА","ЗДРАВСТВУЙ","ЗДРАВСТВУЙТЕ","ДОБРЫЙ ДЕНЬ",
                          "ПРИВЕТСТВУЮ", "ДО СВИДАНИЯ", "ДО ВСТРЕЧИ", "ПРОЩАЙ","МНЕ ПОРА","ТЕМЫ"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    # Метод для очистки от ненужных тэгов

    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

    def new_message(self, message):

        # Привет
        if (message.upper() == self._COMMANDS[0] or message.upper() == self._COMMANDS[2] or
                message.upper() == self._COMMANDS[3] or message.upper() ==self._COMMANDS[4] or
                message.upper() == self._COMMANDS[5]):
            return f"Привет, {self._USERNAME}!"

        # Пока
        elif (message.upper() == self._COMMANDS[1] or message.upper() == self._COMMANDS[6] or
              message.upper() == self._COMMANDS[7] or message.upper() == self._COMMANDS[8] or
                message.upper() == self._COMMANDS[9]):
            return f"Пока, {self._USERNAME}!"
        elif (message.upper() == self._COMMANDS[10]):
            return "Темы:\n1)Города\n2)Животные\n3)Машины"

        elif((message.upper()).find("ДЕЛА") != -1 or (message.upper()).find("НАСТРОЕНИЕ") != -1):
            return "У меня всё отлично!"
        elif ((message.upper()).find("ИЗИ") != -1 or (message.upper()).find("ЛЕГКО") != -1):
            return "А МНЕ СЛОЖНО,Я БОТ!"



        else:
            return "Не понимаю о чем вы..."

