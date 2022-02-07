import random


list_1 = [random.randint(5,30) for i in range(1,11)]
list_2 = [random.randint(5,30) for i in range(1,11)]

print("List 1:", list_1)
print("List 2:", list_2)

# Сформировать третий список, содержащий элементы обоих списков;
print("==Createng 3-rd list with two previous and removing repited values==")

list_3 = list_1 + list_2

print("List 3:", list_3)

# Сформировать третий список, содержащий элементы обоих списков без повторений;

print("===Removing duplicates from 3-rd list===")

list_3 = (list(set(list_1))) + (list(set(list_2)))

print("List 3 without duplicates:", list_3)


# Сформировать третий список, содержащий элементы общие для двух списков;
print("===Createng 3-rd list with duplicated values from two previous===")

# залишив цей варіант щоб було чесно але я його не сильно поняв, якщо зможеш поясмни
list_3 = [i for i in list_1 if i in list_2]

print("List 3 with duplicated values from two previous:", list_3)

# як на мене цей варіант чувака більш зрозуміліший
del list_3
list_3 = list()
for value  in list_1:
    if value in list_2 and value not in list_3:
        list_3.append(value)
print("List 3 with duplicated values from two previous:", list_3)
# у даному варіанті немає повторювань тому цей варіант виграє

# Сформировать третий список, содержащий только уникальные элементы каждого из списков

print("===Createng 3-rd list with unique elements rom two previous===")

list_3 = [i for i in list_1 if i not in list_2] + [i for i in list_2 if i not in list_1]

print("List 3 with unique elements from two previous:", list_3)
# я залишив свою фомулу але мені цікава твоя думка яка краще моя чи та що у чувака

# Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.

print("==Createng 3-rd list with max and min values of two previous==")

list_3 = min(list_1), + min(list_2), + max(list_1), + max(list_2)

print("List 3 with max and min values of two previous:", list_3)
# дивись у мене вони в рандомній послідовності у нього по зростанню, хоча в умові 
# не йшлося про те що їх треба ставити по зростаню, яка твоя думка
# і найголовніше навіщо я тобі це скинув мені цікаво твоя думка є сенс заморачуватися над складними формулами якщо можна це легше зробити