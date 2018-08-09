"""#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given 
testList = [1, -4, 8, -9] into [1, 4, 8, 9]"""
def apply_to_each(L, f):
    for [j, _] in enumerate(L):
        L[j] = f(L[j])
    return L
       

def main():
    data = input()
    data = data.split()
    L = []
    for j in data:
        L.append(int(j))
    apply_to_each(L, abs)
    print(apply_to_each(L,abs))

if __name__ == "__main__":
    main()
