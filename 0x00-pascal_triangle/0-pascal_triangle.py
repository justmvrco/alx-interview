#!/usr/bin/python3

'''
a function `pascal_triangle(n)` that 
returns a list of lists of integers representing
the Pascal’s triangle of size n
'''

def pascal_triangle(n):
    ''' pascal's triangle '''
    n = n if n and isinstance(n, int) else None
    result = []
    if not n:
        return result
    result = [1]
    y = [0]
    for i in range(n):
        print(result)
        result=[left+right for left,right in zip(result+y, y+result)]
    return result

if __name__ == '__main__':

    pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
