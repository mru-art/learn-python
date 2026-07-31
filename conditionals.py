a = 3
if a > 0:
    print("A is a positive number")
# A is a positive number

# if else
a = 3
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")


# if elif else
a = 0
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")


# shorthand
a = 3
(
    print("A is positive") if a > 0 else print("A is negative")
)  # first condition met, 'A is positive' will be printed


# nested conditionals
a = 0
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")


# if & and operators
a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive integer")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")


# if and or operators
user = "James"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied!")
