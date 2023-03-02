import collections

d =  collections.OrderedDict()
n = int(input())

for i in range(n):
    item, price = input().rsplit(' ',1)
    if item not in d:
        d[item] = int(price)
    else:
        d[item] += int(price)

#  items value used to retrive key value pair from the dict
for k ,v in d.items():
    print(k,v)