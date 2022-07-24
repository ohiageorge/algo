import functools

def max(arr):
    """ Return maximum number in a given list of integers.
    """
    return functools.reduce(lambda a, b: a > b and a or b, arr)

def min(arr):
    """ Return minimum number in a given list of integers.
    """
    return functools.reduce(lambda a, b: a < b and a or b, arr)


if __name__ == "__main__":
    numbers = [2, 10,11,23, 45, 45, 67, 89, 3, 6, 8]
    print("The maximum number is => ", max(numbers))
    print("The minimum number is => ", min(numbers))
