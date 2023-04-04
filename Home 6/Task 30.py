start_num = int(input("Введите первое число"))
delta = int(input("Введите дельту"))
count = int(input("Введите кол-во элементов"))
arr = []

for i in range(count):
    arr.append(start_num)
    start_num += delta

print(arr)