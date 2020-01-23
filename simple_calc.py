# A simple calculator program

# First, we define the methods
def add():
    c = x + y
    print("The sum of the numbers is:", c)
def subtract():
    c = x-y
    print("The difference of the values is:", c)
def multiply():
    c = x*y
    print(x, "x", y, "is:", c)
def divide1():
    c = x/y
    print(x, "divided by", y, "is:", c)
def divide2():
    c = y/x
    print(y, "divided by", x, "is:", c)
def end():
    endd = input("\nDo you want to perform another calculation? (Yes/No): ")
    endd = endd.upper()
    if (endd=="Y") | (endd=="YES"):
        print("\nOk,", name.upper())
        i == 1
    elif (endd == "N") | (endd == "NO"):
        print("\nGoodbye ",name.upper())
        quit()
    else:
        print("Wrong input, please try again\n")
        end()



# Now we begin
name = input("Enter your name: ")
print("\n")
print("Hello", name.upper(), "welcome to this calculator app\n\nHow may I help you?")
print("\n")

i = 1
while (i == 1):
    decision = input("I want to:\n\t> Add(A) \n\t> Subtract(S) \n\t> Multiply(M) \n\t> Divide(D) \n\n(Please type your decision):\t")
    decision = decision.lower()
    if(decision == "add") | (decision == "a"):
        print("\nOK\n")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        add()
        end()
    elif(decision == "subtract") | (decision == "sub") | (decision == "s"):
        print("OK")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        subtract()
        end()
    elif(decision == "multiply") | (decision == "m") | (decision == "mul"):
        print("OK")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        multiply()
        end()
    elif(decision == "divide") | (decision == "div") | (decision == "d"):
        print("OK")
        decision2 = input("(1) X by Y\n(2) Y by X\n(Please enter 1 or 2): ")
        if (decision2 == "1"):
            x = int(input("Enter X: "))
            y = int(input("Enter Y: "))
            divide1()
            end()
        elif (decision2 == "2"):
            x = int(input("Enter X: "))
            y = int(input("Enter Y: "))
            divide2()
            end()
    else: print("Wrong input, please try again\n")



    
