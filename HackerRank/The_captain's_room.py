# n = int(input())
# arr = list(map(int,input().split()))

arr = [1,2,3,2,4]

# find out the max value form the array
max_val = max(arr)
#  Initializing the counter_list size with the maximum number+1 to avoid out of rang issue
counter_list = [0]*(max_val+1)

for val in arr:
    counter_list[val]+=1
    print(counter_list)

for i in range(max_val+1):
    if counter_list[i]==1:
        print(i)