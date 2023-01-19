# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way is to append one list element to other's
for x in list1:
    list2.append(x)
print(list2)

# Or using extend() method to add list2 at the end of list1
list1.extend(list2)
print(list1)


