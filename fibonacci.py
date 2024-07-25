def print_fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    print(fib[:n])
n = int(input("Enter the number of Fibonacci numbers to print: "))
print_fibonacci(n)
