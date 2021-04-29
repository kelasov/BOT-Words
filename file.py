cities_available = []
for i in range(2):
    with open('cities.txt', encoding='utf-8') as file:
        contents = file.read()
        search_word = input("Введите город: ")
        if search_word in contents:
            cities_available.append(search_word)
        else:
            print('Я не знаю такого города')
print(cities_available)


# f=open("data.txt","r+")
# s=(f.read())
# a=s.split(',')#вместо запятой может бить точка, любой символ
# print(a)   #(если у вас в файле дание через пробел топишем  пробел, через точку-точку)
# f.close()
# #то что в  файле 13,-45,-233,57,-2,76,3,7,12,34,2
# #виведет ['13', '-45', '-233', '57', '-2', '76', '3', '7', '12', '34', '2']
# в вашем случае вместо зпятой должно бить \n
# a=s.split('\n')
# будет читать-1 рядок-1 елемент лист