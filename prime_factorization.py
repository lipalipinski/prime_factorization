"""
prime factorization script
find_prime_factors returns a list of prime factorization
"""

from math import sqrt


def get_number():
    """
    Asks for a number, validates, and returns entered integer.
    """

    while True:
        try:
            num = input("Just give me the number: ")
            num = int(num)
            break
        except ValueError:
            print('This is not a number!')
    return num


def is_prime(num):
    """
    checks if num is a prime number
    """
    if num <= 1:
        return False
    if num % 2 == 0 and num != 2:
        return False
    for check in range(2, int(sqrt(num))+1):
        if num % (check*2-1) == 0:
            return False
    return True


def find_prime_factors(num):
    """
    returns a list of prime factors of a given number
    """
    primes = []
    if num <= 1:
        return primes
# check if divisible by 2
    while num % 2 == 0:
        num = num / 2
        primes.append(2)

# find all remaining prime factors
    for guess in range(2, int(sqrt(num))+1):
        guess = guess * 2 - 1
        if is_prime(guess):
            while num % guess == 0:
                num = num / guess
                primes.append(guess)

    if num != 1:
        primes.append(int(num))
    primes.sort()
    return primes


def main():
    """
    main function
    """

    print("I'lind all the prime factors of a given number. ")

    number = 0
    while number < 1:
        number = get_number()
        if number < 1:
            print('The number has to be greater than 0')
        elif number == 1:
            print('1 is neither prime nor complex, it has no prime factors.')
            return True

    primes = find_prime_factors(number)
    primes_set = set(primes)
    primes_sort = list(primes_set)
    primes_sort.sort()

    if len(primes) == 1:
        print(f'{number} is a prime!')

    if len(primes_set) == 1:
        print(f'The only prime factor of {number} is {primes[0]}')
    else:
        text = f'Prime factors of {number} are'
        for _, pf in enumerate(primes_sort):
            if _ == len(primes_set) - 1:
                text += f' {pf}'
            elif _ == len(primes_set) - 2:
                text += f' {pf} and'
            else:
                text += f' {pf},'
        print(text)

    if len(primes) != 1:
        text = f'{number} ='
        for _, pf in enumerate(primes):
            if _ == len(primes) - 1:
                text += f' {pf}'
            else:
                text = text + f' {pf} x'
        print(text)


if __name__ == '__main__':
    main()
