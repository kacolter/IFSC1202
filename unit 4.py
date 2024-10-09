def isPrime(number):
    """Returns True if number is prime, otherwise returns False."""
    # Han
    if number < 2:dle special cases:
        return False
    elif number == 2:
        return True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
