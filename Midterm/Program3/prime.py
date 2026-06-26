import time


def current_milli_time():
    return round(time.time() * 1000)


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    # A number x can only have a factor pair (a, b) with a*b == x where
    # min(a, b) <= sqrt(x). So if no divisor up to sqrt(x) is found, x is
    # prime - there is no need to check any divisor beyond that point.
    # We also only need to test odd divisors, since we already ruled out
    # even x above.
    limit = int(x ** 0.5)
    for i in range(3, limit + 1, 2):
        if x % i == 0:
            return False  # Found a factor - stop immediately, no need to keep checking
    return True


rs = 1000
re = 40000

start = current_milli_time()
for i in range(rs, re):
    if is_prime(i):
        print(i, "is prime")
end = current_milli_time()

print((re-rs), "numbers searched in", end-start, "milliseconds")
