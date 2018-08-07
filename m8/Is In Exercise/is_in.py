"""# Exercise: Is In
# Write a Python function, isIn(char, aStr),
that takes in two arguments a character and String,
returns the isIn(char, aStr) which retuns a boolean value.
# This function takes in two arguments character and String and returns one boolean value."""

def is_in(char_acter, input_string):
    '''
    char_acter: a single char_acteracter
    input_string: an alphabetized string
    returns: True if char_acter is in input_string; False otherwise
    '''
    length_string = len(input_string)
    length_string = int(length_string)
    if length_string == 0:
        return str(False)
    if char_acter == input_string[length_string//2]:
        return True
    if input_string[length_string//2] > char_acter:
        return is_in(char_acter, input_string[0:length_string//2])
    return is_in(char_acter, input_string[length_string//2:])

def main():
    """Main Function"""
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))

main()
