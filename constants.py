# ber72, jij8, rrs234
# Thursday Afternoon Lab
# ECE 5725 Final Project
# 
# constants.py: a module containing only constant variables

# Game Info
NAME = "Big Buck Revolution"
SIZE = (640, 480)
FPS = 60.0

# States
STATE_MENU = 0
STATE_SINGLEPLAYER = 1
STATE_SELECTSCREEN = 2
STATE_DIFFICULTY = 3
STATE_EDITOR = 4
STATE_DONE = 5

# Game constants
BOTTOM = 400
PROTRAIT = 200

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
IN_QUIT  = 26

# Pressure Pad input pins
IN_LEFT  = 5
IN_RIGHT = 19
IN_DOWN  = 6
IN_UP    = 13

# LED output pins
OUT_LEFT  = 12
OUT_RIGHT = 21
OUT_DOWN  = 16
OUT_UP    = 20
BACK = 26
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
G_DOWN = 17
B_DOWN = 27

# Up LED output pins
R_UP = 22
G_UP = 23
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

# Arrow locations
ARROW_LEFT = (50, -50)
ARROW_DOWN = (100, -50)
ARROW_UP = (150, -50)
ARROW_RIGHT = (200, -50)

# Input press offsets
OFFSET = 30

# Score
HIT_INCREMENT = 10
ALMOST_INCREMENT = 5
MISSED = 5

# Songs
SONGS = [("Do It Again", "doitagain.json"), ("Down with the Sickness", "example.json"), 
        ("S.O.M.P", "nextLevel.json")]

# Leaderboard
LEADERBOARD_JSON = "jsons/leaderboard.json"
