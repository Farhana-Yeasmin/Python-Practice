import collections
# Function:
"""

"""
a = [1,1,2,3,3,3,4]
c = collections.Counter(a)
print(c)
#  will get the elements of the counter
print(list(c.elements()))

# adding element to the ocunter
c.update([1,2,4])


print(c.most_common())