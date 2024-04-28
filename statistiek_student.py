#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: statistiek

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)

Werk onderstaande functies uit. Elke functie krijgt een niet-lege en
ongesorteerde lijst *lst* met gehele getallen (int) als argument.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def median(lst):
    """
    Bepaal de mediaan van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De mediaan van de gegeven getallen.
    """
    return




def rnge(lst):
    """
    Bepaal het bereik van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        int: Het bereik van de gegeven getallen.
    """
    return


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import os


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_rnge():
    testcases = [
        (([4, 2, 5, 8, 6],), 6),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 5)
    ]

    for case in testcases:
        __my_assert_args(rnge, case[0], case[1])


def test_median():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 4, 6, 4, 2],), 3.5),
        (([1, 3, 4, 6, 2, 4, 2],), 3.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.5)
    ]

    for case in testcases:
        __my_assert_args(median, case[0], case[1])


def test_median_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(median, (lst_test,), statistics.median(lst_test), False)


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur

        test_median()
        test_median_simulated()
        print("Je functie median(lst) werkt goed!")

        test_rnge()
        print("Je functie rnge(lst) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
