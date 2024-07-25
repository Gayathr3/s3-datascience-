def print_non_primes(start, end):
    for num in range(start, end + 1):
        if num > 1: # prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0: # if num is divisible by any number between 2 and num, it's not prime
                    print(num)
                    break
        else:
            print(num) # 0 and 1 are not prime numbers

# test the function
print_non_primes(1, 50)