if __name__ == '__main__':
    N = int(input())
    l=[]
    for _ in range(N):
        inp=list(input().split())
        if "insert" in inp:
            l.insert(int(inp[1]),int(inp[2]))
        if "print" in inp:
            print(l)
        if "remove" in inp:
            l.remove(int(inp[1]))
        if "append" in inp:
            l.append(int(inp[1]))
        if "sort" in inp:
            l.sort()
        if "pop" in inp:
            l.pop()
        if "reverse" in inp:
            l.reverse()   