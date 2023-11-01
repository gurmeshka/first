import random
import time
scores = 0
while True:
    user = input("Выберите: камень, ножницы или бумага (для выхода введите 'выход'): ")

    if user == "выход":
        break
#     if user != "камень" or user != "ножницы" or user != "бумага": # знак неравенства обозначается восклицательным и равно
#         print("некорректный выбор. Попробуйте еще раз.")
#         continue

    computer = random.randint(1,3) # задаем диапазон выбора компьютера от 1 до 3

    print(f"Ваш выбор: {user}")
    print(f"Выбор компьютера: {computer}")

    if user == "камень" and computer == 1:
        print("ничья")
    if user == "ножницы" and computer == 2:
        print("ничья")
    if user == "бумага" and computer == 3:
        print("ничья")
    
    if user == "камень" and computer == 2:
        scores += 1 # scores = scores + 1
        print("Победил игрок, ваших очков: ", scores)
    if user == "бумага" and computer == 1:
        scores += 1 # scores = scores + 1
        print("Победил игрок, ваших очков: ", scores)
    if user == "ножницы" and computer == 3:
        scores += 1 # scores = scores + 1
        print("Победил игрок, ваших очков: ", scores)

    if user == "ножницы" and computer == 1:
        scores -= 1 # scores = scores - 1
        print("Победил компьютер, ваших очков: ", scores)
    if user == "камень" and computer == 3:
        scores -= 1 # scores = scores - 1
        print("Победил компьютер, ваших очков: ", scores)
    if user == "бумага" and computer == 2:
        scores -= 1 # scores = scores - 1
        print("Победил компьютер, ваших очков: ", scores)

    elif scores >= 3:
        print("Победил игрок")
        break
    elif scores <= -3:
        print("Победил компьютер") 
        break
