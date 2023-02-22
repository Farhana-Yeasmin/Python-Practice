print("1 Addition")
print("2 Subtraction")
print("3 Multiplition")
print("4 Division")
print("5 Square root")
print("Press 0 to quite the program:\n")


while True:
    print("Press a number to perform the operation:")
    num = int(input())
    if num == 0:
        break
    print("Input number a:")
    a = int(input())
    print("Input number b:")
    b = int( input())
    match num:
        case 1:
            print("Adding two number",a+b)
        case 2:
            print("Subtract two number",a-b)
        case 3:
            print("Multiply two number",a*b)
        case 4:
            print("Dividing two number",a/b)
        case 5:
            print("Square root of first number",a**0.5)     
                    