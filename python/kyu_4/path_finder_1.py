""" https://www.codewars.com/kata/5765870e190b1472ec0022a2 """


def path_finder(maze):
    maze_arr = list(map(lambda el: list(el), maze.split('\n')))

    start_x = start_y = 0

    maze_arr[start_x][start_y] = 'V'
    cells_to_process = [[start_x, start_y]]

    while len(cells_to_process):
        x, y = cells_to_process.pop(0)
        dest_lst = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
        for new_x, new_y in dest_lst:
            coord_within_bound = (new_x >= 0 and new_y >= 0) and (new_x < len(maze_arr) and new_y < len(maze_arr[new_x]))

            if coord_within_bound:
                next_step = maze_arr[new_x][new_y]
                if next_step == '.':
                    maze_arr[new_x][new_y] = 'V'
                    cells_to_process.append([new_x, new_y])

    return maze_arr[-1][-1] == 'V'


a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...WW",
    "...W."])

print(path_finder(a))
