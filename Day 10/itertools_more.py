import itertools

#  Function : GROUPBY()

s = input()
group = itertools.groupby(s)

for key, val in group:
    val = list(val)
    print((len(val),int(key)), end=' ')
