# ####################### PART 1 ####################### #
# Window size
import pygame.font

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

# Colors
GREEN = (152, 199, 72)
WHITE = (255, 255, 255)
BLACK = (0,0,0)


# Images
CARROT_IMAGE = "images\\carrot.png"
HOLE_IMAGE = "images\\hole.png"
SQUIRREL_IMAGE = "images\\squirrel.png"

# Images size
CARROT_WIDTH = 512 / 8
CARROT_HEIGHT = 512 / 8
HOLE_WIDTH = 822 / 3
HOLE_HEIGHT = 303 / 3
SQUIRREL_WIDTH = 512 / 3
SQUIRREL_HEIGHT = 512 / 3

# Positions
# ( formula: [START_X_POS + SPACE_X_POS * index, Y_POS] )
START_X_POS_SQU = 100   # squirrel
SPACE_X_POS_SQU = 300
START_Y_POS_SQU = 250

START_X_POS_CAR = 700   # carrot
SPACE_X_POS_CAR = 50
Y_POS_CAR = 40

START_X_POS_HOL = 50    # hole
SPACE_X_POS_HOL = 300
Y_POS_HOL = 300

# Game settings
CARROTS_NUM_START = 3

# ####################### PART 2 ####################### #
# Colors
WHITE = (255, 255, 255)

# Images
HALF_HOLE_IMAGE = "images\\half_hole.png"

# Images size
HALF_HOLE_WIDTH = 822 / 3
HALF_HOLE_HEIGHT = 156 / 6

# Text position
SCORE_TEXT_POS = [100, 45]
END_TEXT_POS = [300, 170]
FONT = pygame.font.get_fonts()
# Positions
MIDLINE = 375  # The line where the squirrel disappears

# square pos
SQUARE_START_X_POS = START_X_POS_HOL
SPACE_X_POS_SQUARE = SPACE_X_POS_HOL
SQUARE_Y_POS = 350
SQUARE_HEIGHT = 606 / 3
SQUARE_WIDTH = HOLE_WIDTH
# ####################### PART 3 ####################### #
# Positions
SQUIRREL_MAX_Y = 380
SQUIRREL_MIN_Y = 220

# Game settings
SQUIRREL_MOVE_Y = 4


