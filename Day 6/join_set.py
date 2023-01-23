"""
The union() method returns a new set with all items from both sets:
"""

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
# Both union() and update() will exclude any duplicate items.

set1.update(set2)
print(set1)


# Keep ONLY the Duplicates
"""
The intersection_update() method will keep only the items that are present in both sets.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


"""
The intersection() method will return a new set, that only contains the items that are present in both sets.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


#Keep All, But NOT the Duplicates
"""
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

"""
The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
"""
z = x.symmetric_difference(y)
