def isprime(n):
    if n==0:
        return False
    elif n in (2,3):
        return True
    else:
        for i in range(2,n+1):
            if n%i==0 and i!=n:
                return False
        return True

def primes_yield(n=1):
    while True:
        if isprime(n): yield n
        n = n + 1


if __name__ == '__main__':
    n=0
    primes = []
    while(True):
        if isprime(n): primes.append(n)
        if n >100: break
        n+=1
    print(primes)

    # Using yield generator
    using_yield = []
    for i in primes_yield():
        if i > 150: break
        using_yield.append(i)
    print(using_yield)
