count = 0
currmax = 0
maxdays = 0

for i in range(int(input("Введите кол-во дней"))):
    if int(input("Введите кол-во дней")) > 0:
        currmax += 1
        if maxdays < currmax:
            maxdays = currmax
    else:
        currmax = 0

print(currmax)
