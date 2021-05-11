import pygame
import random

# Init Screen
pygame.init()
window = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Pong")

# Load Assets
field = pygame.image.load("assets/field.png")
ball = pygame.image.load("assets/ball.png")
player1 = pygame.image.load("assets/player1.png")
player2 = pygame.image.load("assets/player2.png")
score1_img = score2_img = pygame.image.load("assets/score/0.png")

# Define Global Game Vars
ball_x = 0
ball_y = 0
ball_dir_x = 0
ball_dir_y = 0

player1_y = 0
player2_y = 0
player1_moveup = False
player1_movedown = False

score1 = 0
score2 = 0


# Start the Game
def start():
    global ball_x
    global ball_y
    global ball_dir_x
    global ball_dir_y
    global player1_y
    global player2_y
    global player1_moveup
    global player1_movedown
    global score1
    global score2
    global score1_img
    global score2_img

    # (Re)Define Start Positions
    ball_x = 617
    ball_y = 337
    ball_dir_x = -5
    ball_dir_y = 1

    player1_y = 310
    player2_y = 310

    # (Re)Define Movement Properties
    player1_moveup = False
    player1_movedown = False

    # (Re)Start Score System
    score1 = 0
    score2 = 0
    score1_img = score2_img = pygame.image.load("assets/score/0.png")

    main()


def main():

    global player1_moveup
    global player1_movedown

    global score1
    global score2

    def move_player():
        global player1_y
        if player1_moveup:
            player1_y -= 5
        if player1_movedown:
            player1_y += 5

        if player1_y <= 0:
            player1_y = 0
        elif player1_y >= 575:
            player1_y = 575

    def move_player2():
        global player2_y

        if player2_y > ball_y - 46:
            player2_y -= 1.9
        if player2_y < ball_y - 46:
            player2_y += 1.9

        if player2_y >= 575:
            player2_y = 575
        elif player2_y <= 0:
            player2_y = 0

    def move_ball():
        global ball_x
        global ball_y
        global ball_dir_x
        global ball_dir_y
        global score1
        global score2
        global score1_img
        global score2_img

        ball_x += ball_dir_x
        ball_y += ball_dir_y

        # Detects if ball is in the same position of P1
        if 125 >= ball_x >= 115:
            if ball_y < player1_y + 146:
                if ball_y + 35 > player1_y:
                    # Changes direction in case of hitting the P1
                    ball_dir_x *= -1
                    # Varies Y intensity on hit
                    if ball_dir_y > 0 and ball_y > player1_y + 116:
                        ball_dir_y = random.uniform(-3.2, -1.2)
                    elif ball_dir_y > 0:
                        ball_dir_y = random.uniform(1.5, 3.5)
                    elif ball_dir_y < 0 and ball_y < player1_y + 30:
                        ball_dir_y = random.uniform(1.2, 3.2)
                    else:
                        ball_dir_y = random.uniform(-3.5, -1.5)
                    if ball_dir_x < 13:
                        # Increase ball speed each Player's touch
                        ball_dir_x += 0.8

        # Same of P1 applies down here to P2
        if 1115 >= ball_x >= 1105:
            if ball_y < player2_y + 146:
                if ball_y + 35 > player2_y:
                    ball_dir_x *= -1
                    if ball_dir_y > 0 and ball_y > player2_y + 116:
                        ball_dir_y = random.uniform(-3.5, -1.5)
                    elif ball_dir_y > 0:
                        ball_dir_y = random.uniform(1.2, 3.2)
                    elif ball_dir_y < 0 and ball_y < player2_y + 30:
                        ball_dir_y = random.uniform(1.5, 3.5)
                    else:
                        ball_dir_y = random.uniform(-3.2, -1.2)
                    if ball_dir_x > -13:
                        ball_dir_x -= 0.8

        # Detects if ball hits a corner, then change its Y direction
        if 684 > ball_y > 674:
            ball_dir_y = random.randint(-2, -1)
        elif 0 > ball_y > -10:
            ball_dir_y = random.randint(1, 2)

        # Detects if a goal has been made
        if ball_x < -50 or ball_x > 1330:
            if ball_x < -50:
                score(2)
                ball_dir_x = -5
                ball_dir_y = random.uniform(-2, 2)
            elif ball_x > 1330:
                score(1)
                ball_dir_x = 5
                ball_dir_y = random.uniform(-2, 2)

            ball_x = 617
            ball_y = 337
            ball_dir_x *= -1
            ball_dir_y *= -1

    def score(player):
        global score1
        global score2
        global score1_img
        global score2_img

        if player == 1:
            score1 += 1
            score1_img = pygame.image.load("assets/score/{}.png".format(score1))
        if player == 2:
            score2 += 1
            score2_img = pygame.image.load("assets/score/{}.png".format(score2))

    # Prepare Scenario
    def draw():
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))

    def end():
        window.blit(pygame.image.load("assets/win.png"), (315, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    start()
                    return False
                if event.key == pygame.K_s:
                    return False
        return True

    # Process Game in Real Time
    loop = True
    while score1 < 3 and score2 < 3 and loop:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                loop = False
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_w:
                    player1_moveup = True
                if evt.key == pygame.K_s:
                    player1_movedown = True
            if evt.type == pygame.KEYUP:
                if evt.key == pygame.K_w:
                    player1_moveup = False
                if evt.key == pygame.K_s:
                    player1_movedown = False

        draw()
        move_ball()
        move_player()
        move_player2()
        pygame.display.update()
    draw()

    while loop:
        loop = end()


start()
