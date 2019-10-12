""" coding=utf-8

Analytical Skills
Practicum 4: algoritmiek

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Naam:
Klas:
Studentnummer:


Opdracht: beantwoord onderstaande vragen en werk onderstaande functies uit.

Je kunt je functies testen met het gegeven raamwerk door het bestand uit te voeren (of met behulp
van pytest, als je weet hoe dat werkt). Lever je werk in op Canvas als alle tests slagen.

Let op! Je mag voor deze opdracht geen extra modules importeren met 'import'.
"""
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

        [antwoord]


    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie genaamd  my_sort(lst).
  
  
    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het snelste klaar (best-case scenario)? Hoeveel vergelijkingen (zoals beschreven 
            in stap 1. van de pseudocode) zijn nodig geweest?
        
        [antwoord]
        
        
        -   Bij welke volgorde van de waarden in de lijst is het sorteeralgoritme het minst snel klaar
            (worst-case scenario)? Hoeveel vergelijkingen zijn nodig geweest?
        
        [antwoord]
        
        
        -   Stel je hebt een lijst met de waarden 1 tot en met 4. Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig? 
            En wat is nu het worst-case scenario? Hoeveel vergelijkingen zijn er nodig?
        
        [antwoord]
                     
                
        -   Stel je hebt een lijst met de waarden 1 tot en met n (je weet nu dus niet precies hoeveel waarden er in de 
            lijst zitten, het zijn er 'n'). Wat is nu het best-case scenario? Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario? Hoeveel vergelijkingen zijn er nodig?

        [antwoord]
            
                
                
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
    Zoekt een element in gegeven lijst door middel van recursief lineair zoeken.

    Argumenten:
    lst -- de lijst waarin gezocht wordt (list)
    target -- het element dat gezocht wordt

    Retourneert of het element in de lijst voorkomt (bool)
    """
    return False


def binary_search_recursive(lst, target):
    """
    Zoekt een element in gegeven lijst door middel van recursief binair zoeken.

    Argumenten:
    lst -- de lijst waarin gezocht wordt (list)
    target -- het element dat gezocht wordt

    Retourneert of het element in de lijst voorkomt (bool)
    """
    return False


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_my_sort():
    lst_test = random.sample(range(-99, 100), 6)
    lst_copy = lst_test.copy()
    my_sort(lst_test)
    assert lst_test == sorted(lst_copy), f"Fout: my_sort({lst_copy}) geeft {lst_test} in plaats van {sorted(lst_copy)}"


def test_linear_search_recursive():
    for i in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        outcome = linear_search_recursive(lst_test, target)
        assert outcome == (target in lst_test), \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {target in lst_test}"


def test_binary_search_recursive():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        outcome = binary_search_recursive(lst_test, target)
        assert outcome == (target in lst_test), \
            f"Fout: binary_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {target in lst_test}"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

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
