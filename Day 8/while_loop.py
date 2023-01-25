# print i as long as i is less than 6:
i = 1
# while i < 6:
#     # print(i)
#     i+=1

# print i as long as i is less than 6 without print i=3
while i < 6:
    # print(i)
    if i!= 3:
        print(i)
    i = i+1
# Continue  Statement   
"""
With the continue statement we can stop the current iteration, and continue with the next:
""" 
"""
output:
1
2
4
5
6
"""
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)