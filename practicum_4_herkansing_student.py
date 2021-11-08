#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 4: herkansing

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = ""
klas = ""
studentnummer = -1

"""
1.  Statistische uitschieters
    Een statistische uitschieter is een meetpunt dat ligt op méér dan anderhalf keer de interkwartielafstand onder Q1
    of méér dan anderhalf keer de interkwartielafstand boven Q3.

    Implementeer een functie outliers(lst) die de uitschieters van lijst lst met gehele getallen bepaald.


2.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme voor een lijst `lst` van natuurlijke getallen:
    1. Bepaal het grootste getal k in de lijst.
    2. Maak een nieuwe lijst van lengte k+1, waarbij elk element in deze tweede lijst begint met de waarde 0.
    3. Tel het aantal voorkomens van elk getal in de originele lijst en sla deze frequentie op in de tweede lijst.
    4. Maak een derde, lege lijst
    5. Voeg elke index van de tweede lijst zo vaak toe aan de derde lijst als zij geteld is in stap 3.
    6. Retourneer de derde lijst: zij is een gesorteerde versie van de originele lijst.

    2a. Handmatig toepassen van stap 3.
        Gegeven is de lijst lst = [ 1, 0, 4, 1 ]. Geef de waardes die de *tweede* lijst aanneemt bij
        álle tussenstappen van stap 3. hierboven.
"""
            # TODO: [geef hier je antwoord]
"""

    2b. Handmatig toepassen van stap 5.
        Geef nu de waardes die de *derde* lijst aanneemt bij álle tussenstappen van stap 5. hierboven.
"""
            # TODO: [geef hier je antwoord]
"""

    2c. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie hieronder genaamd my_sort(lst).

    2d. Best en worst case
        -   Stel, je hebt de lijst met waarden lst = [ 1, 0, 4, 1 ], zoals hierboven. Door hoeveel elementen
            moet je dan stappen in het *hele* algoritme om tot een gesorteerde lijst te komen?
"""
            # TODO: [geef hier je antwoord]
"""

        -   Stel, je hebt de lijst met waarden lst = [ 7, 5, 9 ]. Door hoeveel elementen
            moet je dan stappen in het *hele* algoritme om tot een gesorteerde lijst te komen?
"""
            # TODO: [geef hier je antwoord]
"""

        -   Stel, je hebt de lijst met waarden lst = [ 42, 0 ]. Door hoeveel elementen
            moet je dan stappen in het *hele* algoritme om tot een gesorteerde lijst te komen?
"""
            # TODO: [geef hier je antwoord]
"""

        -   Stel, je hebt de lijst met n waarden (dus len(lst) = n), met daarin als maximum waarde k. Door
            hoeveel elementen moet je dan stappen in het *hele* algoritme om tot een gesorteerde lijst te komen?
"""
            # TODO: [geef hier je antwoord]
"""

        -   Concluderend: wanneer werkt dit algoritme efficiënt? En wanneer niet?
"""
            # TODO: [geef hier je antwoord]
"""


3.  De zeef van Erathosthenes

    De 'zeef van Erathosthenes' is een eeuwenoud algoritme om priemgetallen te bepalen.
    Het algoritme werkt als volgt:

    1. maak een lijst van lengte num met elk element de waarde 'True' (de boolean geeft aan, of de index ervan
       een priemgetal is, en we dus beginnen met de aanname dat alles een priemgetal);
    2. maak het eerste en tweede element (index 0 en 1) 'False' (getallen 0 en 1 zijn per definitie geen priemgetal);
    3. begin bij index i = 0
    4. als het element op index i 'True' is, zet dan alle veelvouden van index i op 'False' (maar i zelf niet!)
    5. verhoog i met 1
    6. ga naar stap 4. als i < num
    7. retourneer alle indexen waarvoor geldt dat de waarde 'True' is

    Zie ook: https://nl.wikipedia.org/wiki/Zeef_van_Eratosthenes

    Implementeer dit algoritme in Python in een functie hieronder genaamd primes(num).

"""


def outliers(lst):
    """
    Bepaal de (statistische) uitschieters van een lijst met getallen.

    Hint: maak gebruik van `q1()` en `q3()` uit het practicum over statistiek.

    Args:
        lst (list): Een (mogelijk ongesorteerde) lijst met gehele getallen.

    Returns:
        list: Een lijst met alle uitschieters van de gegeven getallen.
    """
    outlier_lst = []
    return sorted(outlier_lst)


def my_sort(lst):
    """
    Sorteer gegeven lijst volgens het algoritme zoals beschreven in de pseudocode hierboven.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    sorted_lst = []                     # stap 4.
    return sorted_lst                   # stap 6.


def primes(num):
    """
    Bepaal alle priemgetallen kleiner dan een bepaald geheel getal door middel van 'de zeef van Eratosthenes'.

    Args:
        num (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle priemgetallen kleiner dan `num`.

    .. _Sieve of Eratosthenes:
        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    primes = []
    return primes


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


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


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_outliers():
    testcases = [
        (([10, 10, 10, 10, 12, 12, 12, 12],), []),
        (([0, 10, 10, 10, 10, 12, 12, 12, 12],), [0]),
        (([10, 10, 10, 10, 12, 12, 12, 12, 20],), [20]),
        (([0, 10, 10, 10, 10, 12, 12, 12, 12, 20],), [0, 20]),
        (([0, 0, 10, 10, 10, 10, 12, 12, 12, 12, 20, 20],), [0, 0, 20, 20])
    ]

    for case in testcases:
        __my_assert_args(outliers, case[0], sorted(case[1]))


def test_my_sort():
    lst_test = [random.choice(range(10)) for _ in range(10)]
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def test_primes():
    testcases = [
        ((2,), []),
        ((3,), [2]),
        ((4,), [2, 3]),
        ((5,), [2, 3]),
        ((6,), [2, 3, 5]),
        ((30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ]

    for case in testcases:
        __my_assert_args(primes, case[0], sorted(case[1]))


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_outliers()
        print("Je functie outliers() werkt goed!")

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_primes()
        print("Je functie primes() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
