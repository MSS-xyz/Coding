contact = ["Ahmad Daniel", "Aisyah Echa", "Bang Fadli",
          "Bang Misba", "Bu Ismirawaty", "Cikila",
          "Denil", "Fendi", "Ghaida Basyra",
          "Hafis Khalik", "Herwind", "Ismansyah",
          "Jumisrang", "Kak Titi", "Mukhlisah",
          "Nida", "Putri", "Rasman",
          "Selvi Febrianti", "Ummul Qurnia", "Yusniar"
]

while True:
    print("-" * 50 + "\n")
    print("\t\t1. Cek Kontak")
    print("\t\t2. Tambah Kontak")
    print("\t\t3. Hapus Kontak")
    print("\n" + "-" * 50 + "\n")
    
    choose = int(input("\t\tPilih (1, 2, 3) = "))
    print("\n")
    
    if choose == 1:
        order = 1
        print("Daftar Kontak :\n")
        for i in contact:
            print(f"{order}. {i}")
            order += 1
        print("\n")
    elif choose == 2:
        new_contact = input("Masukkan nama kontak = ")
        contact.append(new_contact)
    elif choose == 3:
        delete_contact = input("Masukkan nama kontak = ")
        contact.remove(delete_contact)
    else:
        break