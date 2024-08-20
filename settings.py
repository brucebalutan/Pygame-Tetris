import pygame as pg

# 2d Engine
vec = pg.math.Vector2

# Setting constants
FPS = 60
FIELD_COLOUR = (50, 40, 30)
BG_COLOUR = (25, 90, 120)

FONT_PATH = 'assets/font/FFFFORWA.TTF'

TILE_SIZE = 35
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

# OFFSET POSITION START
INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
# ANIMATION OFFSET
ANIM_TIME_INTERVAL = 150
FAST_ANIM_TIME_INTERVAL = 15
# Movement directions and vectors
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}


# Tetrominoes dictionary
TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
# 0 = Orange, 1 = Yellow, 2 = Red, 3 = Purple, 4 = Blue, 5 = Green

COLORS = {
    'T': 'orange',
    'O': 'yellow',
    'J': 'red',
    'L': 'purple',
    'I': 'blue',
    'S': 'green',
    'Z': 'cyan'
}