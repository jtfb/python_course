# ERRORS HOMEWORK 1
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error ocurred")

# ERRORS HOMEWORK 2

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("An error ocurred")
finally:
    print("All done")

# ERRORS HOMEWORK 2

def ask():

    while True:

        try:
            result = int(input("Please provide a number: ")) ** 2
        except:
            print("This is not a number! Try again")
            continue
        else:
            break

    print(f"Thank you, your number squared is: {result}")

ask()