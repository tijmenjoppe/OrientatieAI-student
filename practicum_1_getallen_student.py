""" coding=utf-8

Analytical Skills
Practicum 1: getallen

(c) 2019 Hogeschool Utrecht
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)
Tijmen Muller (tijmen.muller@hu.nl)


Naam:
Klas: 
Studentnummer:


Opdracht: werk onderstaande functies uit.

Je kunt je functies met het gegeven raamwerk door het bestand te uit te voeren (of met behulp
van pytest, als je weet hoe dat werkt). Lever je werk in op Canvas als alle tests slagen.

Let op! Je mag voor deze opdracht geen extra modules importeren met 'import'.
"""


def floor(real):
    """ Retourneert het grootste gehele getal (int), dat kleiner dan of gelijk is aan real (float). """
    return


def ceil(real):
    """ Retourneert het kleinste gehele getal (int), groter dan of gelijk aan real (float). """
    return


def div(n):
    """ Retourneert een (natuurlijk) gesorteerde verzameling (list) van delers van n (int).
        Het getal a ∈ N is een deler van n ∈ N, als er een b ∈ N is, zodat a × b = n. """
    divisors = []
    return sorted(divisors)


def is_prime(n):
    """ Return True als n (int) een priemgetal is, anders False.
        Je kunt gebruik maken van de functie 'div(n)' om te bepalen of n een priem is.
        Optioneel: bedenk een efficiënter alternatief. """
    return


def primefactors(n):
    """ Return een (natuurlijk) gesorteerde verzameling (list) van priemfactoren van n (int)
        Return [n] als n een priemgetal is, of wanneer n == 1.
        Tip: maak gebruik van de functie 'is_prime(n)' """
    factors = []
    return sorted(factors)




def primes(num):
    """ Return alle priemgetallen kleiner dan num (int). """
    primes = []
    return primes


def gcd(a, b):
    """ Return de grootste grootste gemene deler , ggd (ofwel greatest common divisor, gcd) (int) van
        natuurlijke getallen a en b (beide int).

        Je hebt twee opties voor deze opgave;
        1.  Je programmeert hier het algoritme van Euclides
            zie: https://nl.wikipedia.org/wiki/Algoritme_van_Euclides
        2.  Je bedenkt zelf een oplossing waarbij je gebruik maakt van de eerder
            geschreven methode div(n) om de gcd te bepalen.
    """
    return




def lcm(a, b):
    """ Return het kleinste gemene veelvoud, kvg (ofwel least common multiple, lcm) (int)
        van natuurlijke getallen a en b (beide int). """
    return


def add_frac(n1, d1, n2, d2):
    """ Retourneer de sommatie van twee breuken als breuk.

        Argumenten:
        n1 -- de teller van de eerste breuk
        d1 -- de noemer van de eerste breuk
        n2 -- de teller van de tweede breuk
        d2 -- de noemer van de tweede breuk

        Retourneert de som *als breuk*, met eerst de teller en dan de noemer van het resultaat (tuple).

        Bijvoorbeeld: 3/4 + 1/6 = 11/12
                 dan: add_frac(3, 4, 1, 6) = (11, 12)
    """
    return 1, 1


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def my_assert_args(function, args, expected_output):
    argstr = str(args).replace(',)', ')')
    assert function(*args) == expected_output, \
        f"Fout: {function.__name__}{argstr} geeft { function(*args)} in plaats van {expected_output}"


def test_floor():
    testcases = [((1.0,),    1),
                 ((1.05,),   1),
                 ((1.95,),   1),
                 ((-1.0,),  -1),
                 ((-1.05,), -2),
                 ((-1.95,), -2)]

    for case in testcases:
        my_assert_args(floor, case[0], case[1])


def test_ceil():
    testcases = [((1.0,),    1),
                 ((1.05,),   2),
                 ((1.95,),   2),
                 ((-1.0,),  -1),
                 ((-1.05,), -1),
                 ((-1.95,), -1)]

    for case in testcases:
        my_assert_args(ceil, case[0], case[1])


def test_div():
    testcases = [ 
        ((1,),   [1]),
        ((2,),   [1, 2]),
        ((3,),   [1, 3]),
        ((4,),   [1, 2, 4]),
        ((8,),   [1, 2, 4, 8]),
        ((12,),  [1, 2, 3, 4, 6, 12]),
        ((19,),  [1, 19]),
        ((25,),  [1, 5, 25]),
        ((929,), [1, 929]),
        ((936,), [1, 2, 3, 4, 6, 8, 9, 12, 13, 18, 24, 26, 36, 39, 52, 72, 78, 104, 117, 156, 234, 312, 468, 936])
    ]

    for case in testcases:
        my_assert_args(div, case[0], sorted(case[1]))


def test_is_prime():
    testcases = [
        ((1,),  False),
        ((2,),  True),
        ((3,),  True),
        ((4,),  False),
        ((5,),  True),
        ((6,),  False),
        ((29,), True)
    ]

    for case in testcases:
        my_assert_args(is_prime, case[0], case[1])


def test_primefactors():
    testcases = [ 
        ((1,),    [1]),
        ((2,),    [2]),
        ((3,),    [3]),
        ((4,),    [2, 2]),
        ((8,),    [2, 2, 2]),
        ((12,),   [2, 2, 3]),
        ((2352,), [2, 2, 2, 2, 3, 7, 7]),
        ((9075,), [3, 5, 5, 11, 11])
    ]

    for case in testcases:
        my_assert_args(primefactors, case[0], sorted(case[1]))


def test_primes():
    testcases = [
        ((1,),  []),
        ((2,),  []),
        ((3,),  [2]),
        ((4,),  [2, 3]),
        ((5,),  [2, 3]),
        ((6,),  [2, 3, 5]),
        ((30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ]

    for case in testcases:
        my_assert_args(primes, case[0], sorted(case[1]))


def test_gcd():
    testcases = [ 
        ((60, 70), 10)
    ]
    
    for case in testcases:
        my_assert_args(gcd, case[0], case[1])


def test_lcm():
    testcases = [ 
        ((15, 27), 135)
    ]

    for case in testcases:
        my_assert_args(lcm, case[0], case[1])


def test_add_frac():
    testcases = [
        ((1, 2, 1, 4), (3, 4)),
        ((3, 4, 1, 6), (11, 12)),
        ((1, 6, 3, 4), (11, 12))
    ]

    for case in testcases:
        my_assert_args(add_frac, case[0], case[1])


if __name__ == '__main__':
    try: 
        print("\x1b[0;32m")

        test_floor()
        print("Je functie floor() werkt goed!")

        test_ceil()
        print("Je functie ceil() werkt goed!")

        test_div()
        print("Je functie div(n) werkt goed!")

        test_is_prime()
        print("Je functie is_prime(n) werkt goed!")

        test_primefactors()
        print("Je functie primefactors(n) werkt goed!")

        test_primes()
        print("Je functie primes() werkt goed!")

        test_gcd()
        print("Je functie gcd(a, b) werkt goed!")

        test_lcm()
        print("Je functie lcm(a, b) werkt goed!")

        test_add_frac()
        print("Je functie add_frac(n1, d1, n2, d2) werkt goed!")

        print("Gefeliciteerd, alles lijkt te werken! Lever je werk nu in op Canvas...")
        
    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))
