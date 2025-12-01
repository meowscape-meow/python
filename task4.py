#task 1

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

#task 4

def stars(num):
    if num > 100:
        print("*")
    elif num >= 0:
        print("*" * num)
    
num = int(input("Введите целое число "))
print(stars(num))

#task 5

str_1 = input("Введите первую строку ")
str_2 = input("Введите вторую строку ")
if str_1 == str_2:
    print(True)
else:
    print(False)
