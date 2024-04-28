#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Bonusvraag: Zeef van Eratosthenes

(c) 2023 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)
Peter van den Berg (peter.vandenberg@hu.nl)

Opdracht: werk onderstaande functie uit.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van pytest, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def zeef_van_eratosthenes(getal):
    """
    Vind alle priemgetallen onder een gegeven getal met behulp van de zeef van Eratosthenes
    (zie https://nl.wikipedia.org/wiki/Zeef_van_Eratosthenes).

    Args:
        getal (int): Het gegeven getal.

    Returns:
        list of int: Alle gevonden priemgetallen onder het gegeven getal.
    """
    return []


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


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
    is_float = type(expected_output) is float
    is_float_list = type(expected_output) is list and all([type(item) is float for item in expected_output])
    if is_float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    elif is_float_list:
        # Vergelijk bij floatlijst als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert [round(x - y, 7) for x, y in zip(output, expected_output)] == [0.0] * len(output), msg
    else:
        assert output == expected_output, msg


def test_find_primes():
    testcases = [
        ([10], [2, 3, 5, 7]),
        ([20], [2, 3, 5, 7, 11, 13, 17, 19]),
        ([30], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        ([50], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
        ([100], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
    ]

    for case in testcases:
        __my_assert_args(zeef_van_eratosthenes, case[0], case[1])
    return 1


def __main():
    try:
        print("\x1b[32m")
        test_find_primes()
        print("De functie zeef_van_eratosthenes werkt goed!\n")

    except AssertionError as ae:
        print("\x1b[31m")   # Red text color
        if not ae:
            print("Your code caused the following AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")  # Reset text color


if __name__ == '__main__':
    __main()
