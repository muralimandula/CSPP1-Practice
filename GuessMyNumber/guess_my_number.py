"""#Guess My Number Exercise"""
LOW_NUM = 0
HIGH_NUM = 100
print("Please think of a number between 0 and 100!")
print("Enter 'y' if guess done, or 'h' if that (number > your guess ) else 'l' ")
USER_GUESS = 'LOW_NUM'
while USER_GUESS != 'y':
    print("Is your secret number ", int((LOW_NUM+HIGH_NUM)//2), "?")
    USER_GUESS = input()
    if USER_GUESS == 'l':
        LOW_NUM = ((LOW_NUM+HIGH_NUM)//2)
    elif USER_GUESS == 'h':
        HIGH_NUM = ((LOW_NUM+HIGH_NUM)//2)
print(USER_GUESS)
