def fibb(num):
    if num == 0 or num == 1:
        return 1
    return fibb(num-1) + fibb(num-2)


num = int(input("Введите число"))
print(fibb(num))
