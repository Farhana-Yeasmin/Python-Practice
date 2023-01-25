def my_newFunc(*val):
    # print(val)
    lst = []
    lst = list(val)
    # print(lst)
    
    size = len(lst)
    i = 0
    while size > 0:
        # i=0
        print(lst[i])
        i = i+1
        size = size - 1

    # for i in range(len(lst)):
    #     print(lst[i])
my_newFunc("Farhana","Yeasmin")  