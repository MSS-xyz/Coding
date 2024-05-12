while True:
    nik = input("Masukkan NIK = ")
    print(f"\nPanjang Digit =  {len(nik)}")
    print(f"Digit Terakhir = {nik[-1]}")
    
    search_digit = input("\nCari Digit Pada NIK = ")
    if (search_digit in nik):
        print(f"\nDigit \"{search_digit}\" ada pada NIK")
    else:
        print(f"\nDigit \"{search_digit}\" tidak ada pada NIK")
    print(f"Jumlah Digit \"{search_digit}\" Pada NIK = {nik.count(search_digit)}")
    
    repeat = input("\nIngin Mengulangi Kembali? (y/n) = ")
    if repeat == "y":
        pass
    elif repeat == "n":
        break
    else:
        print("Invalid Input!!!")
        break