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
exit_button = Button(1200, 30, 100, 50, text='Wyjście')
reset_button = Button(1050, 30, 100, 50, text='Reset')
generate_button = Button(900,30,100,50, text="Generuj")
start_button = Button(750,30,100,50, text="Start")
sniper_button = Button(600,30,120,50, text="Sniper Mode",color=(0,255,0),text_color=(0,0,0))
medium_button = Button(450,30,140,50, text="Medium Mode",color=(0,255,0),text_color=(0,0,0))
easy_button = Button(300,30,120,50, text="Easy Mode",color=(255,0,0),text_color=(0,0,0))
player_label = Button(1050, 560, 100, 50, text='Gracz')
bot_label =  Button(550, 560, 100, 50, text='Bot')

generate_button.draw(WINDOW)
exit_button.draw(WINDOW)
reset_button.draw(WINDOW)
start_button.draw(WINDOW)
sniper_button.draw(WINDOW)
easy_button.draw(WINDOW)
medium_button.draw(WINDOW)
player_label.draw(WINDOW)
bot_label.draw(WINDOW)

class Game:
    @staticmethod
    def run():
        run = True
        clock = pygame.time.Clock()

        board = Board(400, 150, WINDOW, Players_type.BOT)
        board2 = Board(900, 150, WINDOW, Players_type.PLAYER)


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
                    if generate_button.is_mouse_over(pygame.mouse.get_pos()):
                        print(board2.automatic_ships_generator())
                    if reset_button.is_mouse_over(pygame.mouse.get_pos()):
                        pass



            pygame.display.update()

        pygame.quit()



