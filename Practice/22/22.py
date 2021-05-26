maze = (
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
)

maze_w = len(maze[0])
maze_h = len(maze)


def valid_location(x: int, y: int) -> bool:

    return y >= 0 and y < maze_h and x >= 0 and x < maze_w and maze[y][x] != '#';


def get_char(x: int, y: int) -> str:
    if valid_location(x, y):
        
        return maze[y][x]

    return None


def maze_exit(attended: list, ways_out: list, x, y):
    if not valid_location(x, y):

        return

    t = (x, y)
    if t in attended:

        return

    attended = [v for v in attended]
    attended.append(t)
    char = get_char(x, y)

    if char is None:

        return

    if char != ' ' and char not in ways_out:
        ways_out.append(char)
    maze_exit(attended, ways_out, x + 1, y)

    maze_exit(attended, ways_out, x - 1, y)

    maze_exit(attended, ways_out, x, y + 1)
    
    maze_exit(attended, ways_out, x, y - 1)


while True:
    try:
        x, y = map(int, input("Введите координаты x, y - ").split())

        if not valid_location(x, y):
            print("Не верные координаты!")

            break

        ways_out = []

        maze_exit([], ways_out, x, y)

        if ways_out:
            print(' '.join(ways_out))
        else:
            print("Выходов нет...")

        break

    except KeyboardInterrupt:

        break

    except ValueError:

        print("Повторите ввод!")
