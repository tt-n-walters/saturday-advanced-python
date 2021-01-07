# Recursion, or a recursive function, is a function that calls itself.
import sys

sys.setrecursionlimit(10000)
counter = 0
cache = {}

fib = int(input("What number in the Fibonacci sequence do you want to calculate?\n"))


def fibonacci(n):
    global counter
    # print("Calculating:", n)
    if n in cache:
        return cache[n]
    counter += 1
    if n == 1 or n == 2:
        # print("Anchor point")
        return 1
    temp = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = temp
    return temp


print(fibonacci(fib))
print("Run", counter, "times.")

# print(cache)
# for items in cache.items():
#     print(items)
# print(cache.items())
# for x in cache.items():
#     print(x)

# Recursive explosive problem
# The solution is "cache"