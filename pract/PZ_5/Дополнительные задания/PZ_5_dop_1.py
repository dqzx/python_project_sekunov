# Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
# результата предусмотреть в основной программе. Расчет суммы цифр оформить в
# функции

def sumdigit(number):
    temp = abs(number)
    digits_sum = 0

    while temp > 0:
        digits_sum += temp % 10
        temp //= 10
    return digits_sum
try:
    numbera = int(input("Введите число A: "))
    numberb = int(input("Введите число B: "))
    numberc = int(input("Введите число C: "))

    sum_a = sumdigit(numbera)
    sum_b = sumdigit(numberb)
    sum_c = sumdigit(numberc)

    result_sum = max(sum_a, sum_b, sum_c)

    if sum_a == result_sum:
        print(f"самая большая сумма у числа A :{sum_a}")

    if sum_b == result_sum:
        print(f"самая большая сумма у числа B :{sum_b}")

    if sum_c == result_sum:
        print(f"самая большая сумма у числа C :{sum_c}")

except ValueError:
    print("Произошла ошибка, введите корректное значение")