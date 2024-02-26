# List in Python
# This file contains every basic things of Python list

colors = ['red', 'blue', 'green']
print(colors)
print(colors[0])
print(colors[-1]) #will print green

box = [150, 'toy', 123.58]
print(box)

box.append('marker') #added 'marker' in the box
print(box)

box.extend(['pencil', 'pen', 450, 1088, 656.788]) #added multiple items in the box
print(box)

print(len(box)) #shows the size of the list

box.remove('toy') #removes one element from the list by the item's name
print(box)

del box[5] #removes element or elements by index
print(box)

del box[2:5] #removes elements by setting range of item's index
print(box)

#---------------------------------------------------------------------------------------------------

newList = [150, 458.80, 1550.05, 1088, 880, 998.90, 'cheque', 'nagad', 575, 'bKash', 'rocket']
popped = newList.pop(7) #takes an item from the list
print(popped) #will show the popped item
print(newList) #will show the list without the popped item

#--------------------------------------------------------------------------------------------------

numbers = [1, 5, 3, 4, 2, 9, 8, 6, 7]

numbers.reverse() #reverse the exact list
print(numbers)

numbers.sort() #sorts lower to bigger
print(numbers)

numbers.sort(reverse = True) # sorts bigger to lower
print(numbers)

listA = [1, 2, 3, 4, 5]
listB = ['Apple', 'Orange', 'Banana']
totalList = listA + listB
print(totalList)
