import pygame
from enum import Enum
import random as rd
from copy import deepcopy
import math

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



class Game:
    def __init__(self):
        self.turn = -1
        self.board = PList([PList([])] * 8)
        for i in range(len(self.board)):
            self.board[i] = PList([0]*8)

        self.board[3][3] = 1  # 1 for white
        self.board[4][4] = 1
        self.board[3][4] = -1  # -1 for black
        self.board[4][3] = -1


    def calculate_moves(self):
        board = self.board

        to_find = self.turn * -1
        moves = []
        for x, item in enumerate(board):
            for y, value in enumerate(item):
                if value == 0:
                    directions = return_direction((x, y), to_find, board)
                    for d in directions:
                        if find_in_direction((x, y), d, to_find, board):
                            moves.append((x, y))
        return moves

    def make_move(self, pos):    #if game ends after move returns -1
        turn = self.turn
        def flip_in_direction(board, pos, direction):
            (x, y) = (pos[0], pos[1])
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

        x, y = pos    #make_move returns 0 if game ends after making move
        moves = self.calculate_moves()
        if (x, y) in moves:
            flip_coins(self.board, (x, y))
            self.board[x][y] = self.turn
            self.turn *= -1

            if not self.calculate_moves():
                self.turn *= -1
    
    def finished(self):
        if len(self.calculate_moves()) == 0:
            self.turn *= -1
            if len(self.calculate_moves()) == 0:
                return True
        return False

    def get_winner(self):
        onecount = 0
        minuscount = 0
        for l in self.board:
            for item in l:
                if item == 1:
                    onecount+=1
                elif item == -1:
                    minuscount+=1
        if onecount > minuscount:
            return 1
        else:
            return -1
        

    def render(self, screen):
        def render_possible_moves(screen, moves):
            sx = SIZE[0]
            sy = SIZE[1]

            assert(sx == sy)
            celldim = sx // 8
            for (x, y) in moves:
                if(self.turn == 1):
                    pygame.draw.circle(screen, (255, 255, 255), (y * celldim +
                                    celldim // 2, x * celldim + celldim // 2), 0.85 * celldim/2, 3)
                elif (self.turn == -1):
                    pygame.draw.circle(screen, (0, 0, 0), (y * celldim + celldim //
                                    2, x * celldim + celldim // 2), 0.85 * celldim/2, 3)

        def render_pieces(screen):
            board = self.board
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

        # board = self.board
        make_grid_lines(screen)
        render_pieces(screen)
        moves = self.calculate_moves()
        render_possible_moves(screen, moves)
        pygame.display.flip()

    
class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.plays = 0
        self.wins = 0
        self.children = []

    def select_node(self):
        if len(self.children) < len(self.state.calculate_moves()):
            child_state = deepcopy(self.state)
            child_state.make_move(self.state.calculate_moves()[len(self.children)])
            child_node = Node(child_state, self)
            self.children.append(child_node)
            return child_node
        if len(self.children) == 0: #this list is empty means we are at end node
            #back propagate early
            return self
        max_node = max(self.children, key = lambda c: c.wins/c.plays + math.sqrt(2*math.log(self.plays)/c.plays))
        return max_node.select_node()

    def simulate_node(self):
        current_state = deepcopy(self.state)    
        while True:
            valid_moves = current_state.calculate_moves()
            if current_state.finished():
                #work out winner and backpropagate
                winner = current_state.get_winner()

                current_node = self
                # A bit dubious; may need work
                while(current_node):
                    current_node.plays+=1
                    if current_node.parent:
                        if current_node.parent.state.turn == winner:
                            current_node.wins+=1
                    current_node = current_node.parent
                break

            current_state.make_move(rd.choice(valid_moves))
         

    def get_best_move(self):
        for i in range(100):
            new_node = self.select_node()
            new_node.simulate_node()
        best_node_id = 0
        best_score = 0

        for i in range(len(self.children)):
            child = self.children[i]
            if child.wins/child.plays> best_score:
                best_score = child.wins/child.plays
                best_node_id = i
        return self.state.calculate_moves()[best_node_id]

class MCTSBot:
    def __init__(self, state, turn):
        self.node = Node(state, None)
        self.turn = turn

    def get_move(self):
        return self.node.get_best_move()


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Othello')
g = Game()
bot = MCTSBot(g, 1)

while True:
    if g.finished():
        print(g.get_winner())
        break

    if g.turn == bot.turn:
        bot.node = Node(g, None)
        move = bot.get_move()
        g.make_move(move)
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

            g.make_move((x, y))

    g.render(screen)