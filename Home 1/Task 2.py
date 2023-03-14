num = int(input("Введите 3х значное число"))
sum = 0
while num >= 10:
    sum += num % 10
    num //= 10
sum += num
print(sum)