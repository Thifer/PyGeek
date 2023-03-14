max = min = int(input("wm=>"))
min_i = 0
max_i = 0
curr_i = 0

for i in range(1, int(input("Введите кол-во арбузов"))):
    wm =int(input("wm=>"))
    if wm < min:
        min = wm
        min_i = i
    if wm > max:
        max = wm
        max_i = i
print(F"Минимальный вес = {min} и он на позиции = {min_i}")
print(F"Максимальный вес = {max} и он на позиции = {max_i}")
