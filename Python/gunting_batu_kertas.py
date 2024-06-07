import os
import random

os.system("clear")

def gunting_batu_kertas():
    player_score = 0
    computer_score = 0
    screen_width = os.get_terminal_size().columns
    choice = ["Gunting", "Batu", "Kertas"]
    
    while True:
        print("-" * screen_width)
        print(f"{'PERMAINAN GUNTING BATU KERTAS':^{screen_width}}\n")
        print(f"{'1. Gunting':^{screen_width}}")
        print(f"{'2. Batu   ':^{screen_width}}")
        print(f"{'3. Kertas ':^{screen_width}}")
        print(f"{'4. Keluar ':^{screen_width}}")
        print("\n" + "-" * screen_width)
        
        player_choice = int(input("\nSilahkan pilih (1, 2, 3, 4) : "))
        computer_choice = random.choice(choice)
        
        if player_choice == 1:
            player_choice = choice[0]
            if player_choice == choice[0] and computer_choice == choice[0]:
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Seri |-----':^{screen_width}}")
            elif player_choice == choice[0] and computer_choice == choice[1]:
                computer_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Computer menang |-----':^{screen_width}}")
            elif player_choice == choice[0] and computer_choice == choice[2]:
                player_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Player menang |-----':^{screen_width}}")
                
        elif player_choice == 2:
            player_choice = choice[1]
            if player_choice == choice[1] and computer_choice == choice[0]:
                player_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Player menang |-----':^{screen_width}}")
            elif player_choice == choice[1] and computer_choice == choice[1]:
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Seri |-----':^{screen_width}}")
            elif player_choice == choice[1] and computer_choice == choice[2]:
                computer_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Computer menang |-----':^{screen_width}}")
                
        elif player_choice == 3:
            player_choice = choice[2]
            if player_choice == choice[2] and computer_choice == choice[0]:
                computer_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Computer menang |-----':^{screen_width}}")
            elif player_choice == choice[2] and computer_choice == choice[1]:
                player_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Player menang |-----':^{screen_width}}")
            elif player_choice == choice[2] and computer_choice == choice[2]:
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\n\tPlayer {'-->':^20} {player_choice}")
                print(f"\tComputer {'-->':^20} {computer_choice}")
                print(f"\n{'-----| Seri |-----':^{screen_width}}")
        
        elif player_choice == 4:
            print("")
            break
        else:
            print("\nPilihan yang tersedia hanya (1, 2, 3, dan 4)")
        
        repeat = input("\nIngin bermain lagi? (y/n) : ")
        
        if repeat.lower() == 'y':
            os.system("clear")
        elif repeat.lower() == 'n':
            print("")
            break
        else:
            print("\nInvalid Input!\n")
            break

if __name__ == "__main__":
    gunting_batu_kertas()