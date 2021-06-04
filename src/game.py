import pygame
from src.button import Button
from constants.window import HEIGHT,WIDTH,FPS
from constants.colors import BACKGROUND_COLOR
from src.field import Field,Players_type
from src.board import Board
from src.bot.sniperMode import SniperMode
from src.bot.easyMode import EasyMode

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
WINDOW.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Okrety")

class Game:
    @staticmethod
    def run():
        run = True
        clock = pygame.time.Clock()
        exit_button = Button(1280, 30, 100, 50, text='Wyjście')
        reset_button = Button(1150, 30, 100, 50, text='Reset')
        board = Board(400, 150, WINDOW, Players_type.BOT)
        board2 = Board(900, 150, WINDOW, Players_type.PLAYER)

        exit_button.draw(WINDOW)
        reset_button.draw(WINDOW)
        # asd.draw(Window)
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                    board.draw_ship(pygame.mouse.get_pos())
                    board2.draw_ship(pygame.mouse.get_pos())

                    if exit_button.is_mouse_over(pygame.mouse.get_pos()):
                        run = False
                    if reset_button.is_mouse_over(pygame.mouse.get_pos()):
                        print(board2.automatic_ships_generator())
                        pass
                board2.automatic_ships_generator()
                pygame.time.wait(1000)
                bot = EasyMode(board2.get_ships())
                pygame.display.update()
                for i in range(20):
                    pygame.time.wait(1000)
                    x, y = bot.shot()
                    board2.shot(x,y)
                    pygame.display.update()
                pygame.time.wait(1000)
            pygame.display.update()

        pygame.quit()



