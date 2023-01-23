# A set is a collection which is unordered, unchangeable*, and unindexed.
#Duplicates Not Allowed

thisset = {"apple", "banana", "cherry"}
print(thisset)


#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#ACCESS VALUES IN SET
for x in thisset:
  print(x)

# ADD Values:
thisset.add("Water Millon")
# print(thisset)

# To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

# UPDATE() methods can iterate any
"""
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
"""
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# REMOVE ITEM FROM SET:
"""
To remove an item in a set, use the remove(), or the discard() method.
"""
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
thisset.discard("apple")
print(thisset)