a = 33
b = 330
if a>b:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")     

# AND:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The pass Statement:
"""
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
"""
if b > a:
   pass