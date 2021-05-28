import pygame
import random

from obj import Obj

# Init Screen
pygame.init()
window = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

# Create Objects
field = Obj(0, 0, "assets/field.png")
ball = Obj(617, 337, "assets/ball.png")
player1 = Obj(50, 310, "assets/player1.png")
player2 = Obj(1150, 310, "assets/player2.png")
score1_img = Obj(500, 50, "assets/score/0.png")
score2_img = Obj(710, 50, "assets/score/0.png")

player1_moveup = False
player1_movedown = False

score1 = 0
score2 = 0


# Start the Game
def start():
    global player1_moveup
    global player1_movedown
    global score1
    global score2

    # (Re)Define Start Positions
    ball.reset()
    player1.reset()
    player2.reset()
    score1_img.setImg("assets/score/0.png")
    score2_img.setImg("assets/score/0.png")

    ball.setDirX(-5)
    ball.setDirY(1)

    # (Re)Define Movement Properties
    player1_moveup = False
    player1_movedown = False

    # (Re)Start Score System
    score1 = 0
    score2 = 0

    main()


def main():
    global player1_moveup
    global player1_movedown

    global score1
    global score2

    def move_player():
        if player1_moveup:
            player1.setY(player1.getY() - 5)
        if player1_movedown:
            player1.setY(player1.getY() + 5)

        if player1.getY() <= 0:
            player1.setY(0)
        elif player1.getY() >= 575:
            player1.setY(575)

    def move_player2():
        if player2.getY() > ball.getY() - 46:
            player2.setY(player2.getY() - 1.9)
        else:
            player2.setY(player2.getY() + 1.9)

        if player2.getY() >= 575:
            player2.setY(575)
        elif player2.getY() <= 0:
            player2.setY(0)

    def move_ball():
        global score1
        global score2

        ball.setX(ball.getX() + ball.getDirX())
        ball.setY(ball.getY() + ball.getDirY())

        # Detects if ball is in the same position of P1
        if 125 >= ball.getX() >= 115:
            if ball.getY() < player1.getY() + 146:
                if ball.getY() + 35 > player1.getY():
                    # Changes direction in case of hitting the P1
                    ball.setDirX(ball.getDirX() * -1)
                    # Varies Y intensity on hit
                    if ball.getDirY() > 0 and ball.getY() > player1.getY() + 116:
                        ball.setDirY(random.uniform(-3.2, -1.2))
                    elif ball.getDirY() > 0:
                        ball.setDirY(random.uniform(1.5, 3.5))
                    elif ball.getDirY() < 0 and ball.getY() < player1.getY() + 30:
                        ball.setDirY(random.uniform(1.2, 3.2))
                    else:
                        ball.setDirY(random.uniform(-3.5, -1.5))
                    if ball.getDirY() < 13:
                        # Increase ball speed each Player's touch
                        ball.setDirY(ball.getDirY() + 0.8)

        # Same of P1 applies down here to P2
        if 1115 >= ball.getX() >= 1105:
            if ball.getY() < player2.getY() + 146:
                if ball.getY() + 35 > player2.getY():
                    ball.setDirX(ball.getDirX() * - 1)
                    if ball.getDirY() > 0 and ball.getY() > player2.getY() + 116:
                        ball.setDirY(random.uniform(-3.5, -1.5))
                    elif ball.getDirY() > 0:
                        ball.setDirY(random.uniform(1.2, 3.2))
                    elif ball.getDirY() < 0 and ball.getY() < player2.getY() + 30:
                        ball.setDirY(random.uniform(1.5, 3.5))
                    else:
                        ball.setDirY(random.uniform(-3.2, -1.2))
                    if ball.getDirX() < -13:
                        ball.setDirX(ball.getDirX() - 0.8)

        # Detects if ball hits a corner, then change its Y direction
        if 684 > ball.getY() > 674:
            ball.setDirY(random.randint(-2, -1))
        elif 0 > ball.getY() > -10:
            ball.setDirY(random.randint(1, 2))

        # Detects if a goal has been made
        if ball.getX() < -50 or ball.getX() > 1330:
            if ball.getX() < -50:
                score(2)
                ball.setDirX(-5)
                ball.setDirY(random.uniform(-2, 2))
            elif ball.getX() > 1330:
                score(1)
                ball.setDirX(5)
                ball.setDirY(random.uniform(-2, 2))

            ball.setX(617)
            ball.setY(337)
            ball.setDirX(ball.getDirX() * -1)
            ball.setDirY(ball.getDirY() * -1)

    def score(player):
        global score1
        global score2

        if player == 1:
            score1 += 1
            score1_img.setImg("assets/score/{}.png".format(score1))
        if player == 2:
            score2 += 1
            score2_img.setImg("assets/score/{}.png".format(score2))

    # Prepare Scenario
    def draw():
        window.blit(field.getImg(), (field.getX(), field.getY()))
        window.blit(player1.getImg(), (player1.getX(), player1.getY()))
        window.blit(player2.getImg(), (player2.getX(), player2.getY()))
        window.blit(ball.getImg(), (ball.getX(), ball.getY()))
        window.blit(score1_img.getImg(), (score1_img.getX(), score1_img.getY()))
        window.blit(score2_img.getImg(), (score2_img.getX(), score2_img.getY()))

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

        move_ball()
        move_player()
        move_player2()
        draw()
        pygame.display.update()
        clock.tick(60)
        print('fps:', clock.get_fps())
    draw()

    while loop:
        loop = end()


start()
