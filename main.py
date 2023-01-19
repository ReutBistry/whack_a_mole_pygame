import pygame
import random
from constants import *


def main():
    pygame.init()
    # screen related staff
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    screen.fill(GREEN)

    # squirrel related staff
    squirrel = [(START_X_POS_SQU, START_Y_POS_SQU, START_X_POS_HOL),
                (START_X_POS_SQU + SPACE_X_POS_SQU, START_Y_POS_SQU, START_X_POS_HOL + SPACE_X_POS_HOL),
                (START_X_POS_SQU + 2 * SPACE_X_POS_SQU, START_Y_POS_SQU, START_X_POS_HOL + SPACE_X_POS_HOL * 2)]
    squirrel_is = False
    squirrel_direction = "up"

    # carrot related stuff
    carrot_count = 3

    # rating related staff
    rating_t = False
    rating_counter = 0

    finish = False
    while not finish:
        screen.fill(GREEN)

        for index in range(carrot_count):
            add_image(CARROT_IMAGE, START_X_POS_CAR + index * SPACE_X_POS_CAR, Y_POS_CAR, CARROT_WIDTH, CARROT_HEIGHT,
                      screen)

        for index in range(3):
            add_image(HOLE_IMAGE, START_X_POS_HOL + index * SPACE_X_POS_HOL, Y_POS_HOL, HOLE_WIDTH, HOLE_HEIGHT, screen)

        if not squirrel_is:
            squirrel_x, squirrel_y, hole_x = squirrel_xy(squirrel)
            squirrel_is = True
            over_the_squirrel(screen, squirrel_x)
            add_image(HALF_HOLE_IMAGE,  hole_x, MIDLINE, HALF_HOLE_WIDTH, HALF_HOLE_HEIGHT, screen)
        if not rating_t:
            rating_t = True
            rating(screen, FONT, 50, rating_counter)

            squirrel_dir, squirrel_is, squirrel_y = squirrel_movement(squirrel_y, squirrel_direction, SQUIRREL_MAX_Y, SQUIRREL_MIN_Y, SQUIRREL_MOVE_Y,
                                                             carrot_count, squirrel_is)
        else:
            squirrel_dir, squirrel_is, squirrel_y = squirrel_movement(squirrel_y, squirrel_direction, SQUIRREL_MAX_Y,
                        SQUIRREL_MIN_Y, SQUIRREL_MOVE_Y, carrot_count, squirrel_is)
            add_image(SQUIRREL_IMAGE, squirrel_x, squirrel_y, SQUIRREL_WIDTH, SQUIRREL_HEIGHT, screen)

        add_image(SQUIRREL_IMAGE, squirrel_x, squirrel_y, SQUIRREL_WIDTH, SQUIRREL_HEIGHT, screen)
        over_the_squirrel(screen, squirrel_x)
        add_image(HALF_HOLE_IMAGE,  hole_x, MIDLINE, HALF_HOLE_WIDTH, HALF_HOLE_HEIGHT, screen)
        rating(screen, FONT, 50, rating_counter)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                squirrel_dir, squirrel_is, squirrel_y = squirrel_movement(squirrel_y, squirrel_direction, SQUIRREL_MAX_Y, SQUIRREL_MIN_Y, SQUIRREL_MOVE_Y,
                                  carrot_count, squirrel_is)
                add_image(SQUIRREL_IMAGE, squirrel_x, squirrel_y, SQUIRREL_WIDTH, SQUIRREL_HEIGHT, screen)
                add_image(HALF_HOLE_IMAGE, hole_x, MIDLINE, HALF_HOLE_WIDTH, HALF_HOLE_HEIGHT, screen)

                squirrel_is = False
                rating_t = False
                rating_counter += 1

        if carrot_count == 0:
            pygame.quit()

        pygame.display.update()
    pygame.quit()


def add_image(img_path, x_pos, y_pos, width, height, screen):
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x_pos, y_pos))


def squirrel_xy(list_of_pos):
    squirrel_pos = random.choice(list_of_pos)
    squirrel_start_x = squirrel_pos[0]
    squirrel_start_y = squirrel_pos[1]
    hole_x = squirrel_pos[2]
    return squirrel_start_x, squirrel_start_y, hole_x


def over_the_squirrel(screen, square_x):
    square = pygame.Rect(square_x, MIDLINE, SQUARE_WIDTH, SQUARE_HEIGHT)
    pygame.draw.rect(screen, GREEN, square)


def rating(screen, font_name, size, massage):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(str(massage), True, WHITE)
    screen.blit(text, SCORE_TEXT_POS)


def squirrel_movement(squirrel_y, squirrel_dir, max_y, min_y, movement_speed, carrot_count, squirrel_is):
    if not squirrel_dir == "down":
        if not squirrel_y == min_y:
            squirrel_dir = "up"
            squirrel_y -= movement_speed
        else:
            squirrel_dir = "down"
    else:
        if not squirrel_y == max_y:
            squirrel_dir = "down"
            squirrel_y += movement_speed
        else:
            carrot_count -= 1
            squirrel_is = False
            squirrel_dir = "up"
            pygame.time.wait(50)
    return squirrel_dir, squirrel_is, squirrel_y

#             squirrel_movement(squirrel_y, squirrel_direction, SQUIRREL_MAX_Y, SQUIRREL_MIN_Y, SQUIRREL_MOVE_Y,
#                               carrot_count, squirrel_is)

main()

# fix the rating, make it update itself, and show
# the problem is because "rating counter"
