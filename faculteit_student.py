"""
Analytical Skills
Opgave: faculteit (iteratief)

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Je mag voor deze opgave geen extra modules importeren met 'import'.
"""


def faculteit_iteratief(n):
    """ Berekent n! op iteratieve wijze. """
    res = 1

    # Voeg de iteratie in: for ...

    return res


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import math


def test_faculteit_iteratief():
    for x in range(6):
        assert faculteit_iteratief(x) == math.factorial(x), "Fout: faculteit_iteratief({}) geeft {} in plaats van {}".format(x, faculteit_iteratief(x), math.factorial(x))


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_faculteit_iteratief()
        print("Je functie faculteit_iteratief() doorstaat de tests!")

        print("\x1b[0;30m")

        x = int(input("Geef een getal: "))
        print(str(x) + "! = " + str(faculteit_iteratief(x)))

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(str(ae))