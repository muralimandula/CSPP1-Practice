print ("Enter varA below,")
varA = input();
print ("Enter varB below,")
varB = input();
if ( type(varA) == str ) or (type(varB) == str ):
    print ("strings involved")
if varA > varB:
    print ("bigger")
if varA == varB:
    print ("equal")
if varA < varB:
    print ("smaller")