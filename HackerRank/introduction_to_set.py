def average(array):
    # your code goes here
    total = sum(set(array))
    avg = float(total/len(set(array)))

    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)