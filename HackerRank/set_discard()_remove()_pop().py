n = int(input())
s = set(map(int,input().split()))
op_num = int(input())

for i in range(0,op_num):
    operation = input()

    if "pop" in operation:
        s.pop()
    if "remove" in operation:
        text,digit = operation.split()
        s.remove(int(digit))
    if "discard" in operation:
        text,digit = operation.split()
        s.discard(int(digit))

print(sum(s))    


