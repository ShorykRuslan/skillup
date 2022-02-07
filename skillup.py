from random import randint

list_1 = list()
list_2 = list()
#================================Creating two lists with randint()================================
for value in range(1, 11):
    list_1.append(randint(1, 50))
    list_2.append(randint(1, 50))
print(f"1-st list:{list_1} Length:{len(list_1)}\n")
print(f"2-nd list:{list_2} Length:{len(list_2)}\n")
#================Creating 3-rd list with two previous and removing repeated values================
print("=======Createng 3-rd list with two previous and removing repited values=======")
list_3 = list_1 + list_2
print(f"3-rd list with duplicates:{sorted(list_3)} Length:{len(list_3)}\n")