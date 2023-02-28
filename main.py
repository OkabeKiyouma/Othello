import pygame
from othello import *

class GameState:
    def __init__(self, turn):
        self.turn = turn  # 1 for white
        #scores tuples??

game = GameState(-1)

def main():
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

                moves = calculate_moves(board, game.turn)
                if (x, y) in moves:
                    flip_coins(board, (x, y), game.turn)
                    board[x][y] = game.turn
                    game.turn = game.turn * -1


        make_grid_lines(screen)
        render_pieces(screen, board)
        moves = calculate_moves(board, game.turn)
        if len(moves) == 0:
            if(len(calculate_moves(board, game.turn * -1)) == 0):
                break
            game.turn = game.turn * -1
        render_possible_moves(screen, moves, game.turn)

        pygame.display.flip()

    input("Press Enter to continue...")


main()
