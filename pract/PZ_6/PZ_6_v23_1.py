# Дан целочисленный список размера N, не содержащий одинаковых чисел.
# Проверить, образуют ли его элементы арифметическую прогрессию. Если образуют,
# то вывести разность прогрессии, если нет — вывести 0.

def check_progression():
    try:
        n = int(input("Введите размер списка N: "))
        if n <= 0:
            print("Ошибка: Размер списка должен быть больше 0.")
            return

        source_list = []
        print(f"Введите {n} целых чисел (каждое с новой строки):")
        for _ in range(n):
            number = int(input())
            source_list.append(number)

        has_duplicates = False
        for item in source_list:
            if source_list.count(item) > 1:
                has_duplicates = True
                break

        if has_duplicates:
            print("Ошибка: Список содержит повторяющиеся числа.")
            return

        print(f"\nИсходный список: {source_list}")

        if n == 1:
            result = 0
        else:
            sorted_list = list(source_list)
            sorted_list.sort()

            d = sorted_list[1] - sorted_list[0]

            is_progression = True
            for i in range(2, n):
                if sorted_list[i] - sorted_list[i - 1] != d:
                    is_progression = False
                    break

            result = d if is_progression else 0

        print(f"Результат {result}")

    except ValueError:
        print("Ошибка: Пожалуйста, вводите только целые числа.")

check_progression()
