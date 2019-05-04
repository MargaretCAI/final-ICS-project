import pygame
import random
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WINNING_SCORE = 100

PLAY_TIME = 30

PLAYER_SPEED = 5

# set the max speed the AI can move - changing this value can increase/decrease difficulty
AI_SPEED = 5

# set the max speed the ball can move - changing this value can increase/decrease difficulty
BALL_SPEED = 7

# set the size of the ball - changing this value can increase/decrease difficulty
BALL_SIZE = 10


# Draws the timer on the screen, showing the amount of time left to the player
def draw_timer(screen, x, y, time_left):
    font = pygame.font.Font(None, 36)  # Choose the font for the text
    text = font.render("Time Left = " + str(time_left), 1, WHITE)  # Create the text
    screen.blit(text, (x, y))  # Draw the text on the screen


# Draws the game over box on the screen for when we have collided
# With the AI player or the game runs out of time, we have added message_1 and message_2
# paramaters to the function definition so we can set which message to display to the user
def draw_game_over(screen, message_1, message_2):
    pygame.draw.rect(screen, WHITE, (150, 200, 400, 100), 0)  # Draw a white box for the text to sit in

    font = pygame.font.Font(None, 36)  # Choose the font for the text
    text = font.render(message_1, 1, BLACK)  # Create the text for "GAME OVER"
    screen.blit(text, (170, 220))  # Draw the text on the screen
    text = font.render(message_2, 1, BLACK)  # Create the text for "You hit the other player"
    screen.blit(text, (170, 260))  # Draw the text on the screen

    font = pygame.font.Font(None, 28)  # Make the font a bit smaller for this bit
    text = font.render("Press P to play again. Press E to exit the game.", 1,
                       WHITE)  # Create text for instructions on what to do now
    screen.blit(text, (100, 350))  # Draw the text on the screen


# Create the text used to display the score and draw it on the screen
def draw_score(screen, x, y, score):
    font = pygame.font.Font(None, 36)  # Choose the font for the text
    text = font.render("Score = " + str(score), 1, WHITE)  # Create the text
    screen.blit(text, (x, y))  # Draw the text on the screen


# This function draws the ball
def draw_ball(screen, x, y):
    pygame.draw.circle(screen, GREEN, [x, y], BALL_SIZE, 0)


background_image = 'background.jpg'  # file name of the background image


# This function draws the background on the screen
# max_x and max_y are the maximum x and y values of the screen
def draw_background(screen, file_name):
    myimage = pygame.image.load("11.png")
    imagerect = myimage.get_rect()
    screen.blit(myimage, imagerect)


# This function draws the smaller user-controllable stick figure on the screen
# Colour and scale paramaters have been added to the stick figure so that different varieties of stick figure
# Can be produced whilst using the same function, with the scale being used
# to adjust the size of the stick figure, and the colour being used to set the colour of the stick figures body.
def draw_stick_figure(screen, x, y, colour, scale):

    pygame.draw.ellipse(screen, BLACK, [int(1 * scale) + x, y, int(10 * scale), int(10 * scale)], 0)

    pygame.draw.line(screen, BLACK, [int(5 * scale) + x, int(17 * scale) + y],
                     [int(10 * scale) + x, int(27 * scale) + y], int(2 * scale))

    pygame.draw.line(screen, BLACK, [int(5 * scale) + x, int(17 * scale) + y], [x, int(27 * scale) + y], int(2 * scale))

    pygame.draw.line(screen, colour, [int(5 * scale) + x, int(17 * scale) + y],
                     [int(5 * scale) + x, int(7 * scale) + y], int(2 * scale))

    pygame.draw.line(screen, colour, [int(5 * scale) + x, int(7 * scale) + y],
                     [int(9 * scale) + x, int(17 * scale) + y], int(2 * scale))
    pygame.draw.line(screen, colour, [int(5 * scale) + x, int(7 * scale) + y],
                     [int(1 * scale) + x, int(17 * scale) + y], int(2 * scale))


# This function ensures that the number entered is between the range of the min and max values (inclusive).
# If the number is outside of this range, we return the closest allowed value. I.e. if the max was 10 and the number
# entered was 12, 10 would be returned as this is the maximum value allowed
def keep_in_range(number, min_no, max_no):
    if (number < min_no):
        return min_no
    elif (number > max_no):
        return max_no
    else:
        return number


# Setup
pygame.init()
screen_size = [700, 500]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game_fight")


game_over = False
game_ended = False
done = False
clock = pygame.time.Clock()

# Counts the number of times the screen has been redrawn, incremented for every pygame.display.flip()
step = 0
score = 0

# Stores the step at which the last score was made
# Starts with a value of -100 so we can score on the first step of the game
last_score_step = -100
# hide the mouse
pygame.mouse.set_visible(0)
# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 300
y_coord = 1

# AI Players current position
ai_x_coord = 300
ai_y_coord = 300

# The AI players last position
old_ai_x_coord = 300
old_ai_y_coord = 300

ai_moves = (-AI_SPEED, 0, AI_SPEED)  # A list of moves that the ai player can make each turn


ai_x_direction = 0
ai_y_direction = 0


ball_x_coord = 300
ball_y_coord = 300

old_ball_x_coord = 300
old_ball_y_coord = 300

# Controls the different moves the ball can make, change these values
# To change the ball speed
ball_moves = (-BALL_SPEED, BALL_SPEED)

ball_x_directon = 0
ball_y_direction = 0

# Stores the start time of the game in milliseconds
start_time = pygame.time.get_ticks()
print(start_time)

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                x_speed = PLAYER_SPEED
            elif event.key == pygame.K_UP:
                y_speed = -PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                y_speed = PLAYER_SPEED

            # If the game_over or the game_ended boolean is true, then we are on the game over screen
            # Players therefore have multiple options for what to do on these screens
            if (game_over or game_ended):
                # If they press p, they have decided to play again, therefore we reset all the variables
                # and set game_over to False so the player can try again
                if event.key == pygame.K_p:
                    score = 0
                    step = 0
                    last_score_step = 0
                    x_coord = 300
                    y_coord = 1

                    ai_x_coord = 300
                    ai_y_coord = 300

                    game_over = False
                    game_ended = False

                    start_time = pygame.time.get_ticks()  # reset the start time
                # If they press e, they have decided to quit, so we exit the game
                elif event.key == pygame.K_e:
                    sys.exit()  # call sys.exit() to close the window and exit the game

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # --- Game Logic

    # Check if Games time is up (it has been more than 30 seconds from when we started the game)
    if (start_time + (PLAY_TIME * 1000) <= pygame.time.get_ticks()):
        # If the time is up, set the boolean game_ended to True
        # so we can display the correct game over screen
        game_ended = True

        # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    if (x_coord < 0):
        x_coord = 0

    if (y_coord < 0):
        y_coord = 0

    # Adjust the x and y co-ordinates to ensure that the stick figure is kept on the screen and can't
    # travel off of it
    x_coord = keep_in_range(x_coord, 0, screen_size[
        0] - 10)  # We adjust the upper limit of our allowed range to match the stick figures width
    y_coord = keep_in_range(y_coord, 0, screen_size[
        1] - 27)  # We adjust the upper limit of our allowed range to match the stick figures height

    # MOVE THE AI PLAYER
    # Every 30 steps (screen draws) we change the direction the ai player is moving in
    # This makes the movement of the ai player look more realistic. This works because
    # step % 30 is gives the remained when the value step is divided by 30, which will only
    # occur every 30 steps. You can experiment with changing this value and seeing how the ai
    # character moves
    if (step % 30 == 0):
        ai_x_direction = random.choice(ai_moves)
        ai_y_direction = random.choice(ai_moves)

    # Update the old ai co-ordinate values
    old_ai_x_coord = ai_x_coord
    old_ai_y_coord = ai_y_coord

    # move the ai player in the chosen direction
    ai_x_coord = ai_x_coord + ai_x_direction
    ai_y_coord = ai_y_coord + ai_y_direction

    # Limit the ai character to ensure it stays on the screen
    ai_x_coord = keep_in_range(ai_x_coord, 0, screen_size[0] - 20)
    ai_y_coord = keep_in_range(ai_y_coord, 0, screen_size[1] - 54)

    # If our x co-ordinate has not changed, then we could have collided with a screen edge so we reverse the direction
    # This helps to keep the movement looking natural by preventing the ai player from repeatedly
    # moving along the edge of the screen
    if (ai_x_coord == old_ai_x_coord):
        ai_x_direction *= -1;
    # the same is true for the y co-ordinate
    if (ai_y_coord == old_ai_y_coord):
        ai_y_direction *= -1;

    # MOVE THE BALL
    # Randomly move the ball basically in the same way as the ai player
    # Every 50 steps update the ball direction with a new random one
    if (step % 50 == 0):
        ball_x_direction = random.choice(ball_moves)
        ball_y_direction = random.choice(ball_moves)

    # update the old ball coord
    old_ball_x_coord = ball_x_coord
    old_ball_y_coord = ball_y_coord

    # Move the ball in the chosen direction
    ball_x_coord += ball_x_direction
    ball_y_coord += ball_y_direction

    ball_x_coord = keep_in_range(ball_x_coord, 0, screen_size[0])
    ball_y_coord = keep_in_range(ball_y_coord, 0, screen_size[1])

    # If our x co-ordinate has not changed, then we could have collided with a screen edge so we reverse the direction
    # This helps to keep the movement looking natural by preventing the ai player from repeatedly
    # moving along the edge of the screen
    if (ball_x_coord == old_ball_x_coord):
        ball_x_direction *= -1;
    # the same is true for the y co-ordinate
    if (ball_y_coord == old_ball_y_coord):
        ball_y_direction *= -1;

    # Tests if the ball has collided with the player
    if (ball_x_coord - BALL_SIZE <= x_coord + 5) and (ball_x_coord + BALL_SIZE >= x_coord - 5) and (
            ball_y_coord - BALL_SIZE <= y_coord + 27) and (ball_y_coord + BALL_SIZE >= y_coord):
        # Register the score if it is more than 10 steps after the last score
        # This is necessary as the ball has a habit of double bouncing against the player
        # Meaning that we register multiple hits with only one true collision
        if (last_score_step + 10 < step):
            score += 10;  # increment the score
            # reverse the ball direction
            ball_x_directon *= -1
            ball_y_direction *= -1
            last_score_step = step  # record the step at which this score is made

            print(score)

    # Test if the player has collided with the ai
    if (x_coord - 5 <= ai_x_coord + 10) and (x_coord + 5 >= ai_x_coord) and (y_coord - 3 <= ai_y_coord + 54) and (
            y_coord + 27 >= ai_y_coord):
        print("COLLIDED WITH AI")
        game_over = True  # set the game over boolean to True so we can trigger the end of the game

    # --- Drawing Code

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)  # erase the previous screen
    draw_background(screen, background_image)  # draw the background

    # If the game isn't over. we draw the game
    if not game_over and not game_ended:
        draw_stick_figure(screen, x_coord, y_coord, RED, 1)  # draw the user controlled stick figure on the screen
        draw_stick_figure(screen, ai_x_coord, ai_y_coord, BLUE, 2)  # draw the ai controlled stick figure on the screen

        draw_ball(screen, ball_x_coord, ball_y_coord)

        # Draw the score on the screen
        draw_score(screen, 550, 450, score)

        # Calculate how much time is left by subtracting the current time
        # from the start time, and then this value from the maximum allowed time (30 seconds).
        # As these times are stored in milliseconds, we then
        # divide by 1000 to convert to seconds, and convert the result to an integer
        # value so that only whole seconds are shown.
        time_left = pygame.time.get_ticks() - start_time  # find out how much time has passed since the start of the game
        time_left = time_left / 1000  # Convert this time from milliseconds to seconds
        time_left = PLAY_TIME - time_left  # Find out how much time is remaining by subtracting total time from time thats passed
        time_left = int(time_left)  # Convert this value to an integer
        draw_timer(screen, 50, 450, time_left)  # Once we have calculated how much time is left, draw the timer

    # Else if the game is over (i.e. because we collided with the ai player)
    # We print the game over screen
    elif game_over:
        draw_game_over(screen, "YOU LOSE, SORRY TRY AGAIN", "You hit the other player!")  # draw the game over screen
    # Else if the game has ended because the player has run out of time, we print a different game over
    # screen
    elif game_ended:
        # If the score is >= 100, the player has one the game
        if score >= WINNING_SCORE:
            draw_game_over(screen, "YOU WIN THE GAME!", "Final Score: " + str(score))
        # Otherwise they didn't win, so we draw a you lose screen
        else:
            draw_game_over(screen, "YOU LOSE, SORRY TRY AGAIN", "You didn't score enough points")
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    step += 1


    clock.tick(60)


pygame.quit()
