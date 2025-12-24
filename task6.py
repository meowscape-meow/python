#task 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("matrix:")
for row in matrix:
    print(row)
    
print("\nнечетные числа matrix")
for row in matrix:
    for num in row:
        if num % 2 != 0:
            print(num, end=" ")

print("\n")
count_even = 0
for row in matrix:
    for num in row:
        if num % 2 == 0:
            count_even += 1

print(f"кол-во чётных: {count_even}")

#task 2

matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]

answer_matrix = []
for x in range(len(matrix_1)):
    row = []
    for y in range(len(matrix_1[0])):
        row.append(0)
    answer_matrix.append(row)

for x in range(len(matrix_1)):
    for y in range(len(matrix_1[0])):
        answer_matrix[x][y] = matrix_1[x][y] * matrix_2[x][y]

print(answer_matrix)
print()        

for x in range(len(answer_matrix)):
    row_sum = sum(answer_matrix[x])
    print(f"{answer_matrix[x]} сумма строки: {row_sum}")

#task 3

fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'Lemon'], ['Mango', 'grapes']]
print("Элементы с заглавной буквы:")
for row in fruits:
    for fruit in row:
        if fruit[0].isupper():  
            print(fruit)
    
#task 4

random_elements = [['toy', 'bee', 'cheese', 'ear'], 
                   [False, 'word', '0110110', 10], 
                   ['happiness', '(⅃°口°)⅃ ', 'luck', None], 
                   ['car', '<- code ->', 4.7, True]]

print("Каждый второй элемент из random_elements:")
for list_index, list in enumerate(random_elements):
    for element_index, element in enumerate(list):
        if element_index % 2 == 1:
            print(f"random_elements[{list_index}][{element_index}] = {element}")

#task 5

rows = int(input("Введите количество строк:\n"))

column = int(input("Введите количество столбцов:\n"))

matrix = []

for x in range(rows):
    row = []
    
    for y in range(column):
        num = (input(f"Введите значение элемента [{x}][{y}]:\n"))
        
        row.append(num)
    
    matrix.append(row)


print("\nВаш двумерный массив:")
for row in matrix:
    print(row)
        
