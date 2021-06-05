import pygame
from src.button import Button
from constants.window import HEIGHT,WIDTH,FPS
from constants.colors import BACKGROUND_COLOR
from src.field import Field,Players_type
from src.board import Board
from src.bot.sniperMode import SniperMode
from src.bot.easyMode import EasyMode
from enum import Enum

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
WINDOW.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Okrety")
exit_button = Button(1200, 30, 100, 50, text='Wyjście')
reset_button = Button(1050, 30, 100, 50, text='Reset')
generate_button = Button(900,30,100,50, text="Generuj")
start_button = Button(750,30,100,50, text="Start")
sniper_button = Button(600,30,120,50, text="Sniper Mode",color=(255,255,0),text_color=(0,0,0))
medium_button = Button(440,30,140,50, text="Medium Mode",color=(255,255,0),text_color=(0,0,0))
easy_button = Button(300,30,120,50, text="Easy Mode",color=(255,0,0),text_color=(0,0,0))
player_label = Button(1050, 560, 100, 50, text='Gracz')
bot_label =  Button(550, 560, 100, 50, text='Bot')
message_window = Button(50,150,300,50,text='Ułóż swoją flotę',color=(0,0,0),text_color=(255,255,255))

generate_button.draw(WINDOW)
exit_button.draw(WINDOW)
reset_button.draw(WINDOW)
start_button.draw(WINDOW)
sniper_button.draw(WINDOW)
easy_button.draw(WINDOW)
medium_button.draw(WINDOW)
player_label.draw(WINDOW)
bot_label.draw(WINDOW)
message_window.draw(WINDOW)

class Game:

    @staticmethod
    def run():
        run = True
        clock = pygame.time.Clock()
        state = GameState.PREPARE
        mode = GameMode.EASY


        bot_board = Board(400, 150, WINDOW, Players_type.BOT)
        player_board = Board(900, 150, WINDOW, Players_type.PLAYER)

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    print(mouse_position)
                    if state == GameState.PREPARE:
                        player_board.draw_ship(mouse_position)
                        if generate_button.is_mouse_over(mouse_position):
                            print(player_board.automatic_ships_generator())
                        if start_button.is_mouse_over(mouse_position):
                            if player_board.check_ships_position():
                                state = GameState.BATTLE
                                bot_board.automatic_ships_generator()
                                if mode == GameMode.EASY:
                                    bot = EasyMode(player_board.get_ships())
                                if mode == GameMode.MEDIUM:
                                    bot = EasyMode(player_board.get_ships())
                                if mode == GameMode.SNIPER:
                                    bot = SniperMode(player_board.get_ships())
                                round = RoundMode.PLAYER
                                message_window.change_text("Twój strzał",WINDOW)
                            else:
                                message_window.change_text("Błędne ustawienie",WINDOW)

                        if medium_button.is_mouse_over(mouse_position):
                            mode = GameMode.MEDIUM
                            medium_button.change_color((255,0,0),WINDOW)
                            easy_button.change_color((255,255,0),WINDOW)
                            sniper_button.change_color((255,255,0),WINDOW)
                        if easy_button.is_mouse_over(mouse_position):
                            mode = GameMode.EASY
                            medium_button.change_color((255,255,0),WINDOW)
                            easy_button.change_color((255,0,0),WINDOW)
                            sniper_button.change_color((255,255,0),WINDOW)
                        if sniper_button.is_mouse_over(mouse_position):
                            mode = GameMode.SNIPER
                            medium_button.change_color((255,255,0),WINDOW)
                            easy_button.change_color((255,255,0),WINDOW)
                            sniper_button.change_color((255,0,0),WINDOW)

                    if state == GameState.BATTLE:
                        if round == RoundMode.PLAYER:
                            if bot_board.shot_i(pygame.mouse.get_pos()) ==0:
                                round = RoundMode.BOT
                            if bot_board.check_win():
                                state = GameState.WAIT
                                message_window.change_text("Wygrana gracza",WINDOW)

                    if exit_button.is_mouse_over(mouse_position):
                        run = False

                    if reset_button.is_mouse_over(mouse_position):
                        message_window.change_text("Ułóż swoją flotę",WINDOW)
                        state = GameState.PREPARE
                        bot_board = Board(400, 150, WINDOW, Players_type.BOT)
                        player_board = Board(900, 150, WINDOW, Players_type.PLAYER)


            if state == GameState.BATTLE and round == RoundMode.BOT:
                print('bot strzela')
                x, y = bot.shot()

                if player_board.shot(x, y) == 0:
                    round = RoundMode.PLAYER
                if player_board.check_win():
                    state = GameState.WAIT
                    message_window.change_text("Wygrana bota",WINDOW)

            pygame.display.update()

        pygame.quit()



class GameState(Enum):
    PREPARE = 0
    BATTLE = 1
    WAIT = 2
class GameMode(Enum):
    EASY = 0
    MEDIUM = 1
    SNIPER = 2

class RoundMode:
    PLAYER = 0
    BOT = 1