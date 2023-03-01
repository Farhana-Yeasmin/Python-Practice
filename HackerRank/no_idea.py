m,n = map(int,input().split())
array = list(map(int,input().split()))
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

cnt=0
for i in array:
    if i in a_list:
        cnt = cnt+1
    elif i in b_list:
        cnt = cnt - 1    
print(cnt)
