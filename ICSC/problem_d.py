# ----------- Word Search Puzzle -------
import random
import string

# ANSI color codes
COLOR = '\033[93m' # Yellow text
RESET = '\033[0m'

def create_crossword(words):
    size = 10
    grid = [['' for _ in range(size)] for _ in range(size)] # Create a 10 x 10 grid initalized with empty strings
    highlight_positions = set() # Store positions of characters that belong to placed words for highlighting

    # Define possible directions for placing words:
    # (row change, column change) - horizontal, vertical, diagonal down-right, diagonal up-right
    directions = [
        (0, 1), # horizontal
        (1, 0), # vertical
        (1, 1), # diagonal down-right
        (-1, 1), # diagonal up-right
    ]

    # Check if a word can be placed at a given starting position and direction
    def can_place(word, row, col, dr, dc):
        for i in range(len(word)):
            r, c = row + dr*i, col + dc *i  # Calculate position of each character
            if r < 0 or r >= size or c < 0 or c >= size:  # Check if position is within grid bounds
                return False
            if grid[r][c] not in ('', word[i]):  # Check for conflict with exisiting letters
                return False
            return True  # Word can be placed safely
    
    def place_word(word):
        attempts = 100
        while attempts > 0:
            dr, dc = random.choice(directions)
            row = random.randint(0, size-1)
            col = random.randint(0, size-1)
            if can_place(word, row, col, dr, dc):
                for i in range(len(word)):
                    r, c = row + dr*i, col + dc *i
                    grid[r][c] = word[i]
                    highlight_positions.add((r, c))
                return True
            attempts -= 1
        return False
    
    for word in words:
        place_word(word.lower())

    # Fill remaining cells with random letters
    for r in range(size):
        for c in range(size):
            if grid[r][c]== '':
                grid[r][c]  = random.choice(string.ascii_lowercase)
    
    # Print with highlights
    for r in range(size):
        row_output = ''
        for c in range(size):
            char = grid[r][c]
            if(r, c) in highlight_positions:
                row_output += f"{COLOR}{char}{RESET} "
            else:
                row_output += f"{char} "
            
        print(row_output)

# Example usage
words = (input("Enter words: ").strip().split(','))
create_crossword(words)

