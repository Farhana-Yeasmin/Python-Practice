"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# It is also possible to use the dict() constructor to make a dictionary.

# thisdict = dict(name = "John", age = 36, country = "Norway")

x = thisdict.get("model")
x = thisdict.keys() # print all the keys of dictionary
x = thisdict.values() # print all the values of dict
x = thisdict.items() # The items() method will return each item in a dictionary, as tuples in a list.



print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:

thisdict ["Color"] = "White"          
print(thisdict)


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
