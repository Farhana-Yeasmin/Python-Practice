import itertools

l1 = set(map(int,input().split()))
l2 = set(map(int,input().split()))

res = itertools.product(l1,l2)
new_list = list(res) 
for i in new_list:
    print(i, end=" ")
print("\n")
