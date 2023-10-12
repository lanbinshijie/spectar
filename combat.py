from lib import NarrationPrint, TyperPrint
from main import clear_screen
from status import *
now_dialog_lock = UNLOCK

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
        TyperPrint("The battle between you and "+name+" starts!", sleep=0.02)
    
    print("+--------------+\t" * len(choices))
    for i in choices:
        print(f"| {i[0]}{(12-len(i[0]))*' '} |\t", end="")
    print()
    print("|--------------|\t" * len(choices))
    for i in choices:
        print(f"| Damage: {i[1]}{(2-len(str(i[1])))*' '}{(12-10)*' '} |\t", end="")
    print()
    for i in choices:
        print(f"| MP: {'+' if i[3] > 0 else ' '}{i[3]}{(3-len(str(i[3])))*' '}{(12-8)*' '} |\t", end="")
    print()
    for i in choices:
        print(f"| HP: {'+' if i[2] > 0 else ' '}{i[2]}{(3-len(str(i[2])))*' '}{(12-8)*' '} |\t", end="")
    print()
    print("|              |\t" * len(choices))
    for i in choices:
        print(f"| Press [{i[4]}]{(12-9)*' '} |\t", end="")
    print()
    print("|              |\t" * len(choices))
    print("+--------------+\t" * len(choices))
    exit()

    # 打印所有的choices
    for i in range(len(choices)):
        print(f"[{choices[i][4]}] {i+1}. {choices[i][0]} {'(Optional) ' if choices[i][7] == False else ''}", end="")
        # Print more information
        print(f"  --   Damage: {choices[i][1]} HP: {choices[i][2]} MP: {choices[i][3]}")
    
    
    now_dialog_lock = UNLOCK

if __name__ == "__main__":
    combat_print_battle_screen("Hunter")