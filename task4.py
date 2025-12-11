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
 
# task 3 var 4
input("Как твои дела? ")
def whatsapp(a):
    if a == "плохо" or "не хорошо" or "...":
        print(":(")
    elif a == "хорошо" or "нормально" or "отлично":
        print(":)")
    else:
        print(":/")

a = ("плохо" or "хорошо" or "нормально"or "отлично" or "не хорошо" or "...")
print(whatsapp("плохо"))

# task 1 var 5

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if num1 > num2:
    num1 ** num2
    print(num1)
elif num2 > num1:
    num2 ** num1
    print(num2)
else:
    num1 == num2
    print(num1+num2)

# task 2
n = 5
new_message = "Hello! How are you?"
print(new_message)
answer = input()
if answer.startswith(new_message[:n]):
    print(True)
else:
    print(False)

# task 3

a = int(input("Введите длину первого отрезка "))
b = int(input("Введите длину второго отрезка "))
if a > b:
    print(f"Первый отрезок длинее второго на {a - b}")
elif b > a:
    print(f"Второй отрезок длинее первого на {b - a}")
else:
    print("Отрезки равны")

# task 1 var 6

str = input("Введите строку")
if str[0] == str[-1]:
    print(True)
else:
    print(False)

# task 2

num = int(input("Введите число"))

if num // 2:
    num1 = num ** 2
    print(num1)
elif num // 3:
    num1 = num ** 3
    print(num1)
else:
    num1 = num * 100
    print(num1)
    
# task3

num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
if num1 < 0 and num2 > 0:
    num3 = num1 + 1000
    print(num3, num2)
elif num2 < 0 and num1 > 0:
    num3 = num2 + 1000
    print(num3, num1)
elif num1 < 0 and num2 < 0:
    print(False)
elif num1 > 0 and num2 > 0:
    print(True)

# task 1 var 7

user_str = input("Введите строку: ")
print(user_str and user_str[-1] in "яиею")

# task 2 

side_1 = int(input("Введите первую сторону треугольника"))
side_2 = int(input("Введите вторую сторону треугольника"))
side_3 = int(input("Введите третью сторону треугольника"))
if side_1 + side_2 > side_3:
    print(True)
elif side_1 + side_3 > side_2:
    print(True)
elif  side_2 + side_3 > side_1:
    print(True)
else:
    side_1 <= 0
    print(False)
    side_2 <= 0
    print(False)
    side_3 <= 0
    print(False)
#task 3

# a = int(input("введите число: "))

# if a  - 10 < 0:
#     a %= 10
#     if a == 1:
#         b = a % 3
#     elif a == 2:
#         b = a % 2
#     elif a >= 3:
#         b = a ** 2
# elif a - 10 > 0:
#     if a == 1:
#         b = a % 3
#     elif a == 2:
#         b = a % 2
#     elif a >= 3:
#         b = a ** 2

# print(b)

#var 8 task 1


# a == str(input("Паролл?? "))

# if a == qwerty123:
#     print("False")

# else:
# ((((((((((((((((((



# task 2

# pc_number = 777


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# if a < pc_number < b or b < pc_number < a or pc_number < a < b or pc_number < b < a:
#     print("True")

# else:
#     print("False")


#task 3

lamp_1 = 0
lamp_2 = 0

a = int(input("какую лампочку зажечь?"))

if a == 1:
    lamp_1 = 1
    print("лампочка 1 горит")

elif a == 2:
    lamp_2 = 2
    print("вторая лампочка горит")

else:
    print("обе лампочки не горят")
