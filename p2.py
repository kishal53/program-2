print("Welcome to the Pattern Generator and Number Analyzer!!")
while True:
    print("Select an Option:")
    print("1. Generate a pattern")
    print("2. analyze range of Numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            i = int(input("Enter your number of rows: "))
            for a in range(0,i):
                for b in range (a+1):
                    print("*", end = " ")
                print()
        case 2:
            total = 0
            c = int(input("Enter your first number: "))
            d = int(input("Enter your second number: "))
            for i in range(c, d+1):
                if (i%2==0):
                    print(i, "is even")
                else:
                    print(i, "is odd")
                total+=i
            print("Sum of all number from", c, "to", d,"is: ", total)
        case 3: 
            print("Exiting the program. Goodbye!!")
            break;
        case _:
            print("Another choice")