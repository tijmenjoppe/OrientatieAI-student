#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Bonusvraag: binary search recursief

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht: werk onderstaande functie uit.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van pytest, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def recursive_binary_search(lst, target):
    """
    Zoek een element in de gegeven lijst door middel van recursief binair zoeken.

    Je mag ervan uit gaan dat de gegeven lijst al gesorteerd is.
    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
    """
    return False


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_recursive_binary_search():
    for _ in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = recursive_binary_search(lst_test, target)
        assert outcome == found, \
            f"Fout: recursive_binary_search({lst_test}, {target}) geeft {outcome} in plaats van {found}"
        assert lst_copy == lst_test, "Fout: recursive_binary_search(lst, target) verandert de inhoud van lijst lst"


def __main():
    try:
        print("\x1b[32m")
        test_recursive_binary_search()
        print("Je functie recursive_binary_search werkt goed!\n")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")  # Reset tekstkleur


if __name__ == '__main__':
    __main()
