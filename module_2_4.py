numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for number in range(2,len(numbers)):
    if number >1:
        for num in range(2,number):
            if number % num == 0:
                not_primes.append(number)
                break
        else:
            primes.append(number)
    else:
        not_primes.append(number)
print(primes)
print(not_primes)
