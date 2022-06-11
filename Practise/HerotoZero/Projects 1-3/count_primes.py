"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25

"""

def count_primes(num):
    prime = []
    for x in range(2, num+1):
        #print(x)
        for y in range(2, x):
            if (x % y) == 0:
                break
        else:
            print(prime)
            prime.append(x)

    return (len(prime))

print(count_primes(100))