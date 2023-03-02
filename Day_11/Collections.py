import collections

# Function: nametuple()
a = collections.namedtuple('courses',['name','code','description'])
s = a('Python','PY101','Learn from the scratch')
print(s)

# Impliment a list using namedtuple():
a = collections.namedtuple('course',['name','code','description'])
l = a._make(['Python','PY102','Learn from the scratch'])
print(l)

#  Function: deque()
a = ['a','b','c']
d  = collections.deque(a)
d.append('farhana') # it will insert the value at the end
print(d)

d.appendleft('yeasmin') # add the value to the left side
d.pop() # remove the element fro the end
d.popleft() # remove the element from the left
print(d)
