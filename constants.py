# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# constants.py: a module containing only constant variables

# Game Info
NAME = "Big Buck Revolution"
FPS = 60.0

LARGE = True # True for big and False for small

# Game constants
if LARGE:
        SIZE = (1920, 1080)
        #SIZE = (1920, 1080)
        BOTTOM = 900

        # Arrow locations
        ARROW_LEFT = (100, -50)
        ARROW_DOWN = (300, -50)
        ARROW_UP = (500, -50)
        ARROW_RIGHT = (700, -50)

        # Input press offsets
        OFFSET = 120

        ARROW_SIZE = (150, 150)
        LOGO_BOTTOM = 400

        BBB_IMAGE_SIZE = (450, 450)
        BBB_IMAGE_POS = [(225, 235), (225, 700), (1695, 235), (1695, 700)]
        BBB_TEXT_POS = (960, 200)

        # Done controller
        NAME_BUTTON = (1380, 435)
        LEADERBOARD_TEXT_POS = (1530, 400)
        LEADERBOARD_CHANGE = 90
        WINNER_TEXT_POS = (640, 380)
        WINNER_TEXT_SCORE = (640, 410)

        # Game displays
        SCORE_BUTTON = (1920, 0)
        MULTIPLIER_BUTTON = (1920, 50)
        POINTS_RECEIVED_BUTTON = (1920, 100)
        ACCURACY_BUTTON = (1920, 150)

else:
        SIZE = (640, 480)
        BOTTOM = 400

        # Arrow locations
        ARROW_LEFT = (50, -50)
        ARROW_DOWN = (100, -50)
        ARROW_UP = (150, -50)
        ARROW_RIGHT = (200, -50)

        # Input press offsets
        OFFSET = 30

        ARROW_SIZE = (50, 50)
        LOGO_BOTTOM = 150

        BBB_IMAGE_SIZE = (150, 150)
        BBB_IMAGE_POS = [(80, 235), (80, 395), (560, 235), (560, 395)]
        BBB_TEXT_POS = (320, 200)

        # Done controller
        NAME_BUTTON = (450, 235)
        LEADERBOARD_TEXT_POS = (500, 210)
        LEADERBOARD_CHANGE = 30
        WINNER_TEXT_POS = (210, 180)
        WINNER_TEXT_SCORE = (210, 210)

        # Game display
        SCORE_BUTTON = (640, 0)
        MULTIPLIER_BUTTON = (640, 30)
        POINTS_RECEIVED_BUTTON = (640, 60)
        ACCURACY_BUTTON = (640, 90)


# States
STATE_MENU = 0
STATE_SINGLEPLAYER = 1
STATE_SELECTSCREEN = 2
STATE_DIFFICULTY = 3
STATE_EDITOR = 4
STATE_DONE = 5

# BBB Images
BBB_IMAGES = ["assets/BBB/BBB" + str(i) + ".jpg" for i in range(1, 5)]

# Colors
BLACK = 0,0,0
WHITE = 255, 255, 255
BLUE = 37, 137, 204

# LED Colors
LED_OFF         = 0, 0, 0
LED_RED         = 100, 0, 0
LED_ORANGE      = 100, 50, 0
LED_YELLOW      = 100, 100, 0
LED_LIME        = 50, 100, 0
LED_GREEN       = 0, 100, 0
LED_TEAL        = 0, 100, 50
LED_CYAN        = 0, 100, 100
LED_AZURE       = 0, 50, 100
LED_BLUE        = 0, 0, 100
LED_PURPLE      = 50, 0, 100
LED_MAGENTA     = 100, 0, 100
LED_PINK        = 100, 0, 50
LED_WHITE       = 100, 100, 100
LED_COLORS = {
        "off": LED_OFF,
        "red": LED_RED,
        "orange": LED_ORANGE,
        "yellow": LED_YELLOW,
        "lime": LED_LIME,
        "green": LED_GREEN,
        "teal": LED_TEAL,
        "cyan": LED_CYAN,
        "azure": LED_AZURE,
        "blue": LED_BLUE,
        "purple": LED_PURPLE,
        "magenta": LED_MAGENTA,
        "pink": LED_PINK,
        "white": LED_WHITE
}
COLORS = ["off", "red", "orange", "yellow", "lime", 
        "green", "teal", "cyan", "azure", "blue", "purple", "magenta", "pink", 
        "white"]

# Panic button input pin
IN_QUIT  = 26 #17
# Pressure Pad input pins
IN_LEFT  = 5 #22
IN_RIGHT = 19 #23
IN_DOWN  = 6 #27
IN_UP    = 13

# LED output pins
OUT_LEFT  = 12
OUT_RIGHT = 21
OUT_DOWN  = 16
OUT_UP    = 20
BACK = 26 #17 -- DUPLICATE of IN_QUIT
INPUT_PINS = [IN_LEFT, IN_RIGHT, IN_DOWN, IN_UP, BACK]

# Left LED output pins
R_LEFT  = 21
G_LEFT  = 20
B_LEFT  = 16

# Right LED output pins
R_RIGHT = 12
G_RIGHT = 25
B_RIGHT = 24

# Down LED output pin
R_DOWN = 4
G_DOWN = 17 #26
B_DOWN = 27 #6

# Up LED output pins
R_UP = 22 #5
G_UP = 23 #19
B_UP = 18

# All LED output pins
OUTPUT_PINS = [
        R_LEFT, G_LEFT, B_LEFT, 
        R_RIGHT, G_RIGHT, B_RIGHT, 
        R_DOWN, G_DOWN, B_DOWN,
        R_UP, G_UP, B_UP
]

# LED output pins for each button
LED_BUTTONS = {
        "left": (R_LEFT, G_LEFT, B_LEFT),
        "right": (R_RIGHT, G_RIGHT, B_RIGHT),
        "down": (R_DOWN, G_DOWN, B_DOWN),
        "up": (R_UP, G_UP, B_UP)
}

# Score
HIT_INCREMENT = 10
ALMOST_INCREMENT = 5
MISSED = 5

# Songs
SONGS = [("Do It Again", "doitagainbryce.json"), ("Down with the Sickness", "downlarge.json"), 
        ("S.O.M.P", "somp.json"), ("You Spin Me Round", "spin.json")]

# Leaderboard
LEADERBOARD_JSON = "jsons/leaderboard.json"
