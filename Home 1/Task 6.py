num = int(input("Введите номер билета"))
sum1 = 0
half1 = num // 1000
sum2 = 0
half2 = num % 1000

while half1 >= 10:
    sum1 += half1 % 10
    half1 //= 10
sum1 += half1

while half2 >= 10:
    sum2 += half2 % 10
    half2 //= 10
sum2 += half2

print("Lucky" if sum1 == sum2 else "Unlucky")
