n1 = int(input())
s1 = set(map(int,input().split()))

n2 = int(input())
s2 = set(map(int,input().split()))

dif_set = s1.symmetric_difference(s2)
sorted_set = sorted(dif_set,reverse=False)

for i in sorted_set:
    print(i)
