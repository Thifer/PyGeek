orel = reshka = 0

for _ in range(int((input("кол-во монеток")))):
    if (int(input("0 или 1"))) == 0:
        orel += 1
    else:
        reshka += 1

print(min(orel, reshka))
