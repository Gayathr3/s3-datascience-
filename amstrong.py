def is_armstrong(n):
    return n == sum(int(digit)**len(str(n)) for digit in str(n))

armstrong_numbers = [i for i in range(1, 1001) if is_armstrong(i)]

print("Armstrong numbers up to 1000:")
print(armstrong_numbers)