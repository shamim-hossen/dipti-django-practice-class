# Example usage:
# square_pattern(5)
def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()


# Example usage:
# triangle_pattern(5)
def triangle_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()



# Example usage:
# right_triangle_pattern(5)
def right_triangle_pattern(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("* ", end="")
            else:
                print(" ", end="")
        print()



# Example usage:
# pyramid_pattern(5)
def pyramid_pattern(n):
    for i in range(n):
        print(" " * (n-i-1) + "* " * (i+1))














