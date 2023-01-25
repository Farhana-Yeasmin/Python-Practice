def my_functions():
    return 1+2

print(my_functions())

#Arguments Pass:

def my_func(first_name, last_name):
    print(first_name,last_name)

my_func("Farhana","Yeasmin")

# Arbitrary Arguments, *args:
"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
"""  

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
"""
You can also send arguments with the key = value syntax.
"""
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
"""
If the number of keyword arguments is unknown, add a double ** before the parameter name:
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Passing a List as an Argument

def newFunc(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
newFunc(fruits)