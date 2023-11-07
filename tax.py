# Получение дохода от пользователя
income = float(input("Введите ваш доход: "))

# Начальные значения для каждой из ставок налога
tax1_rate = 0.13
tax2_rate = 0.20
tax3_rate = 0.30

# Пределы для каждой из ставок налога
tax1_limit = 10000
tax2_limit = 50000

# Инициализация налога
tax = 0

# Вычисление налога с учетом прогрессивной шкалы
if income <= tax1_limit:
    tax = income * tax1_rate
elif income <= tax2_limit:
    tax = tax1_limit * tax1_rate + (income - tax1_limit) * tax2_rate
else:
    tax = tax1_limit * tax1_rate + (tax2_limit - tax1_limit) * tax2_rate + (income - tax2_limit) * tax3_rate

# Вывод суммы налога
print(f"Сумма налога: {tax:.2f} рублей")
