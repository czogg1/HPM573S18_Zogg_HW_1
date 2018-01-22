
#Problem 3: Iterative and Recursive Operations (Weight 4). Write an iterative function and a recursive
#function that computes the sum of all numbers from 1 to n, where n is given as parameter. Test both
#functions for n = 100.

def iteration(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print(iteration(100))

def recursion(n):
    if n == 1:
        return 1
    else:
        return n+recursion(n-1)

print(recursion(100))

