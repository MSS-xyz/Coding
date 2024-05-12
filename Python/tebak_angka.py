import random

while True:
    random_number = random.randint(1, 3)
    user_number = int(input("\n\tTebak Angka Antara 1-3 = "))
    
    if user_number > 0 and user_number < 4:
        if user_number == random_number:
            print("\n\tSelamat anda berhasil menebaknya :D")
        else:
            print("\n\tSayang sekali anda gagal menebaknya :(")
            print(f"\n\tAngka yang benar adalah = {random_number}")
    else:
        print("\n\tTolong Tebak Angka Antara 1-5!!!")
        
    print("\n\t---------------------------------")    
    repeat = input("\n\tIngin bermain lagi? (y/n) = ")
    
    if repeat == 'y':
        pass
    elif repeat == 'n':
        break
    else:
        print("\n\tInvalid Input!!!")
        break