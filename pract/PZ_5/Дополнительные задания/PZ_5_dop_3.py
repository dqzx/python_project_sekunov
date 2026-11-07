# Написать программу, подсчитывающую количество цифр числа, используя для
# этого функцию

def counter(number):
    count = 0
    temp = abs(number)

    if temp == 0:
        return 1

    while temp > 0:
        temp = temp // 10
        count += 1
    return count

try:
    number = int(input("Введите целое число "))

    function_call = counter(number)
    print(f"В числе: {function_call}")

except ValueError:
    print("Введите корректное значение")