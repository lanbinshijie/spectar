import os
import time


def clear_screen():
    os.system("cls")

def NarrationPrint(text, title, box_width=50, delay=0.009):

    lines = []
    current_line = ''

    for word in text.split():
        if len(current_line) + len(word) <= box_width:
            current_line += f'{word} '
        else:
            lines.append(current_line.strip())
            current_line = f'{word} '

    if current_line:
        lines.append(current_line.strip())

    max_length = max(len(line) for line in lines)
    horizontal_line = '+' + '-' * (max_length + 2) + '+'
    

    clear_screen()
    textr = "+-" + "-" * (max_length) + "-+"
    print(textr)
    print(f"| {title}" + " " * (max_length - len(title)) + " |")


    print(horizontal_line)

    sleeps = delay
    for line in lines:
        padded_line = '| '
        for c in line.ljust(max_length):
            padded_line += c
            print(f'{padded_line} |', end='\r')
            time.sleep(sleeps)
        print()

    print(horizontal_line)