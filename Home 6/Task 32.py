arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min = int(input("Введите минимальное значение"))
max = int(input("Введите максимальное значение"))

for i in range(len(arr)):
    if min <= list[i] <= max:
        print(i)