#task 1 var 1

num = int(input("Введите целое число "))

if num == 0:
    num =+ 1
    print(num)
elif num >= 1:
    print(num)
else:
    num < 0
    num ** 1
    print(num)

#task 2

your_str = input("Введите строку")
if "." in your_str:
        print(True)
elif "," in your_str:
        print(True)
else:
        print(False)

#task 3

num1 = int(input("Введите первое целое число "))
num2 = int(input("Введите второе целое число "))
numbers = (num1, num2)
if all(n % 3 == 0 for n in numbers):
    print(True)
elif num1 // 3:
    print(True)
elif num2 // 3:
    print(True)
else: 
    print(False)

#task 1 var 2

def stars(num):
    if num > 100:
        print("*")
    elif num >= 0:
        print("*" * num)
    
num = int(input("Введите целое число "))
print(stars(num))

#task 2

str_1 = input("Введите первую строку ")
str_2 = input("Введите вторую строку ")
if str_1 == str_2:
    print(True)
else:
    print(False)

#task 3

r = int(input("Введите первое число: "))
g = int(input("Введите второе число: "))
b = int(input("Введите третье число: "))
if r == g == b == 0:
    print("Черный цвет")
elif r == g == b == 255:
    print("Белый цвет")
elif r == 255 and g == b == 0:
    print("Красный цвет")
elif g == 255 and r == b == 0:
    print("Зеленый цвет")
elif b == 255 and r == g == 0:
    print("Синий цвет")
else:
    print("Нет цвета")

#task 1 var 3

a = int(input("Введите число: "))
if a > 0:
    c = a - 1
    b = a + 1
    print(c, a, b)

elif a <= 0:
    a = 1
    c = a - 1
    b = a + 1
    print(c, a, b)

#task 2 

name_file = input("Введите имя файла: ")

if ".doc" in name_file:
        print(f"{name_file} имеет разрешение Документ word.")
elif ".txt" in name_file:
        print(f"{name_file} имеет разрешение текстовый файл")
elif ".py" in name_file:
        print(f"{name_file} имеет разрешение python.")
else:
        print("Введено неправильное имя файла")

#task 3


a = int(input("Первая сторона: "))
b = int(input("Вторая сторона: "))
c = int(input("Третяя сторона: "))



if a == b == c:
    print("Треугольник равносторонний")
elif a == b or a == c or b == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")

#task 1 var 4


text = 'important information in one line'

a = input("Буква: ")

if a in text:
    print("Буква имеется!")

else:
    print("Нет такой буквы")

#task 2 



a = int(input("сторона первая: "))
b = int(input("сторона вторая: "))


if a != b:
    s = a * b
    print(f"Это прямоугольник, его площадь равна {s}")

elif a == b:
    s = a**2
    print(f"Это квадрат, его площадь равна {s}")

#task 3 
