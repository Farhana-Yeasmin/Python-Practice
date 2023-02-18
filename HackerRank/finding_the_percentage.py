if __name__ =='__main__':
    n = int(input())
    sttudent_marks= {}
    for _ in range(n):
        # separating the name and numbers
        name, *line = input().split()
        # map the numbers into floting number and convert it into a list for iterating
        scores = list(map(float,line))
        sttudent_marks[name] = scores
    query_name = input()    
    list_value = sttudent_marks[query_name]
    avg_mark = sum(list_value)/ len(list_value)
    # print 2 value after decimal point
    print("{:.2f}".format(avg_mark))