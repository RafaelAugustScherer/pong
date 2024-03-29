import pygame

from objects.window import Window
from objects.obj import Obj
from objects.player import Player
from objects.ball import Ball

# Init Screen
game = Window(1280, 720, "Pong")

# Create Objects
field = Obj(0, 0, "assets/field.png")
score1 = Obj(500, 50, "assets/score/0.png")
score2 = Obj(710, 50, "assets/score/0.png")
ball = Ball(617, 337, "assets/ball.png")
player1 = Player(94, 310, "assets/player.png")
player2 = Player(1150, 310, "assets/player.png")

objects = [field, player1, player2, score1, score2, ball]


# Define a function to start the game
def start():
    # (Re)Define Start Positions
    for obj in objects:
        obj.reset()

    # Execute the main game
    main()


# Define a function for the main game
def main():
    # Define a function to move player1 (Human)
    def move_player():
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            player1.move(-4)
        elif keys_pressed[pygame.K_s]:
            player1.move(4)

        player1.corner_block()

    # Define a function to move player2 (Bot)
    def move_player2():
        if player2.y > ball.y - 46:
            player2.move(-1.97)
        else:
            player2.move(1.97)

        player2.corner_block()

    # Define a function to move the ball and detect trigger points
    def move_ball():
        ball.move()

        # Detects if the ball is in the same position of P1
        if 114 >= ball.x >= 94 and ball.dirX < 0:
            if player1.y - 25 < ball.y < player1.y + 141:
                # Changes direction in case of hitting the P1
                ball.change_dir_x()

                # Varies Y intensity on hit
                if ball.dirY > 0 and ball.y + 30 > player1.y + 116:
                    ball.rand_dir_y(-3.5, -1.5)
                elif ball.dirY < 0 and ball.y < player1.y + 30:
                    ball.rand_dir_y(1.5, 3.5)
                elif ball.dirY > 0:
                    ball.rand_dir_y(1.2, 3.2)
                else:
                    ball.rand_dir_y(-3.2, -1.2)

                # Increase ball speed each Player's touch until 13
                ball.speed_ctrl()

        # Same of P1 applies down here to P2
        if 1170 >= ball.x + 30 >= 1150 and ball.dirX > 0:
            if player2.y - 25 < ball.y < player2.y + 146:
                ball.change_dir_x()
                if ball.dirY > 0 and ball.y + 30 > player2.y + 116:
                    ball.rand_dir_y(-3.5, -1.5)
                elif ball.dirY < 0 and ball.y < player2.y + 30:
                    ball.rand_dir_y(1.5, 3.5)
                elif ball.dirY > 0:
                    ball.rand_dir_y(1.2, 3.2)
                else:
                    ball.rand_dir_y(-3.2, -1.2)
                ball.speed_ctrl()

        # Detects if the ball hits a corner, then change its Y direction
        if 704 > ball.y + 30 > 700 and ball.dirY > 0:
            ball.rand_dir_y(-2, -1)
        elif 20 > ball.y > 16 and ball.dirY < 0:
            ball.rand_dir_y(1, 2)

        # Detects if a goal has been made, score and reset ball position
        if ball.x < -50 or ball.x > 1330:
            if ball.dirX > 0:
                score(1)
                ball.reset()
            else:
                score(2)
                ball.reset()
            ball.rand_dir_y(-2, 2)

    # Defines a function to score the goals
    def score(player):
        if player == 1:
            score1.value += 1
            score1.set_img("assets/score/{}.png".format(score1.value))
        if player == 2:
            score2.value += 1
            score2.set_img("assets/score/{}.png".format(score2.value))

    # Process the game in real time
    loop = True
    while score1.value < 3 and score2.value < 3 and loop:
        move_ball()
        move_player()
        move_player2()
        game.update(objects)
        pygame.display.update()

        # Exit the game if the close button is pressed
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                loop = False

    # Ends the game when a player scores 3 goals
    if loop:
        end()


# Define the ending screen
def end():
    loop = True
    ending = "assets/victory.png"
    if score2.value == 3:
        ending = "assets/defeat.png"

    while loop:
        game.window.blit(pygame.image.load(ending), (350, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    start()
                    loop = False
                if event.key == pygame.K_e:
                    loop = False


# Start the Game
start()
