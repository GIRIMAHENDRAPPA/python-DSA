# Day 27 - 20 Pattern Questions - LPU MTech AIML
# All in One Folder - python-placement-60-days/Day27_Patterns/all_patterns.py

n = 5

def pattern01_square():
    print("1. Square Stars")
    for i in range(n):
        print('*' * n)

def pattern02_right_triangle():
    print("\n2. Right Triangle")
    for i in range(1, n+1):
        print('*' * i)

def pattern03_inverted():
    print("\n3. Inverted Right Triangle")
    for i in range(n, 0, -1):
        print('*' * i)

def pattern04_number_triangle():
    print("\n4. Number Triangle 1 to n")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        print()

def pattern05_same_number():
    print("\n5. Same Number Repeat")
    for i in range(1, n+1):
        print(str(i) * i)

def pattern06_pyramid():
    print("\n6. Pyramid Star")
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1))

def pattern07_inverted_pyramid():
    print("\n7. Inverted Pyramid")
    for i in range(n, 0, -1):
        print(' ' * (n-i) + '*' * (2*i-1))

def pattern08_diamond():
    print("\n8. Diamond")
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1))
    for i in range(n-1, 0, -1):
        print(' ' * (n-i) + '*' * (2*i-1))

def pattern09_number_pyramid():
    print("\n9. Number Pyramid")
    for i in range(1, n+1):
        print(' ' * (n-i), end='')
        for j in range(1, i+1):
            print(j, end='')
        for j in range(i-1, 0, -1):
            print(j, end='')
        print()

def pattern10_floyd():
    print("\n10. Floyd's Triangle")
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()

def pattern11_binary():
    print("\n11. Binary Triangle 0/1")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print((i+j) % 2, end='')
        print()

def pattern12_alphabet():
    print("\n12. Alphabet Triangle A, AB, ABC")
    for i in range(1, n+1):
        for j in range(i):
            print(chr(65+j), end='')
        print()

def pattern13_butterfly():
    print("\n13. Butterfly Pattern [MOST ASKED LPU]")
    for i in range(1, n+1):
        print('*'*i + ' '*(2*(n-i)) + '*'*i)
    for i in range(n, 0, -1):
        print('*'*i + ' '*(2*(n-i)) + '*'*i)

def pattern14_hollow_square():
    print("\n14. Hollow Square")
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def pattern15_hollow_pyramid():
    print("\n15. Hollow Pyramid")
    for i in range(1, n+1):
        print(' '*(n-i), end='')
        for j in range(1, 2*i):
            if j==1 or j==2*i-1 or i==n:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def pattern16_mirror_number():
    print("\n16. Mirror Number Pyramid")
    for i in range(1, n+1):
        print(' '*(n-i) + (str(i)+' ')*i)

def pattern17_sandglass():
    print("\n17. Sandglass Pattern")
    for i in range(n, 0, -1):
        print(' '*(n-i) + '*'*(2*i-1))
    for i in range(2, n+1):
        print(' '*(n-i) + '*'*(2*i-1))

def pattern18_zigzag():
    print("\n18. Zigzag Pattern")
    for i in range(1, n+1):
        print(' '*(i-1) + '*')

def pattern19_pascal():
    print("\n19. Pascal's Triangle [ServiceNow Asked]")
    for i in range(n):
        print(' '*(n-i), end='')
        num = 1
        for j in range(i+1):
            print(num, end=' ')
            num = num * (i-j) // (j+1)
        print()

def pattern20_spiral_number():
    print("\n20. Spiral Number Pattern")
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==1 or i==n or j==1 or j==n:
                print('5', end=' ')
            elif i==2 or i==n-1 or j==2 or j==n-1:
                print('4', end=' ')
            else:
                print('3', end=' ')
        print()

# Call all patterns
pattern01_square()
pattern02_right_triangle()
pattern03_inverted()
pattern04_number_triangle()
pattern05_same_number()
pattern06_pyramid()
pattern07_inverted_pyramid()
pattern08_diamond()
pattern09_number_pyramid()
pattern10_floyd()
pattern11_binary()
pattern12_alphabet()
pattern13_butterfly()
pattern14_hollow_square()
pattern15_hollow_pyramid()
pattern16_mirror_number()
pattern17_sandglass()
pattern18_zigzag()
pattern19_pascal()
pattern20_spiral_number()

print("\n--- Day 27 Completed - 20 Patterns Done ---")