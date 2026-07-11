def star_pyramid(n, i=1):
    if i > n:
        return
    print(" " * (n - i) + "*" * (2 * i - 1))
    star_pyramid(n, i + 1)

# Recursive function for Hollow Pyramid
def hollow_pyramid(n, i=1):
    if i > n:
        return
    if i == 1 or i == n:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print(" " * (n - i) + "" + " " * (2 * i - 3) + "")
    hollow_pyramid(n, i + 1)

# Recursive function for Diamond Pattern
def diamond(n):
    def upper_half(i):
        if i > n:
            return
        print(" " * (n - i) + "*" * (2 * i - 1))
        upper_half(i + 1)
    
    def lower_half(i):
        if i < 1:
            return
        print(" " * (n - i) + "*" * (2 * i - 1))
        lower_half(i - 1)
    
    upper_half(1)
    lower_half(n - 1)

# Recursive function for Number Triangle
def number_triangle(n, i=1):
    if i > n:
        return
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    number_triangle(n, i + 1)

# Recursive function for Alphabet Triangle
def print_chars(ch, count):
    if count == 0:
        return
    print(chr(ch), end=" ")
    print_chars(ch + 1, count - 1)

def alphabet_triangle(n, i=1, ch=65): # 65 = 'A'
    if i > n:
        return
    print(" " * (n - i), end="")
    print_chars(ch, i)
    print()
    alphabet_triangle(n, i + 1, ch)

# Main Menu
levels = 5

print("Star Pyramid:")
star_pyramid(levels)

print("\nHollow Pyramid:")
hollow_pyramid(levels)

print("\nDiamond using Stars:")
diamond(levels)

print("\nNumber Triangle:")
number_triangle(levels)

print("\nAlphabet Triangle:")
alphabet_triangle(levels)
