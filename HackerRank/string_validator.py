if __name__ == '__main__':
    s = input()

    # alnum = False
    # alpha = False
    # digit=False
    # lower = False
    # upper = False

    # for i in s:
    #     if i.isalnum() and not alnum:
    #         alnum =True
    #     if i.isalpha() and not alpha:
    #        alpha=True    
    #     if i.isdigit() and not digit:
    #         digit=True
    #     if i.isupper() and not upper:
    #         upper= True
    #     if i.islower() and not lower:
    #        lower = True

    # print(alnum)
    # print(alpha)
    # print(digit)
    # print(lower)
    # print(upper)      

    # Another approch
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))