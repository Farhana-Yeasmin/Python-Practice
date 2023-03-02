import collections

n = int(input())
total_marks = 0
info = collections.namedtuple('info',input())

for i in range(n):
    ID,MARKS,NAME,CLASS = input().split()
    new_info = info(ID,MARKS,NAME,CLASS)
    val = new_info.MARKS
    total_marks += int(val)
print(f'{total_marks / n:.2f}')

