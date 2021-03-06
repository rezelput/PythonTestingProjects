import math
import numpy as np

WIDTH = 1280
HEIGHT = 720
SCALE = 1.0
REAL_WIDTH = WIDTH // SCALE
REAL_HEIGHT = HEIGHT // SCALE
HALF_REAL_WIDTH = REAL_WIDTH // 2
HALF_REAL_HEIGHT = REAL_HEIGHT // 2
RESOLUTION = (REAL_WIDTH, REAL_HEIGHT)
RESOLUTION_RATIO = REAL_WIDTH / REAL_HEIGHT
FOV = math.pi / 4
Z_DIST = REAL_HEIGHT / math.tan(FOV / 2)

EPSILON = 0.007
MAX_DEPTH = 13
MAX_STEPS = 100.0

light_pos = (4.0, 3.0, 4.0)
cam_pos = np.array([0.0, 2.5, 9.0])

# colors
DARKGRAY = (15, 15, 15)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLUE_SKY = (0, 189, 255)
BROWN = (140, 50, 20)
DARKBLUE = (0, 0, 70)
DGRAY = (30, 30, 30)
DARKRED = (80, 0, 0)
DARKGREEN = (6, 51, 9)
DARKYELLOW = (155, 135, 12)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
LIGHTBLUE = (100, 100, 225)
LIGHTGRAY = (150, 150, 150)
LIGHTGREEN = (100, 255, 100)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)