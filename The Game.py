import random

# Define global constants
COLORS = ["R", "G", "B", "Y", "W", "O"]  # Red, Green, Blue, Yellow, White, Orange
TRIES = 10  # Maximum number of tries allowed
CODE_LENGTH = 4  # The length of the color code to guess

# Function to generate a random code consisting of the valid colors
def generate_code():
    """
    Generate a random code of colors.
    
    Returns:
    - list: A list containing randomly selected colors from the predefined set.
    """
    code = random.choices(COLORS, k=CODE_LENGTH)  # Efficient way to generate random choices
    return code

# Function to prompt the user to guess the code
def guess_code():
    """
    Get a valid color code guess from the user.
    
    Returns:
    - list: A list containing the user's guess for the color code.
    """
    while True:
        guess = input(f"Enter your guess (space-separated, {CODE_LENGTH} colors): ").upper().split()

        # Validate guess length
        if len(guess) != CODE_LENGTH:
            print(f"Invalid input! You must guess exactly {CODE_LENGTH} colors.")
            continue

        # Validate that all colors in the guess are valid
        invalid_colors = [color for color in guess if color not in COLORS]
        if invalid_colors:
            print(f"Invalid colors: {', '.join(invalid_colors)}. Allowed colors are {COLORS}. Try again!")
        else:
            break

    return guess

# Function to check how many positions are correct and how many colors are misplaced
def check_code(guess, real_code):
    """
    Check the guessed code against the real code.
    
    Parameters:
    - guess (list): The user's guessed color code.
    - real_code (list): The actual color code to be guessed.
    
    Returns:
    - tuple: (correct_pos, incorrect_pos), where:
      - correct_pos (int): Number of colors in the correct positions.
      - incorrect_pos (int): Number of correct colors in the wrong positions.
    """
    color_counts = {}  # Dictionary to track the count of each color in the real code
    correct_pos = 0  # Number of colors in the correct position
    incorrect_pos = 0  # Number of correct colors in the wrong position

    # First pass: Find correct positions
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
        else:
            if real_color not in color_counts:
                color_counts[real_color] = 0
            color_counts[real_color] += 1

    # Second pass: Find misplaced colors
    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

# Main function to run the game
def game():
    """
    Run the Mastermind game loop.
    """
    print(f"Welcome to Mastermind! You have {TRIES} tries to guess the code.")
    print(f"The valid colors are: {', '.join(COLORS)}.")

    code = generate_code()  # Generate the secret code
    # print(code)  # Uncomment this for debugging purposes to see the code

    for attempts in range(1, TRIES + 1):  # Start attempts from 1 for user-friendly numbering
        guess = guess_code()  # Get the player's guess
        correct_pos, incorrect_pos = check_code(guess, code)  # Check the guess

        if correct_pos == CODE_LENGTH:  # Check if the guess is entirely correct
            print(f"Congratulations! You guessed the code in {attempts} attempts.")
            break

        # Provide feedback after each attempt
        print(f"Attempt {attempts}/{TRIES}: Correct Positions: {correct_pos}, Incorrect Positions: {incorrect_pos}")

    else:
        # If the player exhausts all attempts
        print(f"Sorry, you ran out of tries. The correct code was: {' '.join(code)}.")

# Entry point of the program
if __name__ == "__main__":
    game()
