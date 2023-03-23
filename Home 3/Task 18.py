'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

n = int(input("Введите число элементов "))

numbers = []

for i in range(n):
    numbers.append(i+1)
for i in range(n):
    print(numbers[i], end=" ")
print()

s = int(input("Какое число ищем? "))

num = 0

if s in numbers:
    print(s)
else:
    dif = min(s,numbers[1])-max(s,numbers[1])
    for i in numbers:
        if min(s,i)-max(s,i)>dif:
            dif = min(s,i)-max(s,i)
            num = i
    print(f"=>{num}")