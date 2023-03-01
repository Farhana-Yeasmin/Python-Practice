import itertools

text,digit = input().split()

res = itertools.permutations(text,int(digit))
new_list = sorted(list(res))

for i in new_list:
    print("".join(i))