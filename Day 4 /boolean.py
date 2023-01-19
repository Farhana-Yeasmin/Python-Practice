a = 100
b = 25
if a > b :
    print("a is greater than b")
else:
    print("a is not greater than b")  



"""
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction():
    return True

if myFunction():
    print("YES")
else:
    print("NO") 


# Check if an object is an integer or not
x= 100
print(isinstance(x,int))   