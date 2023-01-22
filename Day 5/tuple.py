#A tuple is a collection which is ordered and unchangeable. Also allow duplicate values
# Tuple are writte with round brackets

thistuple = ("apple","banana","cherry")
print(tuple)

# Create tuple with one item but remember the comma
newTuple = ("Apple",)
print(type(newTuple))

#NOT a Tuple
newTuples=("apple")

# It is also possible to use the tuple() constructor to make a tuple
thistuple = tuple(("apple","orange","cherry"))# note the double round brackets

if "apple" in thistuple:
    print("Yes exist")

#CHANGE TUPLE VALUES
"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable or immutable as it is called.
But there is a workaround. You can cinvert the tuple into a list, change the list and convert into a tuple back.
"""
x = ("apple","banana","cherry")
y = list(x) # convert tuple into a list
y[1]= "Kiwi"
x = tuple(y) # convert list into a tuple

print(x)

#ADD ITEMS
"""
Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#print(thistuple)

#ADD TUPLE TO A TUPLE:
"""
You are allowed to add tuples to tuples. so if you want to add one item, create a new tuple with item and add it to the existing tuple
"""

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#REMOVE ITEMS:
"""
You cannot remove items in a tuple. So convert tuple into a list then remove item from it.
"""

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
y.remove("cherry")
thistuple = tuple(y)

print(thistuple)

