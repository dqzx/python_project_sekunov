# Дан список A размера N. Сформировать новый список B того же размера, элементы
# которого определяются следующим образом:
# BK = 2*AK, если AK < 5,
# AK/2 в противном случае.


def main():
    try:
        user_input = input("Введите элементы списка A через пробел: ")

        list_a = [float(x) for x in user_input.split()]

        if not list_a:
            print("Ошибка: список не должен быть пустым.")
            return

        list_b = []
        for ak in list_a:
            if ak < 5:
                bk = 2 * ak
            else:
                bk = ak / 2
            list_b.append(bk)

        print(f"Исходный список A: {list_a}")
        print(f"Результирующий список B: {list_b}")

    except ValueError:
        print("Ошибка: пожалуйста, вводите только числа.")

main()
