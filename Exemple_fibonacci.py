import scipy
import numpy as np
import time

#Recursive function fibonacci
def fib(n):
    if n >= 40:
        return "n trop grand"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fibMemo(n, memo):
    if n >= 40:
        return "n trop grand"
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]

val = 14

start = time.time()
print(fib(val))
end = time.time();
print(end - start)

start = time.time()
print(fibMemo(val, {}))
end = time.time()
print(end - start)