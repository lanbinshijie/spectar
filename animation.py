
# Animation Functions
# def openBox(title, description,choice1="Accept (A)", choice2="Cancle (C)"):
#     # 大致效果
#     '''
#     +---------------------------------+
#     | Title                        X  |
#     +---------------------------------+
#     | Description... ... ............ |
#     | ... ... ... ... ... ... ... ... |
#     | ... ... ... ... ... ... ... ... |
#     | ... ... ... ... ... ... ... ... |
#     |                                 |
#     | Accept (A)    Cancle (C)        |
#     +---------------------------------+
#     '''

import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_openBox(title, description, choice1="Accept (A)", choice2="Cancel (C)"):
    box_width = 40

    description_lines = description.split('\n')
    box_height = len(description_lines) + 7
    for line in description_lines:
        while len(line) > box_width - 4:
            box_height += 1
            line = line[box_width - 4:]

    # print(box_height)
    # exit()

    # 初始分割线
    line = "+" + "-" * (box_width - 2) + "+"

    # 清屏
    clear_screen()

    # 打印渐变的分割线
    for i in range(2, box_height):
        clear_screen()
        print(line)
        for a in range(i - 1):
            if a in [1, box_height-5, box_height-3]:
                print(line)
            else:
                print(f"|{' ' * (box_width - 2)}|")
        time.sleep(0.02)

    # time.sleep(2)
    # 打印标题
    clear_screen()
    print("+" + "-" * (box_width - 2) + "+")
    print(f"| {title.center(box_width - 4)} |")
    # print("+" + "-" * (box_width - 2) + "+")

    # 打印描述文本，处理超长行
    print("+" + "-" * (box_width - 2) + "+")
    description_lines = description.split('\n')
    for line in description_lines:
        while len(line) > box_width - 4:
            print(f"| {line[:box_width - 4].ljust(box_width - 4)} |")
            line = line[box_width - 4:]
        print(f"| {line.ljust(box_width - 4)} |")

    # 打印底部边框和按钮
    print("+" + "-" * (box_width - 2) + "+")
    print(f"| {choice1}  {choice2}{' ' * (box_width - 16 - len(choice2))} |")
    print("+" + "-" * (box_width - 2) + "+")

import time
import os


def NarrationPrint(text, title, box_width, delay=0.009):
    clear_screen()
    textr = "+-" + "-" * (box_width) + "-+"
    print(textr)
    print(f"| {title}" + " " * (box_width - len(title)) + " |")

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

# text = "As the exhaustion weighed heavily upon me, I glanced around, realizing that all I had were the shorts and clothes I wore. The situation seemed desperate, but I couldn't let despair consume me.[nextline]With a deep breath, I decided to explore my surroundings to alleviate the boredom. The island presented itself as an enigma, its dense foliage and hidden pathways beckoning me to unravel its secrets. As I walked along the shoreline, the sun kissed my skin, offering a momentary sense of warmth and comfort. My wanderings led me to stumble upon a small cave tucked away between towering cliffs. Curiosity got the better of me, compelling me to venture inside. The air inside the cave was cool and damp, mysterious shadows dancing on the walls. As I cautiously moved forward, my hand grazed against something smooth and cold—a flashlight.[nextline]Relief flooded over me as I turned on the flashlight, illuminating the cavernous space. The beam revealed hidden treasures: ancient drawings etched onto the walls and a pile of discarded belongings left behind by previous explorers. Among them, I discovered a tattered notebook - its pages filled with stories and musings. It was a serendipitous find, providing me with a source of solace and entertainment."
text = "As the exhaustion weighed heavily upon me, I glanced around, realizing that all I had we As the exhaustion weighed heavily upon me, I glanced around, realizing that all I had we As the exhaustion weighed heavily upon me, I glanced around, realizing that all I had we"
box_width = 50

NarrationPrint(text, "What", box_width)


# 使用示例
# slow_openBox("Title", "Description...\nThis is a very long line asjdhjas that will be wrapped to th ansdjha ajsd ja sj dja sjd ajs dja sjd as dja e next line to fit within the box width. ... ... ... ... ... ... ... ... ...", "Accept (A)", "Cancel (C)")
