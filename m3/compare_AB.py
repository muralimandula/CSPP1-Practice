"""Doc This is just a practice program"""
print("Enter varA below,")
VARA = input()
print("Enter varB below,")
VARB = input()
if(isinstance(VARA) == str) or (isinstance(VARB) == str):
    print("strings involved")
if VARA > VARB:
    print("bigger")
if VARA == VARB:
    print("equal")
if VARA < VARB:
    print("smaller")
