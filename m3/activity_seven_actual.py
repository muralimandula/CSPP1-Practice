"""DD"""
ITERATION = 0
COUNT = 0
while ITERATION < 5:
    for letter in "hello, world":
        COUNT += 1
    print("ITERATION " + str(ITERATION) + "; COUNT is: " + str(COUNT))
    ITERATION += 1