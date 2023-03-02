import collections

# Function : Chainmap
"""
Chainmap is a dictionary like class for creating a single view of multiple mappings
""" 
A = {1: 'farhana', 2:'python'}
B = {3:'ML',4:'AI'}
m = collections.ChainMap(A,B)
#  accessing values
print(m.values())
# converting it to list
print(list(m.values()))
print(m.keys())
print(m)

"""
A new dictionary can be added by using the new_child() method. It is added at the beginnin of the chainmap
"""
C = {5:'No way'}
new_map = m.new_child(C)
# print(new_map)