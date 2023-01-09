import pygame
import random
from constants import *


def main():
    pygame.init()
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    squirrel = [(START_X_POS_SQU, START_Y_POS_SQU), (START_X_POS_SQU + SPACE_X_POS_SQU, START_Y_POS_SQU),
                (START_X_POS_SQU + 2 * SPACE_X_POS_SQU, START_Y_POS_SQU)]
    squirrel_is = False

    screen.fill(GREEN)

    finish = False
    while not finish:
        screen.fill(GREEN)

        for index in range(3):
            add_image(CARROT_IMAGE, START_X_POS_CAR + index * SPACE_X_POS_CAR, Y_POS_CAR, CARROT_WIDTH, CARROT_HEIGHT,
                      screen)
            add_image(HOLE_IMAGE, START_X_POS_HOL + index * SPACE_X_POS_HOL, Y_POS_HOL, HOLE_WIDTH, HOLE_HEIGHT, screen)

        if not squirrel_is:
            squirrel_xy = random.choice(squirrel)
            squirrel_start_x = squirrel_xy[0]
            squirrel_start_y = squirrel_xy[1]
            squirrel_is = True

        add_image(SQUIRREL_IMAGE, squirrel_start_x, squirrel_start_y, SQUIRREL_WIDTH, SQUIRREL_HEIGHT, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                squirrel_eraser(screen, squirrel_start_x, squirrel_start_y)

                squirrel_is = False
        pygame.display.update()
    pygame.quit()


def add_image(img_path, x_pos, y_pos, width, height, screen):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x_pos, y_pos))


def squirrel_eraser(screen, squirrel_start_x, squirrel_start_y):
    width, height = SQUIRREL_WIDTH, SQUIRREL_HEIGHT
    blank_surface = pygame.Surface((width, height))
    blank_surface.fill(GREEN)
    screen.blit(blank_surface, (squirrel_start_x, squirrel_start_y))


main()
