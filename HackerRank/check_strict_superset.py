s = set(map(int,input().split()))
n = int(input())

for i in range(n):
    temp_set = set(map(int,input().split()))
    if s.issuperset(temp_set):
        res = True
    else:
        res = False
        break
print(res)            