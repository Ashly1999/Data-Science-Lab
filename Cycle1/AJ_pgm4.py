def __gcd(a, b):

    if (a == 0 or b == 0): return 0


    if (a == b): return a

   
    if (a > b):
        return __gcd(a - b, b)

    return __gcd(a, b - a)
def coprime(a, b):
    if (__gcd(a, b) == 1):
        print("Co-Prime")

a =int(input("enter the first number"))
b =int(input("enter the second number"))
coprime(a, b)
