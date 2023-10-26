# Получение трех целых чисел
num1 = int(input("Введите первое число целое число: "))
num2 = int(input("Введите второе число целое число: "))
num3 = int(input("Введите третье число целое число: "))

# Находим максимум
maximum = max(num1, num2, num3)

# Находим минимум
minimum = min(num1, num2, num3)

# Находим среднее число, исключив максимум и минимум
average = num1 + num2 + num3 - maximum - minimum

# Вывод результатов
print("Максимум:", maximum)
print("Миимум", minimum)
print("Среднее", average)