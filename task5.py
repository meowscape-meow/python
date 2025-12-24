#task 1
m=["круг",0.25,"квадрат","треугольник",15,"круг","овал","10"]

m.remove(0.25)
m.remove(15)
m.remove("10")
print(m)
#task 2
abc=["A","B","C","D","E","F","G"]

del abc[1:-2]
print(abc)
#task  3
numbers=[1,4]

numbers.insert(1,2)
numbers.insert(2,3)
print(numbers)
#task 4
mass=[14,-6,3,11,6,8.5,99,-20,-6,10,40,0.25,-4.5]

mass=[x for x in mass if x>=0]
mass.sort()
print(mass)
mass.sort(reverse=True)
print(mass)
#task 5
numbers_plus = []
numbers_minus = []
numbers_zero = []

n = int(input("Введите количество чисел: "))

for x in range(n):
  num = float(input("Введите числа: "))
  
  if num < 0:
    numbers_minus.append(num)
  elif num > 0:
    numbers_plus.append(num)
  else:
    numbers_zero.append("*")
    
if numbers_minus:
  print(sum(numbers_minus))
else:
    None
  
  
if numbers_plus:
  average_num = sum(numbers_plus) / len(numbers_plus)
  print(average_num)
else:
    None
  
  
print("Количество звезд:", len(numbers_zero), numbers_zero)
