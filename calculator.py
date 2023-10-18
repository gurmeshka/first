while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выйти")

    choice = input("Введите номер операции (1/2/3/4/5): ")
    if choice == '5':
        break
    if choice not in ('1', '2', '3', '4',):
        print("Некорректный ввод")
        continue

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        result = num1 / num2
        if num2 == 0:
            print("Деление на ноль невозможно")
            continue
    else:
        print("Некорректный ввод")
        continue
    print("Результат:", result)