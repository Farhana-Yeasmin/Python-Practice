age = 36
# txt = "My name is John, I am " + age
# print(txt)  won't work
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

"""
But we can combine strings and numbers by using the format() method!
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))