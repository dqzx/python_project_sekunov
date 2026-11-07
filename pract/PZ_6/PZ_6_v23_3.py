# Дано множество A из N точек (точки заданы своими координатами x, у). Среди всех
# точек этого множества, лежащих в первой или третьей четверти, найти точку,
# наиболее близкую к началу координат. Если таких точек нет, то вывести точку с
# нулевыми координатами.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат

def main():
    try:
        n_input = input("Введите количество точек N: ")
        n = int(n_input)
        if n <= 0:
            print("Ошибка: количество точек должно быть больше 0.")
            return

        x_coords = []
        y_coords = []

        print("Введите координаты точек:")
        for i in range(n):
            point_input = input(f"Точка {i + 1}: ").split()
            if len(point_input) != 2:
                print("Ошибка: необходимо ввести ровно два числа (x и y).")
                return

            x_coords.append(float(point_input[0]))
            y_coords.append(float(point_input[1]))

        print(f"\nИсходный список X: {x_coords}")
        print(f"Исходный список Y: {y_coords}")

        min_distance = float('inf')
        best_x, best_y = 0.0, 0.0
        found = False

        for i in range(n):
            x = x_coords[i]
            y = y_coords[i]

            is_in_first_quadrant = (x > 0 and y > 0)
            is_in_third_quadrant = (x < 0 and y < 0)

            if is_in_first_quadrant or is_in_third_quadrant:
                distance = (x ** 2 + y ** 2) ** 0.5

                if distance < min_distance:
                    min_distance = distance
                    best_x = x
                    best_y = y
                    found = True

        if found:
            print(f"\nНайдена ближайшая точка: ({best_x}, {best_y})")
            print(f"Расстояние до начала координат: {min_distance:.4f}")
        else:
            print(f"\nТочки в 1 или 3 четвертях не найдены.")
            print(f"Вывод согласно условию: ({best_x}, {best_y})")

    except ValueError:
        print("Ошибка: вводите только числовые значения.")

main()
