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
for i in range(1, tinggi_segitiga_a + 1):
    print("*" * i)
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
for i in range(tinggi_segitiga_b, 0, -1):
    print("*" * i)
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
for i in range(1, tinggi_segitiga_c + 1):
    print(" " * space + "*" * i)
    space -= 1
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
for i in range(tinggi_segitiga_d, 0, -1):
    print(" " * space + "*" * i)
    space += 1
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
for i in range(1, tinggi_segitiga_e + 1):
    print(" " * space  + "*" * star)
    space -= 1
    star += 2
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
for i in range(1, tinggi_segitiga_f + 1):
    print(" " * space  + "*" * star)
    space += 1
    star -= 2