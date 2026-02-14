# Configuration constants for SpeedyHighway.432

# Game settings
SCREEN_WIDTH = 800  # width of the game window
SCREEN_HEIGHT = 600 # height of the game window
FPS = 60            # frames per second

# Color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
PLAYER_START_X = SCREEN_WIDTH // 2  # starting x position
PLAYER_START_Y = SCREEN_HEIGHT - 100  # starting y position
PLAYER_SPEED = 5                # speed of player’s car
PLAYER_HEALTH = 100             # initial health value

# Game physics
GRAVITY = 0.5                  # gravity effect
FRICTION = 0.1                 # friction coefficient

# Levels
LEVEL_COUNT = 10               # total number of levels
LEVEL_TIME_LIMIT = 300          # time limit for each level in seconds

# Score settings
SCORE_INCREMENT = 10            # points awarded for each checkpoint
SCORE_PER_SECOND = 1            # points awarded per second

# Other constants
MAX_CARS = 5                   # maximum number of cars on the screen at once
CAR_SPAWN_RATE = 60            # how often new cars spawn (in frames)
