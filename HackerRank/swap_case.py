def swap_case(s):
    line = ""
    for i in s:
        if i.isupper():
            line = line+i.lower()
        else:
            line = line + i.upper()


    # just return this 
    # s.swapcase()        
    return line

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)