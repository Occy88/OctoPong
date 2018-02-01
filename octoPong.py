import pygame

import math
import sys
import random

#TO DO:
#: COLLISIONS
# Time based collision detection not framebased.
# possibly include broad phase followed by narrow with time if the above is not good enough


#PLAYER GUI AND ACCELERATION:
#make acceleration stop in the direction when key is released.
#make acceleration increase with time? possibly if it makes it better.

#add scores, and reset for ballse
#add ability to spawn balls during game.




# Define constants
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# dimensions
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
P_WIDTH = 20
# rate
SPEED = 60 * 60 * 24 * 12
# physics
G_CONST = 6.67408 * 10 ** -11
# player constants

PlAYER_SPEED = 20

PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

BALL_RADIUS=14

# game_constants


class Player:
    def _init_(self):
        self.velocityX=0
        self.velocityY=0
        self.x = 0
        self.y = 0
        self.width = P_WIDTH
        self.length=P_WIDTH*5
        self.id = 0
        self.r=0
        self.g=0
        self.b=0


    def draw(self,screen,fps):
        self.x+=self.velocityX/fps
        self.y+=self.velocityY/fps
        pygame.draw.rect(screen, (self.r,self.g,self.b), (self.x, self.y, self.width, self.length))
class Ball:
    def _init_(self):

        self.x = 0
        self.y = 0
        self.radius=BALL_RADIUS

        self.color = (255, 255, 255)
        self.velocityX=0
        self.velocityY=0
    def update(self,screen,fps):
        self.x+=self.velocityX/fps
        self.y+=self.velocityY/fps
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))
    def reset(self):
        n = random.randint(0, 1)
        if n == 1:
            self.velocityY = random.randint(-250, -200)
        else:
            self.velocityY = random.randint(200, 250)
        n = random.randint(0, 1)
        if n == 1:
            self.velocityX = random.randint(-250, -200)
        else:
            self.velocityX = random.randint(200, 250)

        self.x=SCREEN_WIDTH/2
        self.y=SCREEN_HEIGHT/2
        self.color=WHITE
def main():

    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2d Shooter")

    #init sets and stuff:
    ball_set=set()
    ball_Dset=set()
    player_dic={}

    #init time
    clock = pygame.time.Clock()
    seconds = 0
    seconds2 = 0
    #init ball?
    b1=Ball()
    b1.x=SCREEN_WIDTH/2
    b1.y=SCREEN_HEIGHT/2
    b1.radius=BALL_RADIUS
    b1.color=WHITE
    n=random.randint(0,1)
    if n==1:
        b1.velocityY=random.randint(-250,-200)
    else:
        b1.velocityY = random.randint(200,250)
    n = random.randint(0, 1)
    if n == 1:
        b1.velocityX = random.randint(-250, -200)
    else:
        b1.velocityX = random.randint(200, 250)

    ball_set.add(b1)
    #init players:
    p1=Player()
    p1.r=255
    p1.g=255
    p1.b=255
    p1.x=SCREEN_WIDTH*0.75
    p1.y=SCREEN_HEIGHT/2
    p1.velocityX=0
    p1.velocityY=0

    p1.length=P_WIDTH*5
    p1.width=P_WIDTH
    p2 = Player()
    p2.r = 255
    p2.g = 255
    p2.b = 255
    p2.velocityY=0
    p2.velocityX=0
    p2.x = SCREEN_WIDTH *0.25
    p2.y = SCREEN_HEIGHT / 2
    p2.length = P_WIDTH * 5
    p2.width = P_WIDTH
    player_dic={'p1':p1,'p2':p2}
    #functions:
    def up(player):
        player.velocityY-=PlAYER_SPEED

    def down(player):
        player.velocityY += PlAYER_SPEED

    def stop(player):
        player.velocityY *=0.1
        player.velocityX *=0.1

    def right(player):
        player.velocityX += PlAYER_SPEED


    def left(player):
        player.velocityX -= PlAYER_SPEED

    def getDist(player,ball):
        return(((player.x-ball.x)**2)+((player.y-ball.y)**2))
    def getxyDist(a,b):
        d=a-b
        return d
    def checkC(ball,player1,player2,num):
        dx1=getxyDist(ball.x,player1.x)
        dx2=getxyDist(ball.x,player2.x)
        dy1 =getxyDist(ball.y,player1.y)
        dy2=getxyDist(ball.y,player2.y)

        if ball.x>SCREEN_WIDTH-10 and ball.velocityX>0:
            ball.velocityX*=-1.01
            if num>1:
                ball_Dset.add(ball)
            ball.reset()
        if ball.x < 10 and  ball.velocityX<0:
           # print(str(ball.x) + ", " + str(ball.velocityX))
            ball.velocityX *= -1.01
            if num> 1:
                ball_Dset.add(ball)
            ball.reset()
        if ball.y>SCREEN_HEIGHT-10 and ball.velocityY>0:
            ball.velocityY*=-1.01
        if ball.y < 10 and ball.velocityY<0:
            ball.velocityY *= -1.01

      #  print(str(dy1)+", "+str(player1.length/2))
        if dx1>-ball.radius and dx1<player1.width/2and dy1<player1.length and dy1>0:
            ball.velocityX*=-1.01
            ball.velocityX+=player1.velocityX
            ball.x=ball.x-(ball.radius+dx1)
            ball.color = (0, 0, 255)
            player1.r = 50
            player1.g = 50

        if dx1>ball.radius/2 and dx1<player1.width+ball.radius  and dy1<player1.length and dy1>0 :
            ball.velocityX*=-1.01
            ball.velocityX+=player1.velocityX
            ball.x=ball.x+(player1.width+ball.radius-dx1)
            ball.color=(0,0,255)
            player1.r=50
            player1.g=50


        if dx2>-ball.radius and dx2<player2.width/2 and dy2<player2.length and dy2>0 :
            ball.velocityX*=-1.01
            ball.velocityX+=player2.velocityX
            ball.x = ball.x - (ball.radius + dx2)
            ball.color = (255, 0, 0)
            player2.b = 50
            player2.g = 50

        if dx2>ball.radius/2 and dx2<player2.width+ball.radius and dy2<player2.length and dy2>0:
            ball.velocityX*=-1.01
            ball.velocityX+=player2.velocityX
            ball.x = ball.x + (player2.width + ball.radius - dx2)
            ball.color = (255, 0, 0)
            player2.b = 50
            player2.g = 50


    while True:

        clock = pygame.time.Clock()
        seconds = 0
        seconds2 = 0
        game=True
        startTime = pygame.time.get_ticks()
        while game:
            screen.fill(BLACK)
            fps = clock.get_fps()
            ms = pygame.time.get_ticks() - startTime
            seconds = int(ms / 1000)

            if fps < 20:
                fps = 60

            # events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            # -----------PLAYER 1--------------------------
            keys = pygame.key.get_pressed()
            if keys[pygame.K_l]:
                player_dic['p1'].length=500
            if keys[pygame.K_k]:
                player_dic['p1'].length=player_dic['p2'].length
            if keys[pygame.K_UP]:
                up(player_dic['p1'])
            if (keys[pygame.K_UP] == False and player_dic['p1'].velocityY<0 ) or (player_dic['p1'].y <10 and player_dic['p1'].velocityY<0) :
                player_dic['p1'].velocityY =0
            if keys[pygame.K_DOWN]:
                down(player_dic['p1'])

            if (keys[pygame.K_DOWN] == False and player_dic['p1'].velocityY>0 )or( player_dic['p1'].y>SCREEN_HEIGHT-10 and player_dic['p1'].velocityY>0) :
                player_dic['p1'].velocityY =0
            if keys[pygame.K_RIGHT]:
                right(player_dic['p1'])
            if (keys[pygame.K_RIGHT] == False and player_dic['p1'].velocityX>0) or (player_dic['p1'].x<(SCREEN_WIDTH+10)/2 and player_dic['p1'].velocityX<0):
                player_dic['p1'].velocityX =0

            if keys[pygame.K_LEFT]:
                left(player_dic['p1'])
            if (keys[pygame.K_LEFT] == False and player_dic['p1'].velocityX<0) or ( player_dic['p1'].x>SCREEN_WIDTH-10 and player_dic['p1'].velocityX>0):
                player_dic['p1'].velocityX =0
            if keys[pygame.K_SPACE]:
                b1 = Ball()
                b1.x = SCREEN_WIDTH / 2
                b1.y = SCREEN_HEIGHT / 2
                b1.radius = BALL_RADIUS
                b1.color = WHITE
                b1.velocityY = random.randint(-100, 100)

                b1.velocityX = random.randint(-100, 100)
                ball_set.add(b1)

                # ---------PLYER 1----------BULLET-------
                # ---------------------------infinit ammo for now----------------------

            # -----------PLAYER 2--------------------------
            for b1 in ball_set:
                checkC(b1,player_dic['p1'],player_dic['p2'],len(ball_set))
                b1.update(screen,fps)
            ball_set-=ball_Dset
            if keys[pygame.K_e]:
                up(player_dic['p2'])
            if (keys[pygame.K_e] == False and player_dic['p2'].velocityY<0 ) or (player_dic['p2'].y <10 and player_dic['p2'].velocityY<0):
                player_dic['p2'].velocityY =0
            if keys[pygame.K_d]:
                down(player_dic['p2'])
            if( keys[pygame.K_d] == False and player_dic['p2'].velocityY > 0 )or (player_dic['p2'].y>SCREEN_HEIGHT-10 and player_dic['p2'].velocityY>0):
                player_dic['p2'].velocityY = 0

            if keys[pygame.K_s]:
                left(player_dic['p2'])
            if( keys[pygame.K_s] == False and player_dic['p2'].velocityX< 0) or (player_dic['p2'].x<10 and player_dic['p2'].velocityX<0):
                player_dic['p2'].velocityX = 0

            if keys[pygame.K_f]:
                right(player_dic['p2'])
            if( keys[pygame.K_f] == False and player_dic['p2'].velocityX> 0 )or (player_dic['p2'].x>(SCREEN_WIDTH-10)/2  and player_dic['p2'].velocityX>0):
                player_dic['p2'].velocityX = 0


            if player_dic['p1'].r<254:
                player_dic['p1'].r+=1
                player_dic['p1'].g += 1
            if player_dic['p2'].g<254:
                player_dic['p2'].b+=1
                player_dic['p2'].g += 1

            # for ball in ball_set:
            #     player_dic['p2'].y=ball.y-player_dic['p2'].length/2
            #     player_dic['p1'].y = ball.y-player_dic['p1'].length/2
            player_dic['p1'].draw(screen,fps)
            player_dic['p2'].draw(screen,fps)
            clock.tick(100)
            pygame.display.flip()

if __name__ == "__main__":
    main()
