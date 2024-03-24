#!/usr/bin/python3
"""
Calculates the minimum number of characters using only Copy All and Paste operations.
"""

def minOperations(n):
    """
    Calculates the fewest number exactly in H characters in the file.
    """

    # If n less 2, it's not possible to achieve
    if n < 2:
        return 0

    # Initial minimum number of operations needed for each i
    min_ops = [0] * (n + 1)

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Initial for the current i to i
        min_ops[i] = i

        # for all possible factors of i and minimum operations
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)

    # Return minimum operations needed for n
    return min_ops[n]

# For TESTING
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))