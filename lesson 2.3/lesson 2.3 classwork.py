# list - списки

# val1 = int(input())
# val2 = int(input())
# val3 = int(input())
# val4 = int(input())
# val5 = int(input())

# numbers = [10, 5, 7, 2, 1]

# print(numbers)
# [10, 5, 7, 2, 1]

# numbers = [10, 5, 7, 2, 1]

# print(numbers[3])
# 2

# numbers = [10, 5, 7, 2, 1]

# print(numbers[-1])
# 1    
# якщо ставити "-" то нумерація починається з кінця

# numbers = [10, 5, 7, 2, 1]

# print(numbers)

# numbers[3] = 145

# print(numbers)

# collection

# numbers = [10, 5, 7, 2, 1]

# print(numbers)

# numbers[3] = 145

# print(numbers)

# print(len(numbers))

# from email.headerregistry import Group


from tracemalloc import start
from turtle import end_fill


students = ["John", "Tony", "Sarra", "Mike"]
# # print(students)
# # print(students[3])

# index = len(students)-1
# print(students[index])

# del students[2]

# print(students)
# Mike
# Mike
# ['John', 'Tony', 'Mike']

# Метод - особий від функції
# Функция: y = x^2

# result = function(arg: optional)
# result = data.method(arg: optional)
# result = function(data: required, arg: optional)==method
# ===================
# list.append(value: required)

# # print(students)
# students.append("Marry")
# print(students)
# Group 1
# group_1 = ["Marry", "Sam", "Jack"]
# print("Group 1: ", group_1)

# # # Group 2
# group_2 = ["Don", "Paul", "Bill"]
# print("Group 2:", group_2)

# # print(group_1[0])
# # print(group_2[1])

# group_1.append("Rosa")
# del group_2[1]

# print("Group 1: ", group_1)
# print("Group 2:", group_2)
# Group 1:  ['Marry', 'Sam', 'Jack']
# Group 2: ['Don', 'Paul', 'Bill']
# Marry
# Paul
# Group 1: ['Marry', 'Sam', 'Jack', 'Rosa']
# Group 2: ['Don', 'Bill']

# ===============================
# Insert
# list.insert(lication, value)

# print("Group 1: ", group_1)
# group_1.insert(3, "Mike")
# print("Group 1: ", group_1)


# total = 0    #СУМА
# numbers = [20, 45, 67, 90, 345]
# print(numbers)

# # total = total + numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] 

# # for element in sequence: do
# # # for element in list: do

# for number in numbers:
#     total += number
    
# print("Total =", total)


# for i in range(len(numbers)):
#     print(numbers[i])


# Group 1
# group_1 = ["Marry", "Sam", "Jack"]
# print("Group 1: ", group_1)

# # Group 2
# group_2 = ["Don", "Paul", "Bill"]
# print("Group 2:", group_2)


# group_3 = group_1

# a = 10
# b = a

# print(a)
# print(b)

# a = 20

# del group_1[2]
# print(group_1)
# print(group_3)

# ================================
# import copy

# # Group 1
# group_1 = ["Marry", "Sam", "Jack"]
# print("Group 1: ", group_1)

# # Group 2
# group_2 = ["Don", "Paul", "Bill"]
# print("Group 2:", group_2)


# group_3 = group_1.copy()

# del group_1[2]
# print("Group 1:", group_1)
# print("Group 3:", group_3)

# # elements - списки
# elements = [1, None, "Text", True, 13.2]
# print(elements)
# elements.append("One more text")
# print(elements)
# elements.append([1, True, "String"])
# print(elements)

# # списки можу содержать списки
# print(elements[6])
# print(elements[6] [1])
# 1, None, 'Text', True, 13.2]
# [1, None, 'Text', True, 13.2, 'One more text']
# [1, None, 'Text', True, 13.2, 'One more text', [1, True, 'String']]
# [1, True, 'String']
# True
# ========================

# colors = ["white", "purple", "blue", "yellow", "green"]

# print(colors)

# colors.sort()

# print(colors)
# ['white', 'purple', 'blue', 'yellow', 'green']
# ['blue', 'green', 'purple', 'white', 'yellow']

# ===================================

# Slices срези

# print(students)
# print(students[x:y])
# x -> start
# y -> end

# print(students[0:3])

# print(students[0:3:2])  #добавляємо шаг 2 тільки до середньої цифри

# print(students[:])   # ":" ми нажимаємо тоді коли нам треба з першого по останній елемент
# print(students[::2]) # "::" ми нажимаємо для відображення списку з першого по останній елемент з шагом (треба указувать)
# ['John', 'Tony', 'Sarra', 'Mike']
# ['John', 'Tony', 'Sarra', 'Mike']
# ['John', 'Sarra']
# print(students[::-1])
# 'Mike', 'Sarra', 'Tony', 'John']


# numbers = list(range(1, 100))
# print(numbers[:])   #відображення списка 
# print(numbers[::2])  #відображення нечьотних 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
# 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
# 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 
# 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 
# 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 
# 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
# 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 
# 94, 95, 96, 97, 98, 99]

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 
# 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 
# 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 
# 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# # True, False

# for number in my_list:
# # якщо number = 5 (to_find): виведи мені що я знайшов
# # if variable = value:
# #     ...
# # else:
# #     ...
#     if number == to_find:
#         print("Я найшов цей елемент", number)
#     else:
#         print(number)

# 1
# 2
# 3
# 4
# Я найшов цей елемент 5
# 6
# 7
# 8
# 9
# 10
# ============================

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
finded_index = 0

for index, number in enumerate(my_list):
    if number == to_find:
        print("Я найшов цей елемент", number, "індекс:", index)
        break   # зупинка
    else:
        print(number)
# 1
# 2
# 3
# 4
# Я найшов цей елемент 5 індекс: 4