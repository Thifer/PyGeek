#Задача No11. A > 1. Вывести число Фибоначчи если φ(n)==A. Если А не число Фибоначчи, вывеcти -1.

num = int(input("Введите число для поиска"))
fib = [1, 2]
count = 5
if num == 1:
    print(2)
elif num == 2:
    print(4)
else:
    while fib[1] < num:
        fib[0], fib[1] = fib[1], fib[0] + fib[1]
        if num == fib[1]:
            print(count)
            break
        count += 1
    else:
        print(-1)
# number = int(input("Введите число: "))
# f1 = f2 = 1
# n=3 # число больше 1
# while number>f2 :
#     f1, f2 = f2, f1 + f2
#     n +=1
# print(n if number == f2 else '-1')
# number = int(input("Введите число: "))
# f1 = f2 = 1
# n=3 # число больше 1
# while number>f2 :
#     f1, f2 = f2, f1 + f2
#     n +=1
# print(n if number == f2 else '-1')
