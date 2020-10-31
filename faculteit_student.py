#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Opgave: faculteit (iteratief)

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Je mag voor deze opgave geen extra modules importeren met 'import'.
"""


def faculteit_iteratief(n):
    """ Bereken n! op iteratieve wijze. """
    res = 1

    # Voeg de iteratie in: for ...

    return res


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import math


def test_faculteit_iteratief():
    for x in range(6):
        assert faculteit_iteratief(x) == math.factorial(x), \
            f"Fout: faculteit_iteratief({x}) geeft {faculteit_iteratief(x)} in plaats van {math.factorial(x)}"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_faculteit_iteratief()
        print("Je functie faculteit_iteratief() doorstaat de tests!")

        print("\x1b[0;30m")

        getal = int(input("Geef een getal: "))
        print(f"{getal}! = {faculteit_iteratief(getal)}")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)
