import os
import random

os.system("clear")

def gunting_batu_kertas():
    player_score = 0
    computer_score = 0
    screen_width = os.get_terminal_size().columns
    choice = ["Gunting", "Batu", "Kertas"]
    
    while True:
        print(f"\n" + "-" * screen_width)
        print(f"{'Permainan Gunting Batu Kertas':^{screen_width}}")
        print(f"\n{'1. Gunting':^{screen_width}}\n{'2. Batu   ':^{screen_width}}\n{'3. Kertas ':^{screen_width}}")
        print("\n" + "-" * screen_width)
        
        player = int(input("\nPilih (1, 2, 3) = "))
        computer = random.choice(choice)
        
        if player == 1:
            player = choice[0]
            
            if player == choice[0] and computer == choice[0]:
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Seri |----':^{screen_width}}")
            elif player == choice[0] and computer == choice[1]:
                computer_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Computer menang |----':^{screen_width}}")
            elif player == choice[0] and computer == choice[2]:
                player_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Player menang |----':^{screen_width}}")
            
        elif player == 2:
            player = choice[1]
            
            if player == choice[1] and computer == choice[0]:
                player_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Player menang |----':^{screen_width}}")
            elif player == choice[1] and computer == choice[1]:
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Seri |----':^{screen_width}}")
            elif player == choice[1] and computer == choice[2]:
                computer_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Computer menang |----':^{screen_width}}")
        elif player == 3:
            player = choice[2]
            
            if player == choice[2] and computer == choice[0]:
                computer_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Computer menang |----':^{screen_width}}")
            elif player == choice[2] and computer == choice[1]:
                player_score += 1
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Player menang |----':^{screen_width}}")
            elif player == choice[2] and computer == choice[2]:
                print(f"\n\t      Player [{player_score}]:[{computer_score}] Computer")
                print(f"\nPlayer memilih {'-->':^20} {player}")
                print(f"Computer memilih {'-->':^20} {computer}")
                print(f"\n{'----| Seri |----':^{screen_width}}")
        else:
            print("\nPilihan yang tersedia hanya (1, 2, dan 3)")
        
        repeat = input("\nIngin bermain lagi? (y/n) = ")
        
        if repeat.lower() == 'y':
            os.system("clear")
        elif repeat.lower() == 'n':
            print()
            break
        else:
            print("\nInvalid input!\n")
            break

gunting_batu_kertas()