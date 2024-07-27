import tkinter as tk
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_SPEED = 5

# Create the main window
root = tk.Tk()
root.title("Catch the Falling Balls")

# Create the canvas
canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg='white')
canvas.pack()

# Create the paddle
paddle = canvas.create_rectangle(
    (SCREEN_WIDTH - PADDLE_WIDTH) // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10,
    (SCREEN_WIDTH + PADDLE_WIDTH) // 2, SCREEN_HEIGHT - 10,
    fill='blue'
)

# Create the ball
ball = canvas.create_oval(
    random.randint(0, SCREEN_WIDTH - BALL_SIZE), 0,
    random.randint(0, SCREEN_WIDTH - BALL_SIZE) + BALL_SIZE, BALL_SIZE,
    fill='red'
)

# Initialize score
score = 0
score_text = canvas.create_text(10, 10, anchor='nw', text=f"Score: {score}", fill='black', font=('Arial', 16))

# Paddle movement function
def move_paddle(event):
    x = event.x
    canvas.coords(paddle, x - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10,
                  x + PADDLE_WIDTH // 2, SCREEN_HEIGHT - 10)

# Ball movement function
def move_ball():
    global score  # Declare score as global to modify it
    canvas.move(ball, 0, BALL_SPEED)
    ball_coords = canvas.coords(ball)
    paddle_coords = canvas.coords(paddle)

    # Check for collision with paddle
    if (paddle_coords[0] < ball_coords[2] < paddle_coords[2] and
        paddle_coords[1] < ball_coords[3] < paddle_coords[3]):
        score += 1
        canvas.itemconfig(score_text, text=f"Score: {score}")
        canvas.coords(ball, random.randint(0, SCREEN_WIDTH - BALL_SIZE), 0,
                      random.randint(0, SCREEN_WIDTH - BALL_SIZE) + BALL_SIZE, BALL_SIZE)
    # Check if ball falls below the screen
    elif ball_coords[3] > SCREEN_HEIGHT:
        canvas.create_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, text=f"Game Over! Final Score: {score}", font=('Arial', 24), fill='black')
        root.after(2000, root.quit)  # Close the game after 2 seconds

    root.after(50, move_ball)  # Continue moving the ball

# Bind mouse movement to the paddle movement
canvas.bind('<Motion>', move_paddle)

# Start the ball movement
move_ball()

# Run the main loop
root.mainloop()



