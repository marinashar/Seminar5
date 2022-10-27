# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется 
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# играют два игрока:
# from random import randint

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = 150
# flag = randint(0,2) 
# if flag:
#     print(f"{player1} начинает")
# else:
#     print(f"{player2} начинает")

# def amount(name):
#     count_candy = int(input(f"{name}, сколько конфет, возьмете от 1 до 28: "))
#     while count_candy < 1 or count_candy > 28:
#         count_candy = int(input(f"{name}, еще раз, от 1 до 28 штук: "))
#     return count_candy

# def stepic(name, p, counter, value):
#     print(f"Игрок {name} походил и взял {p} конфет. {name} владеет {counter} конфетами. На столе осталось {value} конфет.")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         p = amount(player1)
#         counter1 += p
#         value -= p
#         flag = False
#         stepic(player1, p, counter1, value)
#     else:
#         p = amount(player2)
#         counter2 += p
#         value -= p
#         flag = True
#         stepic(player2, p, counter2, value)

# if flag:
#     print(f"{player1}, поздравляем! Ты - победитель!")
# else:
#     print(f"{player2}, поздравляем! Ты - победитель!")


# игра против бота
# from random import randint

# player1 = input("Введите имя первого игрока: ")
# player2 = "Бот"
# value = 150
# flag = randint(0,2) 
# if flag:
#     print(f"{player1} начинает")
# else:
#     print(f"{player2} начинает")

# def amount(name):
#     count_candy = int(input(f"{name}, сколько конфет, возьмете от 1 до 28: "))
#     while count_candy < 1 or count_candy > 28:
#         count_candy = int(input(f"{name}, еще раз, от 1 до 28 штук: "))
#     return count_candy

# def stepic(name, p, counter, value):
#     print(f"Игрок {name} походил и взял {p} конфет. {name} владеет {counter} конфетами. На столе осталось {value} конфет.")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         p = amount(player1)
#         counter1 += p
#         value -= p
#         flag = False
#         stepic(player1, p, counter1, value)
#     else:
#         p = randint(1,29)
#         counter2 += p
#         value -= p
#         flag = True
#         stepic(player2, p, counter2, value)

# if flag:
#     print(f"{player1}, поздравляем! Ты - победитель!")
# else:
#     print(f"{player2}, поздравляем! Ты - победитель!")

# игра против Бота с интелектом
from random import randint

player1 = input("Введите имя первого игрока: ")
player2 = "Бот"
value = 150
flag = randint(0,2) 
if flag:
    print(f"{player1} начинает")
else:
    print(f"{player2} начинает")

def amount(name):
    count_candy = int(input(f"{name}, сколько конфет, возьмете от 1 до 28: "))
    while count_candy < 1 or count_candy > 28:
        count_candy = int(input(f"{name}, еще раз, от 1 до 28 штук: "))
    return count_candy

def stepic(name, p, counter, value):
    print(f"Игрок {name} походил и взял {p} конфет. {name} владеет {counter} конфетами. На столе осталось {value} конфет.")

def botIntelect(value):
    s = randint(1,29)
    while value-s <= 28 and value > 29:
        s = randint(1,29)
    return s

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        p = amount(player1)
        counter1 += p
        value -= p
        flag = False
        stepic(player1, p, counter1, value)
    else:
        p = randint(1,29)
        counter2 += p
        value -= p
        flag = True
        stepic(player2, p, counter2, value)

if flag:
    print(f"{player1}, поздравляем! Ты - победитель!")
else:
    print(f"{player2}, поздравляем! Ты - победитель!")

