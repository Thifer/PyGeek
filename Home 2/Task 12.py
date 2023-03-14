X = Y = 0
S = int(input("Введите чему равна сумма чисел"))
P = int(input("Введите чему равно произведение чисел"))

while X <= 1000:
    while Y <= 1000:
        if X + Y == S and X * Y == P:
            break
        else:
            Y += 1
    if X + Y == S and X * Y == P:
        break
    X += 1
    Y = 0

print(X, Y)
