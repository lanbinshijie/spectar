welcome = '''
   _____                         _                  
  / ____|                       | |                 
 | (___    _ __     ___    ___  | |_    __ _   _ __ 
  \\___ \\  | '_ \\   / _ \\  / __| | __|  / _` | | '__|
  ____) | | |_) | |  __/ | (__  | |_  | (_| | | |   
 |_____/  | .__/   \\___|  \\___|  \\__|  \\__,_| |_|   
          | |                                       
          |_|                                     0.96-rc1
==========================================================

                Spectar Adventure I: Eden
             Edition Version 0.9.6-rc1 Octo23
    Author: Shark Liang(Text&Story) Leo Huo(Code&Design)

========================================================== 

Press a key to continue...'''
import faulthandler
faulthandler.enable()

import itertools
import keyboard
import os
import time
import random
from status import *
from lib import NarrationPrint, TyperPrint

CONSTANT_CLEAR_SCREEN = 'cls' if os.name == 'nt' else 'clear'

chapter1 = {
    "chapter_id": 1,
    "chapter_name": "Chapter 1: The Beginning",
    "description": "This is the first chapter of the game. You will start your journey from here.",
    "map": {
        0: [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]],
        1: [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]],
        2: [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]],
    },
    "plot": {
        0: [("a", "a")],
        1: [("b", "b")],
        -10: [("System", "For dialog, you can press \"a\" to continue."),("Narrator", "In a parallel dimension that hovers between worlds, you find yourself awake upon a floating island— A place of breathtaking beauty, overshadowed by the heaviness of forgotten memories. "), ("Narrator", "You slowly rise, eyes scanning the surroundings, trying to make sense of the unfamiliar surroundings."),("You", "Where... Where am I? And what is this place?"), ("Narrator", "Lost and unsure, you struggle with scattered fragments of your history. Desperate for answers, you bravely venture into the unknown, not realizing the dangers that await you."), ("Narrator", "Arriving at the forest, filled with tall trees and patches of sunlight. The smells of fresh soil and plants fill your lungs. Sunlight filters through the trees, revealing beautiful flowers and rocks covered in soft moss. A gentle stream flows through the forest, creating a peaceful atmosphere.", ("Narrator", "As you take cautious steps, uneasiness lingers in the air. Suddenly, a dark presence emerges from the shadows, a figure shrouded in mystery and emanating an icy aura blocking your path. Startled, you instinctively assume a defensive stance."))],
        -11: [("Narrator", "Emerging from the depths of darkness, a menacing figure materializes, its eyes ablaze with hunger. As it comes into view, a chilling growl escapes its lips, echoing through the air. The intensity of its gaze pierces through your very being, sending a wave of unease down your spine. "), ("Narrator", "With every step, its anger becomes more pronounced, each movement revealing a relentless determination. Its appearance is a stark reminder of the danger in its wake, leaving you on edge and ready to face the impending challenge. "), ("???", "Ahhhhhh!"), ("You", "Who is there?"), ("Leo", "It has to be a sample of combat but it is not finished yet in version 1. Sorry :)"),("System", "*Introduces the combat system to the player. Use end-game difficulty so that the player will eventually lose*"), ("Leo", "Just pretent that you lose this combat. :3"),("Narrator", "As a desperate will to survive fills your mind, your body gives way, and you fall to the ground. Inch by inch, the creature advances, yet your trembling body remains frozen, unresponsive to your frantic efforts to rise, paralyzed with fear. "), ("Narrator", "As a desperate will to survive fills your mind, your body gives way, and you fall to the ground. Inch by inch, the creature advances, yet your trembling body remains frozen, unresponsive to your frantic efforts to rise, paralyzed with fear. "),("Narrator","When all seemed lost, an arrow flew through the air, striking the beast's head. A quick and nimble figure dashed through the forest, landing powerful blows on the creature. Startled, the wounded beast fled. The person then leaped down from a tree and approached you.")],
        2: [("You", "Thanks for saving me. I could have died right there."), ("Hunter (???)", "No worries. My name is Ethan, what's yours?"), ("You", "Me? I think I lost my memories. I don't know where I am, who I am, and what I'm doing..."), ("Ethan", "Hmmm... Let's go back to my camp. Maybe you can get some clues there. "), ("Narrator", "After walking for a while, a camp suddenly appeared in front of you."), ("Narrator", "As you cautiously follow Ethan's lead, curiosity propels you forward, inching closer to his camp. The crackling fire casts dancing shadows around the clearing, illuminating a makeshift shelter crafted with care. A worn map rests on a weathered stump, its faded lines hinting at forgotten destinations. Nearby, an assortment of meticulously crafted weapons lies neatly arranged, their edges gleaming in the firelight. Tattered journals, their pages filled with faded ink, scatter across a makeshift table."), ("Ethan", "Welcome to the Harmonian camp.")],
    },
    "special": {
        4: {
            "name": "Shadowy Figure (???)",
            "description": "......",
            "talks": [
                "......"
            ],
            "choice": {
                0: ["A", "...", 3],
                1: ["A", "...", 3]
            }

        },
        5: {
            "name": "Hunter (???)",
            "description": "You know it's dangerous to be out without a weapon. You never know what might hide in those bushes. ",
            "talks": [
                "You know it's dangerous to be out without a weapon. You never know what might hide in those bushes. ",
            ],
            "choice": {
                0: ["A", "\"Uh, Thanks.\"", 4],
                1: ["D", "What?", 4],
            }
        },
        3: {
            "name": "Guide",
            "description": "Hello, I am the guide of this lo game. aha I will help you to get familiar with this game. Now, please press 'W' to move up.",
            "talks": [
                "Oh, here is a new comer...",
                "Uululuu! Huluuluu!",
                "(Turn back) I thought I heard something...",
                "Oh, it's just a little fun thing."
            ],
            "choice": {
                0: ["F", "Fight", 0],
                1: ["A", "Ask", 1],
            }
        }
    },
    "event": {
        3: [0, ".....", [["A", "What happened?", -2, 0]]],
        4: [0, "You see, I helped you up.", [["A", "Continue", -2, 0]]],
        0: [0, "He don't want to fight to you.", [["A", "Talk", 1]]],
        1: [0, "Ahh, you wanna talk to me? Oh, I am just a guide to test this game haha.", [["A", "Continue to talk", 2]]],
        2: [0, "I am just a guide to test this game haha.", [["A","Leave", -2, 0]]],
    }
}

now_map_status = MAP_UNLOCKED
now_mode = GAME_STATUS_STARTMENU
now_map = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
now_chapter = {}
now_text = []
now_hp = 100
now_mp = 100
now_choice = -1
now_special = 0
now_chapter_process = 0
now_narration_process = 0
now_dialog_lock = UNLOCK

def game_load_chapter(chapterInfo):
    global now_map, now_text, now_chapter, pos_x, pos_y
    global now_choice, now_special, now_chapter_process, now_narration_process
    pos_x, pos_y = calc_find_coordinate_with_one()
    # now_map = chapterInfo["map"]
    edit_display_text(chapterInfo["chapter_name"]+"\n"+chapterInfo["description"])
    # print(now_map)
    now_chapter = chapterInfo
    # 重置一些全局变量
    now_choice = -1
    now_special = 0
    now_chapter_process = 0
    now_narration_process = 0
    now_map = now_chapter["map"][now_chapter_process]
    display_print_narration()

def display_print_narration():
    global now_chapter, now_narration_process, now_chapter_process, now_mode, now_dialog_lock
    if now_narration_process >= len(now_chapter["plot"][now_chapter_process]):
        now_mode = GAME_STATUS_MAPMODE
        now_narration_process = 0
        print_Screen()
        return
    # 锁定状态为对话状态
    now_mode = GAME_STATUS_DIALOGMODE
    clear_screen()
    # 打印now_chapter["plot"][now_chapter_process][now_narration_process]
    now_dialog_lock = LOCK
    NarrationPrint(now_chapter["plot"][now_chapter_process][now_narration_process][1], now_chapter["plot"][now_chapter_process][now_narration_process][0])
    now_dialog_lock = UNLOCK
    # 更新now_narration_process
    now_narration_process += 1
    # 如果now_narration_process超过了最大值，则解锁状态为地图状态，并print_Screen
    

def calc_find_coordinate_with_one():
    global now_map
    count = 0
    x = -1
    y = -1

    for i, j in itertools.product(range(len(now_map)), range(len(now_map[0]))):
        if now_map[i][j] == 1:
            count += 1
            x = i
            y = j

    return (x, y) if count == 1 else None


def calc_display_find_text_width(text, max_height=12):
    left = 1  # 最小宽度为1个字符
    right = len(text)  # 最大宽度为整个文本长度

    while left <= right:
        mid = (left + right) // 2  # 取中间宽度
        lines = 0  # 当前宽度能够完整显示的行数

        remaining_text = text
        while remaining_text:
            line = remaining_text[:mid]
            remaining_text = remaining_text[mid:]
            lines += 1

        if lines <= max_height:
            right = mid - 1  # 当前宽度能完整显示，继续缩小宽度
        else:
            left = mid + 1  # 当前宽度不能完整显示，增大宽度

    return left



def edit_hp_add(num):
    global now_hp
    if now_hp + num > 100:
        now_hp = 100
        return False
    now_hp += num
    return True

def edit_hp_minus(num):
    global now_hp
    if now_hp - num < 0:
        now_hp = 0
        return False
    now_hp -= num
    return True

def clear_screen():
    os.system(CONSTANT_CLEAR_SCREEN)

def display_print_health_bar():
    num_filled_blocks = now_hp // 5  # 每个实心方块代表5点血量
    num_empty_blocks = 20 - num_filled_blocks

    filled_block = '■'
    empty_block = ' '

    health_bar = filled_block * num_filled_blocks + empty_block * num_empty_blocks
    print(health_bar, end='')

def display_print_magic_bar():
    num_filled_blocks = now_mp // 5  # 每个实心方块代表5点血量
    num_empty_blocks = 20 - num_filled_blocks

    filled_block = '■'
    empty_block = ' '

    health_bar = filled_block * num_filled_blocks + empty_block * num_empty_blocks
    print(health_bar, end='')

def edit_display_text(text):
    global now_text
    now_text.clear()
    # 计算出文本的最小宽度
    min_width = calc_display_find_text_width(text)
    min_width = max(min_width+2, 37)
    # 将第一行填充为+---+的形式
    now_text = ['+' + '-' * (min_width) + '+']

    # 将文本按照最小宽度进行分割
    for line in text.split('\n'):
        while len(line) > min_width - 2:
            # 找到单词断开的位置
            break_index = line[:min_width - 2].rfind(' ')
            if break_index != -1:  # 如果找到了断开的位置
                now_text.append(f'| {line[:break_index].ljust(min_width - 2)} |')  # 将断开的单词放入当前行
                line = line[break_index + 1:]  # 更新剩余的文本
            else:  # 没有找到断开的位置，直接切换到下一行显示
                now_text.append(f'| {line[:min_width - 2].ljust(min_width - 2)} |')
                line = line[min_width - 2:]
        now_text.append(f'| {line.ljust(min_width - 2)} |')
    # 如果总行数不足13行（包括开头的+---+），则补足13行
    while len(now_text) < 13:
        now_text.append(f'|{" " * (min_width)}|')
    # 将最后一行填充为+---+的形式
    now_text.append('+' + '-' * (min_width) + '+')


def print_Screen():
    global now_map, now_text
    clear_screen()
    # print(now_text, len(now_text))
    # print(now_map)
    for i in range(16):
        if i < 8:
            for j in range(28):
                if now_map_status == MAP_LOCKED:
                    print("#", end="")
                else:
                    if now_map[i][j] == -1:
                        print("#", end="")
                    elif now_map[i][j] == 0:
                        print(" ", end="")
                    elif now_map[i][j] == 1:
                        print("O", end="")
                    elif now_map[i][j] > 2:
                        print("X", end="")
            print(f"  {now_text[i]}", end="")
            print()

        for j in range(28):
            if (i == 9 and j == 0) or (i == 9 and j==27): # 左上角和右上角
                print("+", end="")
            elif i == 9: # 上边界
                print("-", end="")
            elif i == 13 and j == 0: # 左下角
                print("+", end="")
            elif i == 13 and j == 27: # 右下角
                print("+", end="")
            elif i == 13: # 下边界
                print("-", end="")
            elif j == 0 and i > 8 and i < 14: # 左
                print("|", end="")

            if i > 8:
                if i == 10 and j == 0:
                    print(" HP: ", end="")
                    display_print_health_bar()
                    print(" |", end="")
                if i == 11 and j == 0:
                    print(" MP: ", end="")
                    display_print_magic_bar()
                    print(" |", end="")
                elif i in [12] and j == 0:
                    print(" " * 26, end="|")

        if i == 8: 
            print(" "*30, end="")
            print(now_text[i])
        if i > 8 and i < len(now_text):
            print(f"  {now_text[i]}", end="")
            print()
        if i == 15:
            if now_mode == GAME_STATUS_MAPMODE:
                print("\n> Make move ... <")
            else:
                print("\n> Make decision ... <")

def calc_map_move(direction, units):
    # 记录特殊数字（大于2的数字），如果移动后不为-1，则说明出发了剧情，剧情的id为special的值
    special = -1 
    if direction == MAP_DIRECTION_UP:
        # 判断是否可以向上移动（不为-1）
        if now_map[pos_x - units][pos_y] != -1:
            # 判断是否为大于2的数字
            if now_map[pos_x - units][pos_y] > 2:
                special = now_map[pos_x - units][pos_y]
            # 移动
            now_map[pos_x][pos_y] = 0
            now_map[pos_x - units][pos_y] = 1
    elif direction == MAP_DIRECTION_DOWN:
        if now_map[pos_x + units][pos_y] != -1:
            if now_map[pos_x + units][pos_y] > 2:
                special = now_map[pos_x + units][pos_y]
            now_map[pos_x][pos_y] = 0
            now_map[pos_x + units][pos_y] = 1
    elif direction == MAP_DIRECTION_LEFT:
        if now_map[pos_x][pos_y - units] != -1:
            if now_map[pos_x][pos_y - units] > 2:
                special = now_map[pos_x][pos_y - units]
            now_map[pos_x][pos_y] = 0
            now_map[pos_x][pos_y - units] = 1
    elif direction == MAP_DIRECTION_RIGHT:
        if now_map[pos_x][pos_y + units] != -1:
            if now_map[pos_x][pos_y + units] > 2:
                special = now_map[pos_x][pos_y + units]
            now_map[pos_x][pos_y] = 0
            now_map[pos_x][pos_y + units] = 1

    return special
        
def logic_deal_special(special):
    global now_text, now_map_status, now_choice, now_special, now_mode
    now_special = special
    now_map_status = MAP_LOCKED
    now_mode = GAME_STATUS_QUESTMODE
    npc = now_chapter["special"][special]
    dialog = ""
    dialog += npc["name"] + "\n"
    dialog += "---------------" + "\n"
    dialog += npc["description"] + "\n"
    dialog += "\n\n"
    dialog += f"{now_chapter['special'][special]['choice'][0][1]} ({now_chapter['special'][special]['choice'][0][0]})  {now_chapter['special'][special]['choice'][1][1]} ({now_chapter['special'][special]['choice'][1][0]})"
    edit_display_text(dialog)
    print_Screen()

def logic_deal_special_continue_speech(speech, choices):
    global now_text, now_map_status, now_choice, now_special, now_mode, now_chapter_process, now_map
    if choices[0] == -2:
        now_map_status = MAP_UNLOCKED
        now_mode = GAME_STATUS_MAPMODE
        now_choice = -1
        now_special = 0
        now_chapter_process += 1
        now_map = now_chapter["map"][now_chapter_process]
        print_Screen()
        return
    npc = now_chapter["special"][now_special]
    dialog = ""
    dialog += npc["name"] + "\n"
    dialog += "---------------" + "\n"
    dialog += speech + "\n"
    dialog += "\n\n"
    dialog += f"{choices[0][1]} ({choices[0][0]})  {choices[1][1]} ({choices[1][0]})"

    edit_display_text(dialog)
    print_Screen()


def logic_deal_with_choice_text():
    # 返回一段文字，包括npc说的话和给出的选项
    global now_choice, now_special
    if now_special == 0: return
    if now_choice == -1:
        # 胡言乱语
        return random.choice(now_chapter["special"][now_special]["talks"]), [["A", "Leave", -2]]
    else:
        # dialog += npc["description"] + "\n"
        # dialog += f"{now_chapter['special'][special]['choice'][0][1]} ({now_chapter['special'][special]['choice'][0][0]})  {now_chapter['special'][special]['choice'][1][1]} ({now_chapter['special'][special]['choice'][1][0]})"
        # 返回两个值，第一个是npc说的话，第二个是选项
        return now_chapter["event"][now_choice][1], now_chapter["event"][now_choice][2]

        

def logic_deal_with_choice(choice):
    global now_choice
    if now_special == 0: return
    if now_choice == -1:
        # choice去now_chapter.special.special_id.choice里面获取
        choices = now_chapter["special"][now_special]["choice"]
        # print(choices)
        if choice.lower() == choices[0][0].lower():
            now_choice = choices[0][2]
        elif choice.lower() == choices[1][0].lower():
            now_choice = choices[1][2]
        # print(now_choice)
    else:
        # choice去now_chapter.event中获取
        choices = now_chapter["event"][now_choice][2]
        if choice.lower() == choices[0][0].lower():
            # print(choices)
            now_choice = choices[0][2]
        # 有可能出现只有一个选项的情况（注意下标越界）
        if len(choices) == 2:
            if choice.lower() == choices[1][0].lower():
                now_choice = choices[1][2]
    if now_choice == -2:
        next_map = choices[0][3]
        return "", [-2, next_map]
    
    speech, cho = logic_deal_with_choice_text()
    if len(cho) == 1:
        cho.append(["", "", -1])
    return speech, cho
        
def combat_print_battle_screen(name, hurt=None, method=None, choices=None, dialog=None):
    global now_dialog_lock
    now_dialog_lock = LOCK
    # 示例选项
    choices = [
        # This means there is a choice called "Basic-Attack", it will cause 10 damage to the enemy, 
        # and it will cost 0 hp, and it will cost 10 mp, and it will be displayed as "A"
        # And after you choose this option, your round will end, and you can't choose other options
        # And the number 1 after true means in your round, you can use how many times of this option
        # The last True means this option is not optional, you must make a decision from all non-optional options
        # The PS(physical strength) and MS(magic strength) may add in the future !!!
        ["Basic-Attack", 10, 0, -10, "A", True, 1, True],
        ["Skill", 25, 0, -20, "B", True, 1, True],
        ["Pass", 0, 0, 0, "C", True, 1, True],
        ["Restore", 0, +20, -20, "D", False, 1, False],
    ]
    clear_screen()
    if hurt == None and dialog == None:
        # 没有发生冲突或者对话，打印开始战斗字样
        TyperPrint("The battle between you and "+name+" starts!", sleep=0.002)
    
    # 打印所有的choices
    for i in range(len(choices)):
        print(f"[{choices[i][4]}] {i+1}. {choices[i][0]} {'(Optional) ' if choices[i][7] == False else ''}", end="")
        # Print more information
        print(f"  --   Damage: {choices[i][1]} MP: {choices[i][2]} HP: {choices[i][3]}")
    
    
    now_dialog_lock = UNLOCK


def logic_keypress(key):
    global now_mode, pos_x, pos_y, now_map_status
    if now_mode == GAME_STATUS_STARTMENU:
        if key == "a":
            # game_load_chapter(chapter1)
            combat_print_battle_screen("Leo")
    elif now_mode == GAME_STATUS_MAPMODE:
        pos_x, pos_y = calc_find_coordinate_with_one()        
        # 在地图模式下
        if key == "l":
            now_map_status = MAP_LOCKED
            print_Screen()
            return
        elif key == "u":
            now_map_status = MAP_UNLOCKED
            print_Screen()
            return
        if now_map_status == MAP_LOCKED:
            return
        if key == "w":
            special = calc_map_move(MAP_DIRECTION_UP,1)
        elif key == "s":
            special = calc_map_move(MAP_DIRECTION_DOWN,1)
        elif key == "a":
            special = calc_map_move(MAP_DIRECTION_LEFT,1)
        elif key == "d":
            special = calc_map_move(MAP_DIRECTION_RIGHT,1)
        else:
            return
        if special != -1:
            logic_deal_special(special)
        print_Screen()
    elif now_mode == GAME_STATUS_QUESTMODE:
        speech, choice = logic_deal_with_choice(key)
        # print(speech, choice)
        logic_deal_special_continue_speech(speech, choice)
        if choice[0] == -2:
            # time.sleep(1)
            display_print_narration()
        else:
            print_Screen()
    elif now_mode == GAME_STATUS_DIALOGMODE:
        # 按下a是下一段对话
        if key == "a":
            if now_dialog_lock == LOCK:
                return
            display_print_narration()
    else:
        ...
        

# print_Screen()
sentences = ['The quick brown fox jumps over the lazy dog.', 'She sells seashells by the seashore.', 'Peter Piper picked a peck of pickled peppers.', 'How can a clam cram in a clean cream can?', 'I scream, you scream, we all scream for ice cream.', 'Sally sells seashells down by the seashore.', 'Betty Botter bought some butter but the butter was bitter.', 'I saw Susie sitting in a shoeshine shop.', 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?', 'She stood on the balcony, inexplicably mimicking him hiccuping, and amicably welcoming him in.']
def move_character(key):
    global now_hp, now_text
    if key.name == 'w':
        logic_keypress("w")
    elif key.name == 'a':
        logic_keypress("a")
    elif key.name == 's':
        logic_keypress("s")
    elif key.name == 'd':
        logic_keypress("d")
    else:
        logic_keypress(key.name)
    time.sleep(0.05)



if __name__ == "__main__":
    print(welcome)
    # game_load_chapter(chapter1)
    
    # edit_display_text("Hello World! The minimum width required to display the text is:The minimum width required to display the text is:The minimum width required to display the text is: Hello World! The minimum width required to display the text is:The minimum width required to display the text is:The minimum width required to display the text is: Hello World! The minimum width required to display the text is:The minimum width required to display the text is:The minimum width required to display the text is: Hello World! The minimum width required to display the text is:The minimum width required to display the text is:The minimum width required to display the text is:")

    keyboard.on_press(move_character)
    keyboard.wait('esc')  # 等待按下ESC键退出程序
