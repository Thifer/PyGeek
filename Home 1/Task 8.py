height = int(input("Введите высоту шоколадки"))
weight = int(input("Ведите ширину шоколадки"))
num = int(input("Сколько долек нужно получить"))

if (height * weight) % num == 0 or num % height == 0 or num % weight == 0:
    print("это возможно")
else:
    print("это невозможно")
