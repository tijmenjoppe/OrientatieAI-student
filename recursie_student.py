#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Analytical Skills
Opgave: recursie

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Je mag voor deze opgave geen extra modules importeren met 'import'.
"""


def faculteit(n):
    # Base case
    if n == 0:
        return 1
    # Recursie
    else:
        return faculteit(0)


def exponent(n):
    # Base case

    # Recursie
    return n


def som(lst):
    return 1


def palindroom(woord):
    return False


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import math
import random


def test_faculteit():
    for i in range(6):
        assert faculteit(i) == math.factorial(i), \
            "Fout: faculteit({}) geeft {} in plaats van {}".format(i, faculteit(i), math.factorial(i))


def test_exponent():
    for i in range(10):
        assert exponent(i) == 2**i, \
            "Fout: exponent({}) geeft {} in plaats van {}".format(i, exponent(i), 2**i)


def test_som():
    for i in range(6):
        lst_test = random.sample(range(-10, 11), i)
        assert som(lst_test) == sum(lst_test), \
            "Fout: som({}) geeft {} in plaats van {}".format(lst_test, som(lst_test), sum(lst_test))


def test_palindroom():
    testcases = [
        ("", True),
        ("radar", True),
        ("maandnaam", True),
        ("pollepel", False),
        ("Maandnaam", False)
    ]

    for testcase, res in testcases:
        assert palindroom(testcase) is res, \
            "Fout: palindroom({}) geeft {} in plaats van {}".format(testcase, palindroom(testcase), res)


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_faculteit()
        print("Je functie faculteit() doorstaat de tests!")

        test_exponent()
        print("Je functie exponent() doorstaat de tests!")

        test_som()
        print("Je functie som() doorstaat de tests!")

        test_palindroom()
        print("Je functie palindroom() doorstaat de tests!")

        print("\x1b[0;30m")

        x = input("Geef een woord: ")
        print("'" + x + "' is " + ("" if palindroom(x) else "g") + "een palindroom!")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)
