#  A lambda function can take any number of arguments, but can only have one expression.
#  lambda arguments : expression

x = lambda a : a+10
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))

def myfunc(n):
    return lambda a : a * n
val = myfunc(3)

print(val(2))