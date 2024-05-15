#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: recursie

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def faculteit_iteratief(n):
    """ Bereken n! op iteratieve wijze. """
    res = 1

    # Voeg de iteratie in: for ...

    return res


def faculteit(n):
    """ Bereken n! op recursieve wijze. """
    # Base case
    if n == 0:
        return 1
    # Recursie
    else:
        return faculteit(0)


def exponent(n):
    """ Bereken 2^n op recursieve wijze. """
    # Base case

    # Recursie
    return n


def som(lst):
    """ Bereken de som van alle elementen van gegeven lijst `lst` op recursieve wijze. """
    return 1


def palindroom(woord):
    """
    Bepaal of gegeven woord een palindroom (spiegelwoord) is op recursieve wijze.

    Args:
        woord (str): Een woord.

    Returns:
        bool: Of gegeven woord een palindroom is.

    Examples:
        >> palindroom("raar")
        True

        >> palindroom("maandnaam")
        True

        >> palindroom("lekker")
        False
    """
    return False


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import math
import random


def test_faculteit_iteratief():
    for i in range(6):
        assert faculteit_iteratief(i) == math.factorial(i), \
            f"Fout: faculteit_iteratief({i}) geeft {faculteit_iteratief(i)} in plaats van {math.factorial(i)}"


def test_faculteit():
    for i in range(6):
        assert faculteit(i) == math.factorial(i), \
            f"Fout: faculteit({i}) geeft {faculteit(i)} in plaats van {math.factorial(i)}"


def test_exponent():
    for i in range(10):
        assert exponent(i) == 2**i, \
            f"Fout: exponent({i}) geeft {exponent(i)} in plaats van {2**i}"


def test_som():
    for i in range(6):
        lst_test = random.sample(range(-10, 11), i)
        assert som(lst_test) == sum(lst_test), \
            f"Fout: som({lst_test}) geeft {som(lst_test),} in plaats van {sum(lst_test)}"


def test_palindroom():
    testcases = [
        ("", True),
        ("raar", True),
        ("maandnaam", True),
        ("lekker", False),
        ("radar", True),
        ("pollepel", False),
        ("Maandnaam", False)
    ]

    for testcase, res in testcases:
        assert palindroom(testcase) is res, \
            f"Fout: palindroom({testcase}) geeft {palindroom(testcase)} in plaats van {res}"


if __name__ == '__main__':
    try:
        print("\x1b[32m")

        test_faculteit_iteratief()
        print("Je functie faculteit_iteratief() doorstaat de tests!")

        test_faculteit()
        print("Je functie faculteit() doorstaat de tests!")

        test_exponent()
        print("Je functie exponent() doorstaat de tests!")

        test_som()
        print("Je functie som() doorstaat de tests!")

        test_palindroom()
        print("Je functie palindroom() doorstaat de tests!")

        print("\x1b[0m")

        woord = input("Geef een woord: ")
        print(f"'{woord}' is {'' if palindroom(woord) else 'g'}een palindroom!")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur
