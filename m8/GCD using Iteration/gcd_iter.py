"""# Exercise: GCDIter
# Write a Python function, gcdIter(a, b),
that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number."""
def gcd_iteration(a_val, b_val):
    '''   a, b: positive integers
        returns: a positive integer, the greatest common divisor of a & b.'''
    gcd = 1
    i = 1
    if a_val < b_val:
        large = a_val
    elif b_val < a_val:
        large = b_val
    else:
        large = a_val
    while i <= large:
        if a_val%i == 0:
            if b_val%i == 0:
                if i > gcd:
                    gcd = i
        i += 1
    return gcd

def main():
    '''Main Function'''
    data = input()
    data = data.split()
    print(gcd_iteration(int(data[0]), int(data[1])))
main()
