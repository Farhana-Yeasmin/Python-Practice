if __name__ == '__main__':
    n = int(input())
    # multi line input
    arr = set(map(int, input().split()))
    
    arr = list(arr)
    arr.sort(reverse=True)
    print(arr[1])