import functools

def max(arr):
    """ Given a list of integers, find the maximum number
    """
    return functools.reduce(lambda a, b: a > b and a or b, arr)

def min(arr):
    """ Given a list of integers, find the minumum number
    """
    return functools.reduce(lambda a, b: a < b and a or b, arr)


if __name__ == "__main__":
    numbers = [2, 10,11,23, 45, 45, 67, 89, 3, 6, 8]
    print("The maximum number is => ", max(numbers))
    print("The minimum number is => ", min(numbers))
