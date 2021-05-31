import pygame
import random

from obj import Obj
from player import Player

# Init Screen
pygame.init()
window = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

# Create Objects
field = Obj(0, 0, "assets/field.png")
ball = Obj(617, 337, "assets/ball.png")
player1 = Player(50, 310, "assets/player1.png")
player2 = Player(1150, 310, "assets/player2.png")
score1 = Obj(500, 50, "assets/score/0.png")
score2 = Obj(710, 50, "assets/score/0.png")


# Define a function to start the game
def start():
    # (Re)Define Start Positions
    ball.reset()
    player1.reset()
    player2.reset()
    score1.reset()
    score2.reset()

    ball.dirX = -5
    ball.dirY = 1

    # Execute main game
    main()


# Define a function for the main game
def main():
    # Define a function to move player1 (Human)
    def move_player():
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and keys_pressed[pygame.K_s]:
            player1.dirY = 0
        elif keys_pressed[pygame.K_w]:
            player1.dirY = -5
        elif keys_pressed[pygame.K_s]:
            player1.dirY = 5
        else:
            player1.dirY = 0

        player1.y += player1.dirY

        if player1.y <= 0:
            player1.y = 0
        elif player1.y >= 575:
            player1.y = 575

    # Define a function to move player2 (Bot)
    def move_player2():
        if player2.y > ball.y - 46:
            player2.y -= 1.9
        else:
            player2.y += 1.9

        if player2.y >= 575:
            player2.y = 575
        elif player2.y <= 0:
            player2.y = 0

    # Define a function to move the ball and detect trigger points
    def move_ball():
        ball.x += ball.dirX
        ball.y += ball.dirY

        # Detects if the ball is in the same position of P1
        if 128 >= ball.x >= 112 and ball.dirX < 0:
            if player1.y - 33 < ball.y < player1.y + 179:
                # Changes direction in case of hitting the P1
                ball.dirX *= -1

                # Varies Y intensity on hit
                if ball.dirY > 0 and ball.y > player1.y + 116:
                    ball.dirY = random.uniform(-3.2, -1.2)
                elif ball.dirY > 0:
                    ball.dirY = random.uniform(1.5, 3.5)
                elif ball.dirY < 0 and ball.y < player1.y + 30:
                    ball.dirY = random.uniform(1.2, 3.2)
                else:
                    ball.dirY = random.uniform(-3.5, -1.5)
                if ball.dirY < 13:
                    # Increase ball speed each Player's touch
                    ball.dirX += 0.8

        # Same of P1 applies down here to P2
        if 1160 >= ball.x + 46 >= 1150 and ball.dirX > 0:
            if player2.y - 33 < ball.y < player2.y + 179:
                ball.dirX *= -1
                if ball.dirY > 0 and ball.y > player2.y + 116:
                    ball.dirY = random.uniform(-3.5, -1.5)
                elif ball.dirY > 0:
                    ball.dirY = random.uniform(1.2, 3.2)
                elif ball.dirY < 0 and ball.y < player2.y + 30:
                    ball.dirY = random.uniform(1.5, 3.5)
                else:
                    ball.dirY = random.uniform(-3.2, -1.2)
                if ball.dirX < -13:
                    ball.dirX -= 0.8

        # Detects if the ball hits a corner, then change its Y direction
        if 724 > ball.y + 46 > 720 and ball.dirY > 0:
            ball.dirY = random.randint(-2, -1)
        elif 0 > ball.y > -4 and ball.dirY < 0:
            ball.dirY = random.randint(1, 2)

        # Detects if a goal has been made, score and reset ball position
        if ball.x < -50 or ball.x > 1330:
            if ball.dirX > 0:
                score(1)
                ball.dirX = -5
            else:
                score(2)
                ball.dirX = 5
            ball.x = 617
            ball.y = 337
            ball.dirY = random.uniform(-2, 2)

    # Defines a function to score the goals
    def score(player):
        if player == 1:
            score1.value += 1
            score1.set_img("assets/score/{}.png".format(score1.value))
        if player == 2:
            score2.value += 1
            score2.set_img("assets/score/{}.png".format(score2.value))

    # Defines a function to draw every object in the screen
    def draw():
        window.blit(field.img, (field.x, field.y))
        window.blit(player1.img, (player1.x, player1.y))
        window.blit(player2.img, (player2.x, player2.y))
        window.blit(ball.img, (ball.x, ball.y))
        window.blit(score1.img, (score1.x, score1.y))
        window.blit(score2.img, (score2.x, score2.y))

    # Process the game in real time
    loop = True
    while score1.value < 3 and score2.value < 3 and loop:
        move_ball()
        move_player()
        move_player2()
        draw()
        pygame.display.update()

        # Exit the game if the close button is pressed
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                loop = False

        # Print the framerate in which the game is being played
        clock.tick(60)
        print('fps:', clock.get_fps())
    # Ends the game when a player scores 3 goals
    end()


# Define the ending screen
def end():
    loop = True
    while loop:
        window.blit(pygame.image.load("assets/win.png"), (315, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    start()
                    loop = False
                if event.key == pygame.K_s:
                    loop = False


# Start the Game
start()
