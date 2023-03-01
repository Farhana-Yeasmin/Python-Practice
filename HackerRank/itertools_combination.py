import itertools 

a = input().split()
t = a[0]
digit = int(a[1])
text = sorted(t)

for i in range(1,digit+1):
    combo = list(itertools.combinations(text, i))
    for j in combo:
        print(''.join(j))