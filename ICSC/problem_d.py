# ----------- Word Search Puzzle -------
import random
import string

# ANSI color codes
COLOR = '\033[93m' # Yellow text
RESET = '\033[0m'

def create_crossword(words):
    size = 10
    grid = [['' for _ in range(size)] for _ in range(size)]
    highlight_positions = set()

    directions = [
        (0, 1), # horizontal
        (1, 0), # vertical
        (1, 1), # diagonal down-right
        (-1, 1), # diagonal up-right
    ]
