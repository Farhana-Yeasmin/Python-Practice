# n = int(input())
# line = tuple(map(int,input().split()))
# print(hash(line))

# if __name__ == '__main__':
#     n = int(input())
#     integer_list = tuple(map(int, input().split()))
#     print(hash(integer_list))

# Create an empty tuple and values to it
n = int( input())
tup = ()
for i in range(n):
    tup = tup + (input(),)
print(tup)
