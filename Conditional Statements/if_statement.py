# If statements examples
flag = True

# If statements
if flag:
    print("If statement Works")

# if--else
name = "Python"
if name == "Python":
    print("If statement Works")
else:
    print("Statement Not Works")

# If elif else
policy_status = input("Enter the policy status:-")
if policy_status == "AP":
    print("Collection Eligible")
elif policy_status == "IL" or policy_status == "VL":
    print("Collection Eligible with intrest")
else:
    print("Index Revival Request")

