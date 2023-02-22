# List are used to store multiple iteam in a single variable. It created with square bracket
# If you added anew items to a list, the new items will be placed at the end of the list.
# List is a collection which is ordered and changeable. Allows duplicate members.

myList = ["Apple", "Mango","Banana"]
print(myList)

# List allow duplicare values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))

"""
Other way to create a list:
It is also possible to use the list() constructor when creating a new list.
Note the double round-brackets
"""
myList = list(("Farhana","Yeasmin"))
print(myList)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1])
print(thislist[2:5]) # start at index 2 and end at index 5(not included)
print(thislist[:4])

# Change list items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# INSERT ITEMS TO A LIST:
"""
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
"""
thislist.insert(2,"Farhana")
print(thislist)

# ADD LIST ITEMS:
"""
Using the append() method to append an item at the end
"""
thislist.append("yeasmin")
print(thislist)

#EXTEND LIST:
"""
TO append elements from another list to the current list, use the extend() method.
"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # "tropical" list will added at the end of the "thislist"
print(thislist)

#REMOVE ITEMS FROM A LIST:
"""
remove specified index: the POP() method removes the secified index. If you don't specify the index, the POP() method will remove the last item
"""
thislist.remove("apple")
thislist.pop(1) # remove 1 number index item from the list
thislist.pop() # remove last item from the list
print(thislist)

"""
del keyword also removes the specified index
"""
# del thislist[0]

# LOOP ON LIST:
# for x in thislist:
#     print(x)
"""
The iterable created in the example above is [0, 1, 2]
"""

for x in range(len(thislist)):
    print(thislist[x])



