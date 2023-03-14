num = int(input("Введите число "))
n = 0
while 2 ** n < num:
    print(2**n, end=" ")
    n += 1
