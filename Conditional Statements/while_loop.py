# Example 1 - While Loop
x = 1
while x < 10:
    print("The Value of x is :", x)
    x += 1

# Example 2 - While Loop with else
x = 1
while x < 10:
    print("The Value of x is :", x)
    x += 1
else:
    print("Value is greater than x:", x)

# Example 3 - While loop with Break and Continue
x = 1
while x < 10:
    print("The Value of x is :", x)
    x += 1
    if x == 4:
        print("data Found",x)
        break
    else:
        print("Continue....")
        continue
