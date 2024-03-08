#!/usr/bin/python3

def pascal_triangle(n):
    """

    Returns Pascal's triangle up to the nth row.
    
    Args:
        n (int): Number of rows in the Pascal's triangle.
        
    Returns:
        list: List of lists representing Pascal's triangle.
    
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# TO Test this function
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))

