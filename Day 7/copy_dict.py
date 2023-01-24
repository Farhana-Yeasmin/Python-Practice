#  Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()

#  Using dict() method:
mydict = dict(thisdict)
print(mydict)