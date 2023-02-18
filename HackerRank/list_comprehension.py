if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    # n = int(input())
    
    list_matrix = []
    
    for i in range(0,x):
        for j in range(0,y):
            for k in range(0,z):
                list_matrix = [i,j,k]
    
    print(list_matrix)            