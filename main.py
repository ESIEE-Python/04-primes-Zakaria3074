"""je suis gay"""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """g"""
    if p<=1:
        return False
    if p==2:
        return True
    if p%2:
        return False
    for d in range(3,int(sqrt(p+1))):
        if p%d==0:
            return False
    return True  
#### Fonction principale

def main():
    """h"""

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
