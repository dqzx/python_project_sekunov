# С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий.

def g_line(length):
    print("-" * length)

def v_line():
    print("|", end="")

word = input("Введите слово: ")
size_length = len(word) + 2

g_line(size_length)
v_line()
print(word, end="")
v_line()
print()
g_line(size_length)