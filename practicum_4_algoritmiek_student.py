#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Analytical Skills
Practicum 4: algoritmiek

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht: beantwoord onderstaande vragen en werk onderstaande functies uit.

Je kunt je functies testen met het gegeven raamwerk door het bestand uit te voeren (of met behulp
van pytest, als je weet hoe dat werkt). Lever je werk in op Canvas als alle tests slagen.

Let op! Je mag voor deze opdracht geen extra modules importeren met 'import'.
"""

# Vul hier je naam, klas en studentnummer in
naam = ""
klas = ""
studentnummer = -1

"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die de lijst aanneemt bij álle tussenstappen bij 
        toepassing van bovenstaand sorteeralgoritme.

        [geef hier je antwoord]


    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie genaamd  my_sort(lst).
  
  
    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het snelste klaar (best-case scenario)? Hoeveel vergelijkingen (zoals beschreven 
            in stap 1. van de pseudocode) zijn nodig geweest?
        
            [geef hier je antwoord]
        
        
        -   Bij welke volgorde van de waarden in de lijst is het sorteeralgoritme het minst snel klaar
            (worst-case scenario)? Hoeveel vergelijkingen zijn nodig geweest?
        
            [geef hier je antwoord]
        
        
        -   Stel je hebt een lijst met de waarden 1 tot en met 4. Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig? 
            En wat is nu het worst-case scenario? Hoeveel vergelijkingen zijn er nodig?
        
            [geef hier je antwoord]
                     
                
        -   Stel je hebt een lijst met de waarden 1 tot en met n (je weet nu dus niet precies hoeveel waarden er in de 
            lijst zitten, het zijn er 'n'). Wat is nu het best-case scenario? Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario? Hoeveel vergelijkingen zijn er nodig?

            [geef hier je antwoord]
            
                
                
2.  Recursie

    2a. Lineair zoeken
        Implementeer het lineair zoekalgoritme in Python op een *recursieve* manier. Maak hiervoor de functie genaamd 
        linear_search_recursive(lst, target).


    2b. Binair zoeken
        Implementeer het binair zoekalgoritme in Python op een *recursieve* manier. Maak hiervoor de functie genaamd 
        binary_search_recursive(lst, target).
"""


def my_sort(lst):
    """
    Sorteert gegeven lijst lst volgens het algoritme zoals beschreven in de pseudocode bij 1. hierboven.
    De sortering vind 'in place' plaats, met andere woorden: de gegeven lijst lst wordt *zelf* gemuteerd. Er is
    geen return-waarde.
    """
    return None


def linear_search_recursive(lst, target):
    """
    Zoekt een element in gegeven lijst door middel van recursief lineair zoeken. De inhoud van de gegeven lijst
    verandert niet.

    Argumenten:
    lst -- de lijst waarin gezocht wordt (list)
    target -- het element dat gezocht wordt

    Retourneert of het element in de lijst voorkomt (bool)
    """
    return False


def binary_search_recursive(lst, target):
    """
    Zoekt een element in gegeven lijst door middel van recursief binair zoeken. De inhoud van de gegeven lijst
    verandert niet.

    Argumenten:
    lst -- de (reeds gesorteerde) lijst waarin gezocht wordt (list)
    target -- het element dat gezocht wordt

    Retourneert of het element in de lijst voorkomt (bool)
    """
    return False


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_my_sort():
    lst_test = random.sample(range(-99, 100), 6)
    lst_copy = lst_test.copy()
    my_sort(lst_test)
    assert lst_test == sorted(lst_copy), \
        "Fout: my_sort({}) geeft {} in plaats van {}".format(lst_copy, lst_test, sorted(lst_copy))


def test_linear_search_recursive():
    for _ in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = linear_search_recursive(lst_test, target)
        assert outcome == found, \
            "Fout: linear_search_recursive({}, {}) geeft {} in plaats van {}".format(lst_test, target, outcome, found)
        assert lst_copy == lst_test, \
            "Fout: linear_search_recursive(lst, target) verandert de inhoud van lijst lst"


def test_binary_search_recursive():
    for _ in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = binary_search_recursive(lst_test, target)
        assert outcome == found, \
            "Fout: binary_search_recursive({}, {}) geeft {} in plaats van {}".format(lst_test, target, outcome, found)
        assert lst_copy == lst_test, \
            "Fout: binary_search_recursive(lst, target) verandert de inhoud van lijst lst"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        print("Je functie linear_search_recursive() werkt goed!")

        test_binary_search_recursive()
        print("Je functie binary_search_recursive() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken! Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)
