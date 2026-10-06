# Recursion - A function calling itself
# Factorial, Fibonacci series, Stairs 

def fact(n):
    # Edge case handling
    if n == 0:
        return 1
    return n * fact(n - 1)
     
# n = int(input())
# print(fact(n))
# n = 5
# 5! = 5 x 4 x 3 x 2 x 1
# 5 x 4! => 120 n x (n-1)!
# 4 x 3! = 24
# 3 x 2! = 6
# 2 x 1! = 2
# 1 x 0! = 1

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


# n = 5
# print(fib(n))