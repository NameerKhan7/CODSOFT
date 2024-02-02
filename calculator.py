print("\t\t\tCalculator app",end="\n")



first = input("Enter first number: ")
second = input("Enter second number: ")
op = input("Enter operator(+,-,/,*,^): ")


if first.isdigit() and second.isdigit():
    if op == '+':
        print(int(first) + int(second))
        

    elif op == '-':
        print(int(first) - int(second))

    elif op == '*':
        print(int(first) * int(second))
    elif op == '/':
        if int(second) != 0:
            print(int(first) / int(second))
        else:
            print("Second number is Zero so cannot be divided")

    elif op =='^':
        print(int(first) ** int(second))
    else:
        print("invalid operator")
else:
    print("one of the the input is not digit")        