# SEGITIGA A
'''
    *
    **
    ***
    ****
    *****
'''

tinggi_segitiga_a = int(input("Masukkan tinggi segitiga A = "))
print("\n")
star = 1
while True:
    print("*" * star)
    star += 1
    if star > tinggi_segitiga_a:
        break
print("\n")

# SEGITIGA B
'''
    *****
    ****
    ***
    **
    *
'''

tinggi_segitiga_b = int(input("Masukkan tinggi segitiga B = "))
print("\n")
star = tinggi_segitiga_b
while True:
    print("*" * star)
    star -= 1
    if star < 1:
        break
print("\n")

# SEGITIGA C
'''
        *
       **
      ***
     ****
    *****
'''

tinggi_segitiga_c = int(input("Masukkan tinggi segitiga C = "))
print("\n")
space = tinggi_segitiga_c - 1
star = 1
while True:
    print(" " * space + "*" * star)
    space -= 1
    star += 1
    if star > tinggi_segitiga_c:
        break
print("\n")

# SEGITIGA D
'''
    *****
     ****
      ***
       **
        *
'''

tinggi_segitiga_d = int(input("Masukkan tinggi segitiga D = "))
print("\n")
space = 0
star = tinggi_segitiga_d
while True:
    print(" " * space + "*" * star)
    space += 1
    star -= 1
    if star < 1:
        break
print("\n")

# SEGITIGA E
'''
        *
       ***
      *****
     *******
    *********
'''

tinggi_segitiga_e = int(input("Masukkan tinggi segitiga E = "))
print("\n")
space = tinggi_segitiga_e - 1
star = 1
while True:
    print(" " * space + "*" * star)
    space -= 1
    star += 2
    if space < 0:
        break
print("\n")

# SEGITIGA F
'''
    *********
     *******
      *****
       ***
        *
'''

tinggi_segitiga_f = int(input("Masukkan tinggi segitiga F = "))
print("\n")
space = 0
star = tinggi_segitiga_f * 2 - 1
while True:
    print(" " * space + "*" * star)
    space += 1
    star -= 2
    if star < 0:
        break