#create an empty list
my_list = []
#append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#print the list
print(my_list)
#insert the value 15 at the second position in the list
my_list.insert(1, 15)
print(my_list)
#extend the list with another list
my_list.extend([50, 60, 70])
print(my_list)
#remove the last element from the list
my_list.pop()
print(my_list)
#sort the list in ascending order
my_list.sort()
print(my_list)
#find and print the index of the value 30 in the list
index_of_30 = my_list.index (30)
print("index of 30 in the list:", index_of_30)
