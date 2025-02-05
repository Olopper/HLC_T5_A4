def factorial_it(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
 
print(factorial_it)
factorial_it(5)