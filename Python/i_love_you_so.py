import os
import sys
from time import sleep

os.system("clear")

def lyrics():
    lines = [
        ("I'm gonna pack my things", 0.1, False),
        ("and leave you behind", 0.1, False),
        ("this feeling's old and I know", 0.095, False),
        ("that I've made up my mind", 0.09, False),
        ("I hope you feel what I felt", 0.1, False),
        ("when you shattered my soul", 0.09, False),
        ("'cause you were cruel", 0.075, False),
        ("and I'm a fool", 0.07, False),
        ("so, please let me go", 0.1, True),
        ("but I love you so", 0.13, False),
        ("please let me go", 0.13, True),
        ("I love you so", 0.15, False),
        ("please let me go", 0.13, True),
        ("I love you so", 0.15, False),
        ("please let me go", 0.13, True),
        ("I love you so ♡.", 0.14, False)
    ]
    
    delays = [
        0.8,
        0.6,
        0.9,
        0.5,
        0.7,
        0.5,
        0.4,
        0.8,
        2.3,
        1.7,
        0.5,
        1.7,
        0.7,
        1.7,
        0.5,
        3.4
    ]
    
    print(f"{'The Walters - I Love You So':^50}\n\n")
    
    for line_delay, (lyric, char_delay, is_colored) in enumerate(lines):
        if is_colored:
            print("\033[31m", end="")
            
        for char in lyric:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
            
        if is_colored:
            print("\033[39m", end="")
            
        sleep(delays[line_delay])
        print("")
    print("")

if __name__ == "__main__":
    lyrics()