# 参考UI
'''
 ############################  +-----------------------------+
 #                    X     #  | Information                 |
 #   #                      #  +-----------------------------+
 #   #              #       #  | You are Tired. You have no- |
 #          #               #  | thing to do with this wier- |
 #  O              #        #  | d island. You have nothing  |
 #                          #  | but only shorts and clothes |
 ############################  +-----------------------------+
 
 +--------------------------+  +-----------------------------+
 | [Normal] Wooden Axe  x1  |  | Tips: W, S, A, D to walk, s-|
 | [Normal] Water Bot.  x1  |  | pace to trigger things, ent-|
 | [Good]   Food        x5  |  | er to make a choice         |
 +--------------------------+  +-----------------------------+

 > Make decision ... <

############################
#                    X     #
#   #                      #
#   #              #       #
#          #               #
#  O              #        #
#                          #
############################

+--------------------------+
| HP: ■■■■■■■■■□□□□□□□□□□□ |
|                          |
|                          |
+--------------------------+
'''
# 左上角是地图，左下角是物品栏，右上角是信息栏，右下角是选择栏
# 左上角用来储存当前玩家所在世界的地图，用于显示相对位置
# 左下角用来储存当前玩家的物品栏，用于显示当前玩家的物品（我觉得可以删除，或者是改成状态栏，比如HP，MP，EXP之类的）
# 右上角用来放置Instruction这样的，比如展示对话，或者任务相关
# 右下角用来放置选择栏，比如选择是否接受任务，选择是否进入某个地方，选择是否攻击某个敌人之类的

# Shark我们最后要做到的是每一个period都需要一个左下角，右上角，右下角的具体内容，状态栏我可以解决，主要还是故事线（右上角）和选择栏（右下角）

def convert_map(map_str):
    map_array = []
    for line in map_str.split('\n'):
        row = []
        for char in line:
            if char == '#':
                row.append(-1)
            elif char == 'X':
                row.append(3)
            elif char == 'O':
                row.append(1)
            else:
                row.append(0)
        map_array.append(row)
    return map_array

def print_map(map_array):
    for row in map_array:
        for cell in row:
            if cell == -1:
                print('#', end='')
            elif cell > 2:
                print('X', end='')
            elif cell == 1:
                print('O', end='')
            else:
                print(' ', end='')
        print()

map_str = """############################
#                          #
#   #                      #
#   #    X  O      #       #
#          #               #
#                 #        #
#                          #
############################"""

map_array = convert_map(map_str)
print_map(map_array)
print(map_array)
