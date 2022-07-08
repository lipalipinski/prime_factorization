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
    for check in range(2, num//2+1):
        if num % check == 0:
            return False
    return True


def find_prime_factors(num):
    """
    returns a list of prime factors of a given number
    """
    primes = []
    while not is_prime(num):
        for guess in range(2, num//2+1):
            if num % guess == 0:
                primes.append(guess)
                num = int(num / guess)
                break
    primes.append(num)
    return primes


def main():
    print("I'lind all the prime factors of a given number. ")

    number = 0
    while number < 1:
        number = get_number()
        if number < 1:
            print('The number has to be greater than 0')
        elif number == 1:
            print('1 neither prime or complex, it has no prime factors.')
            return True

    primes = find_prime_factors(number)
    primes_set = set(primes)

    if len(primes) == 1:
        print(f'{number} is a prime!')

    if len(primes_set) == 1:
        print(f'The only prime factor of {number} is {primes[0]}')
    else:
        text = f'Prime factors of {number} are'
        for _, pf in enumerate(primes_set):
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
