# Даны целые положительные числа N и K. Найти сумму 1K + 2К + ... + NK
# k - степень

while True:
    try:
        a = int(input("Введите целое положительное число n: "))
        if a > 0:
            break
        print("Число должно быть больше нуля!")
    except ValueError:
        print("Неправильно ввели! Это должно быть целое число.")

# Запрашиваем число K (должно быть > 0)
while True:
    try:
        b = int(input("Введите целое положительное число k: "))
        if b > 0:
            break
        print("Число должно быть больше нуля!")
    except ValueError:
        print("Неправильно ввели! Это должно быть целое число.")

total_sum = 0
i = 0

while i <= a:
    total_sum += i ** b
    i += 1

print("Результат: ", total_sum)
