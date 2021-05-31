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
score1 = Obj(500, 50, "assets/score/0.png")
score2 = Obj(710, 50, "assets/score/0.png")

player1_moveup = False
player1_movedown = False


# Start the Game
def start():
    global player1_moveup
    global player1_movedown

    # (Re)Define Start Positions
    ball.reset()
    player1.reset()
    player2.reset()
    score1.reset()
    score2.reset()

    ball.dirX = -5
    ball.dirY = 1

    # (Re)Define Movement Properties
    player1_moveup = False
    player1_movedown = False

    main()


def main():
    global player1_moveup
    global player1_movedown

    def move_player():
        if player1_moveup:
            player1.y -= 5
        if player1_movedown:
            player1.y += 5

        if player1.y <= 0:
            player1.y = 0
        elif player1.y >= 575:
            player1.y = 575

    def move_player2():
        if player2.y > ball.y - 46:
            player2.y -= 1.9
        else:
            player2.y += 1.9

        if player2.y >= 575:
            player2.y = 575
        elif player2.y <= 0:
            player2.y = 0

    def move_ball():
        ball.x += ball.dirX
        ball.y += ball.dirY

        # Detects if ball is in the same position of P1
        if 125 >= ball.x >= 115:
            if ball.y < player1.y + 146:
                if ball.y + 35 > player1.y:
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
                        ball.dirY += 0.8

        # Same of P1 applies down here to P2
        if 1115 >= ball.x >= 1105:
            if ball.y < player2.y + 146:
                if ball.y + 35 > player2.y:
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

        # Detects if ball hits a corner, then change its Y direction
        if 684 > ball.y > 674:
            ball.dirY = random.randint(-2, -1)
        elif 0 > ball.y > -10:
            ball.dirY = random.randint(1, 2)

        # Detects if a goal has been made
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

    def score(player):
        if player == 1:
            score1.value += 1
            score1.set_img("assets/score/{}.png".format(score1.value))
        if player == 2:
            score2.value += 1
            score2.set_img("assets/score/{}.png".format(score2.value))

    # Prepare Scenario
    def draw():
        window.blit(field.img, (field.x, field.y))
        window.blit(player1.img, (player1.x, player1.y))
        window.blit(player2.img, (player2.x, player2.y))
        window.blit(ball.img, (ball.x, ball.y))
        window.blit(score1.img, (score1.x, score1.y))
        window.blit(score2.img, (score2.x, score2.y))

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
    while score1.value < 3 and score2.value < 3 and loop:
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
