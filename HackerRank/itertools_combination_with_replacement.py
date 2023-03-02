import itertools

text,digit = input().split()

text = sorted(text)
res = itertools.combinations_with_replacement(text,int(digit))
new_list = list(res)
for i in new_list:
    print("".join(i))