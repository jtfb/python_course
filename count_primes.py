def count_primes(num):
    result = 0

    for 2 in num:
        if num%2 != 0 and num%3 != 0 and num%5 != 0 and num%7 != 0:
            result = result + 1

    print(result)

# check
count_primes(100)