n1 = int(input())
s1 = set(map(int,input().split()))

n2 = int(input())
s2 = set(map(int,input().split()))

dif_set = s1.difference(s2)

print(len(dif_set))
