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

    # end text related staff
    end_text = "GAME OVER"

    finish = False
    while not finish:
        if carrot_count > 0:
            screen.fill(GREEN)

            for index in range(carrot_count):
                add_image(CARROT_IMAGE, START_X_POS_CAR + index * SPACE_X_POS_CAR, Y_POS_CAR, CARROT_WIDTH, CARROT_HEIGHT,
                          screen)

            for index in range(3):
                add_image(HOLE_IMAGE, START_X_POS_HOL + index * SPACE_X_POS_HOL, Y_POS_HOL, HOLE_WIDTH, HOLE_HEIGHT, screen)

            if not squirrel_is:
                squirrel_x, squirrel_y, hole_x = squirrel_xy(squirrel)
                squirrel_is = True
                square_drawer(screen, squirrel_x)
                add_image(HALF_HOLE_IMAGE,  hole_x, MIDLINE, HALF_HOLE_WIDTH, HALF_HOLE_HEIGHT, screen)
            if not rating_t:
                rating_t = True
                rating(screen, FONT, 50, rating_counter)

                squirrel_direction, squirrel_is, squirrel_y, carrot_count = squirrel_movement(squirrel_y, squirrel_direction, SQUIRREL_MAX_Y, SQUIRREL_MIN_Y, SQUIRREL_MOVE_Y,
                                                                 carrot_count, squirrel_is)
            else:
                squirrel_direction, squirrel_is, squirrel_y, carrot_count = squirrel_movement(squirrel_y, squirrel_direction, SQUIRREL_MAX_Y,
                            SQUIRREL_MIN_Y, SQUIRREL_MOVE_Y, carrot_count, squirrel_is)
                add_image(SQUIRREL_IMAGE, squirrel_x, squirrel_y, SQUIRREL_WIDTH, SQUIRREL_HEIGHT, screen)

            add_image(SQUIRREL_IMAGE, squirrel_x, squirrel_y, SQUIRREL_WIDTH, SQUIRREL_HEIGHT, screen)
            square_drawer(screen, squirrel_x)
            add_image(HALF_HOLE_IMAGE,  hole_x, MIDLINE, HALF_HOLE_WIDTH, HALF_HOLE_HEIGHT, screen)
            rating(screen, FONT, 50, rating_counter)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_loc(squirrel_x, squirrel_y, SQUIRREL_WIDTH, SQUIRREL_HEIGHT):
                        squirrel_direction, squirrel_is, squirrel_y, carrot_count = squirrel_movement(squirrel_y,
                            squirrel_direction, SQUIRREL_MAX_Y, SQUIRREL_MIN_Y, SQUIRREL_MOVE_Y, carrot_count, squirrel_is)

                        add_image(SQUIRREL_IMAGE, squirrel_x, squirrel_y, SQUIRREL_WIDTH, SQUIRREL_HEIGHT, screen)
                        add_image(HALF_HOLE_IMAGE, hole_x, MIDLINE, HALF_HOLE_WIDTH, HALF_HOLE_HEIGHT, screen)
                        squirrel_is = False
                        rating_t = False
                        rating_counter += 1
                        squirrel_direction = "up"
                        pygame.display.update()


        else:
            end_title(screen, FONT, 90, end_text)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True

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


def square_drawer(screen, square_x):
    square = pygame.Rect(square_x, MIDLINE, SQUARE_WIDTH, SQUARE_HEIGHT)
    pygame.draw.rect(screen, GREEN, square)


def rating(screen, font_name, size, massage):
    font = pygame.font.SysFont(font_name, size)
    text = font.render(str(massage), True, WHITE)
    screen.blit(text, SCORE_TEXT_POS)


def squirrel_movement(squirrel_y, squirrel_dir, max_y, min_y, movement_speed, carrot_count, squirrel_is):
    if squirrel_dir == "up":
        if squirrel_y > min_y:
            squirrel_dir = "up"
            squirrel_y -= movement_speed
        else:
            squirrel_dir = "down"
    else:
        if squirrel_y < max_y:
            squirrel_dir = "down"
            squirrel_y += movement_speed
        else:
            carrot_count -= 1
            squirrel_is = False
            squirrel_dir = "up"
            pygame.time.wait(100)
            squirrel_y = START_Y_POS_SQU
    return squirrel_dir, squirrel_is, squirrel_y, carrot_count


def mouse_loc(button_x, button_y, button_width, button_height):
    mouse_pos = pygame.mouse.get_pos()
    if ((button_x <= mouse_pos[0] <= button_x + button_width) and (button_y <= mouse_pos[1] <= button_y + button_height)):
        return True


def end_title(screen, font_name, size, massage):
    square = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.draw.rect(screen, GREEN, square)

    font = pygame.font.SysFont(font_name, size)
    text = font.render(str(massage), True, WHITE)
    screen.blit(text, END_TEXT_POS)


main()
