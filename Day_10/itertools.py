import itertools

# # Function: COUNT()
# counter = itertools.count()
# data = [100,200,300,440,500]

# daily_data = list(zip(itertools.count(),data))
# print(daily_data)
# """
# Output:
# [(0, 100), (1, 200), (2, 300), (3, 440), (4, 500)]
# """
# #  we can initialize from where to start and increase it by 2
# counter = itertools.count(start=2, step=2)

# # Function : CYCLE()
# cycle = itertools.cycle(('On','Off'))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))

# Function : REPEAT()

repeat = itertools.repeat(2, times=3)
 
#  Mapping range to square
# squares = map(pow,range(10), itertools.repeat(2))
# print(list(squares))
#  Star map
"""
Difference between map and starmap is:
=> applies a function to corresponding elements of one or more iterables
=> starmap takes arguments as a list of tuples
"""

# values = [(0,2),(1,2),(2,2)]
# squares = itertools.starmap(pow,values)
# print(list(squares))

# Function : COMBINATION()

letters = ['a','b','c','d']

result = itertools.combinations(letters,2)
result2 = itertools.permutations(letters,2)
# generate all possible combinations of letters includng repeated elements
result3 = itertools.combinations_with_replacement(letters,2)

for item in result:
    print(item)

# Function: Chain()
letters = ['a','b','c','d']
numbers = [0,1,2]

# """
# we can create a list and concate like combined = numbers+leters this. But what if we have million of datas in list then use this chain function
# """
# combind = itertools.chain(letters,numbers)

# for item in combind:
#     print(item)


# FUNCTION: islice()
"""
we may have an iterator that is too large to put into memory to a list to get a certain slice of the iterator
"""
combined = itertools.islice(range(10),1,5,2)
 