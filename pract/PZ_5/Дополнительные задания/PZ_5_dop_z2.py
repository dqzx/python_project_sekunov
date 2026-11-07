# Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в
# функции.

def calc(width, height):
    p = (width + height) * 2
    square = width * height
    return p, square

try:
    wid = float(input("Введи ширину прямоугольника: "))
    heig = float(input("Введи высоту прямоугольника: "))

    if wid <= 0 or heig <=0:
        print("Введите корректное значение: ")

    else:
        per, squ = calc(wid, heig)
        print(f"Периметр равен = {per}")
        print(f"Площадь равна = {squ}")

except ValueError:
    print("произошла ошибка, введите корректное значение")