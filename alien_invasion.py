import sys
import pygame
from Settings import Settings
from ship import Ship
import game_functions as gf

#alien invasion game

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    ship = Ship(screen)

    pygame.display.set_caption("REVENGE OF LORD XENU")
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pygame.display.flip()


run_game()

