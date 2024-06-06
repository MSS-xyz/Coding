import os
from os.path import isfile
from time import sleep

os.system("clear")

def file_manager():
    screen_width = os.get_terminal_size().columns

    all_files = []
    files = os.listdir()
    for file in files:
        if isfile(file):
            all_files.append(file)
    all_files.sort()
    
    while True:
        print("-" * screen_width)
        print(f"{'PENGELOLA FILE':^{screen_width}}")
        print("\n\t\t1. Tampilkan semua file")
        print("\t\t2. Buka file")
        print("\t\t3. Buat file baru")
        print("\t\t4. Hapus file\n")
        print("-" * screen_width)
        
        user = int(input("\nSilahkan pilih (1, 2, 3, 4) : "))
        
        if user == 1:
            print("\n" + "-" * screen_width)
            print(f"{'SEMUA FILE':^{screen_width}}\n")
            order = 1
            for file in all_files:
                print(f"{order}. {file}")
                order += 1
            print("\n" + "-" * screen_width)
        elif user == 2:
            print("\n" + "-" * screen_width)
            print(f"{'BUKA FILE':^{screen_width}}\n")
            order = 1
            for file in all_files:
                print(f"{order}. {file}")
                order += 1
            print("\n" + "-" * screen_width)
            
            open_file = input("\nMasukkan nomor urut atau nama file : ")
            
            if open_file.isdigit():
                if int(open_file) > len(all_files):
                    print("\nFile tidak ditemukan!")
                else:
                    os.system("clear")
                    with open(all_files[int(open_file) - 1], mode = "r") as file:
                        print("\n" + "-" * screen_width)
                        print(f"{all_files[int(open_file) - 1]:^{screen_width}}\n\n")
                        print(file.read())
                        print("\n" + "-" * screen_width)
            else:
                name_file = open_file.lower()
                if name_file in all_files:
                    os.system("clear")
                    with open(open_file, mode = "r") as file:
                        print("\n" + "-" * screen_width)
                        print(f"{name_file:^{screen_width}}\n\n")
                        print(file.read())
                        print("\n" + "-" * screen_width)
                else:
                    print("\nFile tidak ditemukan!")
        elif user == 3:
            new_file = input("\nMasukkan nama file baru : ")
            print("\nPlease wait...")
            sleep(2)
            with open(new_file, mode = "w", encoding = "UTF-8") as file:
                print(f"\nFile {new_file} berhasil dibuat.")
                all_files.append(new_file)
            
        elif user == 4:
            print("\n" + "-" * screen_width)
            print(f"{'HAPUS FILE':^{screen_width}}\n")
            order = 1
            for file in all_files:
                print(f"{order}. {file}")
                order += 1
            print("\n" + "-" * screen_width)
            
            delete_file = input("\nMasukkan nomor urut atau nama file : ")
            
            if delete_file.isdigit():
                if int(delete_file) > len(all_files):
                    print("\nFile tidak ditemukan!")
                else:
                    file = all_files[int(delete_file) - 1]
                    if file in all_files:
                        print("\nPlease wait...")
                        sleep(2)
                        os.remove(file)
                        all_files.remove(file)
                        print(f"\nFile {file} berhasil dihapus.")
            else:
                name_file = delete_file.lower()
                if name_file in all_files:
                    print("\nPlease wait...")
                    sleep(2)
                    os.remove(name_file)
                    all_files.remove(name_file)
                    print(f"\nFile {name_file} berhasil dihapus.")
                else:
                    print("\nFile tidak ditemukan!")
        else:
            print("\nPilihan yang tersedia hanya (1, 2, 3, dan 4)")
    
        repeat = input("\nIngin melanjutkan? (y/n) : ")
        
        if repeat.lower() == 'y':
            os.system("clear")
        elif repeat.lower() == 'n':
            print("")
            break
        else:
            print("\nInvalid input!\n")
            break

if __name__ == "__main__":        
    file_manager()