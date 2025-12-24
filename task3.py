#task 1

min = int(input("Введите кол-во минут "))
hour = min // 60
min2 = min % 60 
print(f"{hour} часов {min2} минут")

#task 2

a = 8
b = 11
h = int(input("введите количество часов "))
if h < a:
    print("Недосып")
elif a<=h<=b:
    print("Это нормально")
elif h > b:
    print("Пересып")

#task 3

a = int(input("Введите a "))
b = int(input("Введите b "))
c = int(input("Введите c "))
p = a + b + c 
p2 = p / 2
q1 = p2 - a
q2 = p2 - b
q3 = p2 - c
q = p2 * q1 * q2 * q3
S = q ** 0.5

print(f"Площадь составляет {S} квадратных сантиметров")
 
#task 4 

type = int(input("Выберите форму комнаты: круг(1), квадрат(2), треугольник(3) "))
if type == 1:
    r = int(input("Введите радиус комнаты "))
    r2 = r ** 2
    p = 3.14
    S = p * r2 
    print(f"площадь составляет {S} метров")
elif type == 2:
    a = int(input("Введите сторону комнаты "))
    b = int(input("Введите 2 сторону комнаты "))
    S = a * b
    print(f"Площадь составляет {S} квадратных сантиметров")
elif type == 3:
    a = int(input("Введите сторону 1 "))
    b = int(input("Введите сторону 2 "))
    c = int(input("Введите сторону 3 "))
    p = a + b + c 
    p2 = p / 2
    q1 = p2 - a
    q2 = p2 - b
    q3 = p2 - c
    q = p2 * q1 * q2 * q3
    S = q ** 0.5
    print(f"Площадь составляет {S} квадратных сантиметров")

#task 5


