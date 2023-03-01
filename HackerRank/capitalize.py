# Complete the solve function below.
def solve(s):
    l = []
    st = s.split(" ")
    for name in st:
        l.append(name.capitalize())
        final_name = " ".join(l)
    
    return final_name

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
