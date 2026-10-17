# Даны целые положительные числа N и K. Найти сумму 1K + 2К + ... + NK
# k - степень

while True:
    try:
        n = int(input("Введите целое положительное число n: "))
        if n > 0:
            break
        print("Число должно быть больше нуля!")
    except ValueError:
        print("Неправильно ввели! Это должно быть целое число.")

while True:
    try:
        k = int(input("Введите целое положительное число k: "))
        if k > 0:
            break
        print("Число должно быть больше нуля!")
    except ValueError:
        print("Неправильно ввели! Это должно быть целое число.")

total_sum = 0
i = 0

while i <= n:
    total_sum += i ** k
    i += 1

print("Результат: ", total_sum)
