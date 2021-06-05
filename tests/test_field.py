import unittest
import pygame
import random
from constants.window import WIDTH,HEIGHT
from src.field import Field,FieldStates,PlayersType

class Tests(unittest.TestCase):

    #--3--
    def test_shot_in_empty_field(self):
        WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
        field = Field(0,0,WINDOW,PlayersType.PLAYER)
        self.assertEqual(field.get_field_state(), FieldStates.EMPTY)
        field.hit()
        self.assertEqual(field.get_field_state(), FieldStates.HIT_EMPTY)

    #--4--
    def test_shot_in_enemy_ship(self):
        WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
        field = Field(0,0,WINDOW,PlayersType.BOT)
        field.draw_ship_segment()
        self.assertEqual(field.get_field_state(), FieldStates.SHIP)
        field.hit()
        self.assertEqual(field.get_field_state(), FieldStates.HIT_SHIP)

    #--6--
    def test_shot_two_times_in_empty_field(self):
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        field = Field(0, 0, WINDOW, PlayersType.PLAYER)
        self.assertEqual(field.get_field_state(), FieldStates.EMPTY)
        field.hit()
        answear = field.hit()
        self.assertEqual(answear, -1)
    #--7--
    def test_shot_two_times_in_enemy_ship(self):
        WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
        field = Field(0,0,WINDOW,PlayersType.BOT)
        field.draw_ship_segment()
        self.assertEqual(field.get_field_state(), FieldStates.SHIP)
        field.hit()
        answear = field.hit()
        self.assertEqual(answear, -1)




if __name__ == '__main__':
    unittest.main()
