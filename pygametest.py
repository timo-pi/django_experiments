import pygame, sys

pygame.init()
WINDOWS_WIDTH, WINDOW_HEIGHTS = 1280, 720
display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOW_HEIGHTS))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()