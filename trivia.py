import functools

def sum(arr):
    return functools.reduce(lambda a, b: a+b, arr)

def exponential(n, p, recursion=False):
    """
    Exponential by while loop
    """

    res = 1
    while p > 0:
        res *= n
        p -= 1
    return res
    
def exponential2(n, p):
    """
    Exponential by recursion
    """
    if n <=1:
        return 1
    return n * exponential(n, p-1)


if __name__ == "__main__":
    numbers = [1,2,3,5]
    print("Sum of the numbers is => ", sum(numbers))

    print("Exponential by while loop => ", exponential(2,10))

    print("Exponential by recursion => ", exponential2(2,10))
