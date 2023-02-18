import pygame
from enum import Enum

turn = -1  # 1 for white
SIZE = (720, 720)

class PList(list):
    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        else:
            return list.__getitem__(self, index)
class DIRECTION(Enum):
    NORTH = 0,
    NORTHEAST = 1,
    EAST = 2,
    SOUTHEAST = 3,
    SOUTH = 4,
    SOUTHWEST = 5,
    WEST = 6,
    NORTHWEST = 7,


def return_direction(coord, to_find, board):
    (x, y) = (coord[0], coord[1])
    directions = []
    try:
        if board[x-1][y] == to_find:
            directions.append(DIRECTION.NORTH)
    except IndexError:
        pass

    try:
        if board[x-1][y+1] == to_find:
            directions.append(DIRECTION.NORTHEAST)
    except IndexError:
        pass
    try:
        if board[x][y+1] == to_find:
            directions.append(DIRECTION.EAST)
    except IndexError:
        pass
    try:
        if board[x+1][y+1] == to_find:
            directions.append(DIRECTION.SOUTHEAST)
    except IndexError:
        pass
    try:
        if board[x+1][y] == to_find:
            directions.append(DIRECTION.SOUTH)
    except IndexError:
        pass
    try:
        if board[x+1][y-1] == to_find:
            directions.append(DIRECTION.SOUTHWEST)
    except IndexError:
        pass
    try:
        if board[x][y-1] == to_find:
            directions.append(DIRECTION.WEST)
    except IndexError:
        pass
    try:
        if board[x-1][y-1] == to_find:
            directions.append(DIRECTION.NORTHWEST)
    except IndexError:
        pass

    return directions


def find_in_direction(coord, direction, to_find, board):
    (x, y) = (coord[0], coord[1])
    try:
        if direction == DIRECTION.NORTH:
            (x, y) = (x-1, y)
            while board[x][y] == to_find:
                (x, y) = (x-1, y)
            if board[x][y] == 0:
                return False
            if board[x][y] == to_find*-1:
                return True
        if direction == DIRECTION.NORTHEAST:
            (x, y) = (x-1, y+1)
            while board[x][y] == to_find:
                (x, y) = (x-1, y+1)
            if board[x][y] == 0:
                return False
            if board[x][y] == to_find*-1:
                return True
        if direction == DIRECTION.EAST:
            (x, y) = (x, y+1)
            while board[x][y] == to_find:
                (x, y) = (x, y+1)
            if board[x][y] == 0:
                return False
            if board[x][y] == to_find*-1:
                return True
        if direction == DIRECTION.SOUTHEAST:
            (x, y) = (x+1, y+1)
            while board[x][y] == to_find:
                (x, y) = (x+1, y+1)
            if board[x][y] == 0:
                return False
            if board[x][y] == to_find*-1:
                return True
        if direction == DIRECTION.SOUTH:
            (x, y) = (x+1, y)
            while board[x][y] == to_find:
                (x, y) = (x+1, y)
            if board[x][y] == 0:
                return False
            if board[x][y] == to_find*-1:
                return True
        if direction == DIRECTION.SOUTHWEST:
            (x, y) = (x+1, y-1)
            while board[x][y] == to_find:
                (x, y) = (x+1, y-1)
            if board[x][y] == 0:
                return False
            if board[x][y] == to_find*-1:
                return True
        if direction == DIRECTION.WEST:
            (x, y) = (x, y-1)
            while board[x][y] == to_find:
                (x, y) = (x, y-1)
            if board[x][y] == 0:
                return False
            if board[x][y] == to_find*-1:
                return True
        if direction == DIRECTION.NORTHWEST:
            (x, y) = (x-1, y-1)
            while board[x][y] == to_find:
                (x, y) = (x-1, y-1)
            if board[x][y] == 0:
                return False
            if board[x][y] == to_find*-1:
                return True
    except IndexError:
        return False

    return False


def calculate_moves(board):
    to_find = turn * -1
    moves = []
    for x, item in enumerate(board):
        for y, value in enumerate(item):
            if value == 0:
                directions = return_direction((x, y), to_find, board)
                for d in directions:
                    if find_in_direction((x, y), d, to_find, board):
                        moves.append((x, y))
    return moves


def flip_in_direction(board, pos, direction):
    (x, y) = (pos[0], pos[1])
    global turn
    try:
        if direction == DIRECTION.NORTH:
            (x, y) = (x-1, y)
            while board[x][y] == turn*-1:
                board[x][y] = turn
                (x, y) = (x-1, y)
        if direction == DIRECTION.NORTHEAST:
            (x, y) = (x-1, y+1)
            while board[x][y] == turn*-1:
                board[x][y] = turn
                (x, y) = (x-1, y+1)
        if direction == DIRECTION.EAST:
            (x, y) = (x, y+1)
            while board[x][y] == turn*-1:
                board[x][y] = turn
                (x, y) = (x, y+1)
        if direction == DIRECTION.SOUTHEAST:
            (x, y) = (x+1, y+1)
            while board[x][y] == turn*-1:
                board[x][y] = turn
                (x, y) = (x+1, y+1)
        if direction == DIRECTION.SOUTH:
            (x, y) = (x+1, y)
            while board[x][y] == turn*-1:
                board[x][y] = turn
                (x, y) = (x+1, y)
        if direction == DIRECTION.SOUTHWEST:
            (x, y) = (x+1, y-1)
            while board[x][y] == turn*-1:
                board[x][y] = turn
                (x, y) = (x+1, y-1)
        if direction == DIRECTION.WEST:
            (x, y) = (x, y-1)
            while board[x][y] == turn*-1:
                board[x][y] = turn
                (x, y) = (x, y-1)
        if direction == DIRECTION.NORTHWEST:
            (x, y) = (x-1, y-1)
            while board[x][y] == turn*-1:
                board[x][y] = turn
                (x, y) = (x-1, y-1)
    except IndexError:
        return False

    return False


def flip_coins(board, pos):
    to_find = turn*-1
    x, y = pos
    directions = return_direction((x, y), to_find, board)
    for d in directions:
        if find_in_direction((x, y), d, to_find, board):
            flip_in_direction(board, pos, d)


def render_possible_moves(screen, moves):
    sx = SIZE[0]
    sy = SIZE[1]

    assert(sx == sy)
    celldim = sx // 8
    for (x, y) in moves:
        if(turn == 1):
            pygame.draw.circle(screen, (255, 255, 255), (y * celldim +
                               celldim // 2, x * celldim + celldim // 2), 0.85 * celldim/2, 3)
        elif (turn == -1):
            pygame.draw.circle(screen, (0, 0, 0), (y * celldim + celldim //
                               2, x * celldim + celldim // 2), 0.85 * celldim/2, 3)


def render_pieces(screen, board):
    sx = SIZE[0]
    sy = SIZE[1]

    assert(sx == sy)
    celldim = sx // 8
    for x, item in enumerate(board):
        for y, value in enumerate(item):
            if(value == 1):
                pygame.draw.circle(screen, (255, 255, 255), (y * celldim +
                                   celldim // 2, x * celldim + celldim // 2), 0.85 * celldim/2)
            elif (value == -1):
                pygame.draw.circle(screen, (0, 0, 0), (y * celldim + celldim //
                                   2, x * celldim + celldim // 2), 0.85 * celldim/2)


def make_grid_lines(screen):
    sx = SIZE[0]
    sy = SIZE[1]

    assert (sx == sy)
    celldim = sx // 8
    for i in range(0, sx, celldim):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, sy))
        pygame.draw.line(screen, (0, 0, 0), (0, i), (sx, i))


def main():
    global turn
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Othello')
    screen.fill((31, 127, 31))

    board = PList([PList([])] * 8)
    for i in range(len(board)):
        board[i] = PList([0]*8)

    board[3][3] = 1  # 1 for white
    board[4][4] = 1
    board[3][4] = -1  # -1 for black
    board[4][3] = -1

    running = True
    while running:
        screen.fill((31, 127, 31))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                sx = SIZE[0]
                sy = SIZE[1]
                assert (sx == sy)
                celldim = sx // 8

                x = pygame.mouse.get_pos()
                y, x = x[0] // celldim, x[1] // celldim

                moves = calculate_moves(board)
                if (x, y) in moves:
                    flip_coins(board, (x, y))
                    board[x][y] = turn
                    turn = turn * -1


        make_grid_lines(screen)
        render_pieces(screen, board)
        moves = calculate_moves(board)
        if len(moves) == 0:
            break
        render_possible_moves(screen, moves)

        pygame.display.flip()

    input("Press Enter to continue...")


main()
