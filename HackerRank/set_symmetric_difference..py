n1 = int(input())
s1 = set(map(int,input().split()))

n2 = int(input())
s2 = set(map(int,input().split()))

diff_set = s1.symmetric_difference(s2)
print(len(diff_set))