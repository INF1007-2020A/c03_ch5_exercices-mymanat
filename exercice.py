#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nombre= input("quel est le chiffre choisi:")
    return abs(float(nombre))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    for i in range(len(prefixes)):
        n=prefixes[i]+suffixes

    return ["n"]


def prime_integer_summation() -> int:
    somme=0
    while premier<=100:
        for n in range(2, num):
            for i in range(2, n-1, 1):
                if n%i!=0:
                    premier+=1
                    somme+=n[i]
    return somme


def factorial(number: int) -> int:
    if number<=1:
        number=1
    else:
        number*=factorial(number-1)
        

    return number


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
