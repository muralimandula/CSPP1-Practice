"""# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.
# This function takes in one number and returns one number."""
def square(x_num):
    """Square of the number"""
    return x_num**2

def main():
    """Square of the number"""
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))
main()
