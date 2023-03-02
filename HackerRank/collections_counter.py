import collections

n = int(input())
shop = map(int, input().split(" "))

d = collections.Counter(shop)

num = int(input())
total = 0
for i in range(num):
    size,price = map(int,input().split(" "))
    if d[size]:
        total+=price
        d[size]-=1

print(total)
