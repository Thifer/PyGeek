"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1

"""


def method_name():
    global i
    for i in range(len(grade)):
        if grade[i] == maxgrade:
            grade[i] = mingrade


count = int(input("Введите число оценок "))
grade = []

for i in range(count):
    grade.append(int(input()))

mingrade = min(grade)
maxgrade = max(grade)

method_name()

print(grade)
