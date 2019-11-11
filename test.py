def primefactors(n):
    """ Return een (natuurlijk) gesorteerde verzameling (list) van priemfactoren van n (int)
        Return [n] als n een priemgetal is, of wanneer n == 1.
        Tip: maak gebruik van de functie 'is_prime(n)' """
    sqrt = n**(1/2.0)
    factors = []
    if n == 1:
        factors.append(1)
    while n % 2 == 0: 
        factors.append(2), 
        n = n / 2
    for i in range(3,int(sqrt)+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            factors.append(i), 
            n = n / i
    if n > 2: 
        factors.append(n)
    
    
    return sorted(factors)

print(primefactors(1))