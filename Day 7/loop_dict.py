thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all the KEY'S:
for i in thisdict:
    print("Key's of the dictionary: ",i)

# Another way to print all the KEY'S:
for i in thisdict.keys():
    print(i)

# Print all the value's:
for i in thisdict.values():
    print("Values of the dictionary: ",i)

# Another way to print values:
for i in thisdict:
    print(thisdict[i])

#print key value as a pair
for x,y in thisdict.items():
    print(x,"  ",y)