import pygame
import image
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#define variables and Booleans needed
x_speed = 0
y_speed = 0

level_1 = True
level_2 = False
level_3 = False
level_4 = False
level = 0

gameover = False
itemexsist = False
itemtime = 0
randitem = 0
itemlevel = 0
pygame.init()
characterwall = True
notmoveable = True
invincible = False
invincibletime = 0
walltime = 0
itemkill = 0
listofwalls=[[]]

LOST = False
WIN = False

#create a window for the game
screen = pygame.display.set_mode((1200,800))
#have a caption for the game 
pygame.display.set_caption("My Game")
#create a list for all the sprites
all_sprites_list = pygame.sprite.Group()


class Character(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/5001.png").convert_alpha() #link to the image 
        self.rect = self.image.get_rect() # have a hitbox acording to the image 
        self.rect.x = x
        self.rect.y = y
        self.xspeed = 5 #vertical and horizontal speed for the character
        self.yspeed = 5
        self.health = 10 # the health of the character
        
    #update method        
    def update(self,y_speed,x_speed):
        self.rect.y += self.yspeed # allow the character to move in all directions 
        self.rect.x += self.xspeed
        self.yspeed = y_speed # work with items to change the speed of the character
        self.xspeed = x_speed
        if self.health <= 0: #kill the character when the health is 0
            self.kill()
            
    #health bar of the character        
    def draw(self,win):
        pygame.draw.rect(win, RED, (self.rect.x, self.rect.y - 20, 50, 10))
        pygame.draw.rect(win, GREEN , (self.rect.x, self.rect.y - 20, 50 - (5 * (10 - self.health)), 10))

#location of the character        
char = Character(500,500)



        
class Wall(pygame.sprite.Sprite):

    def __init__(self,x,y):        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/wall.png").convert_alpha()#image
        self.rect = self.image.get_rect()
        self.rect.x = x*50
        self.rect.y = y*50

Walls = pygame.sprite.Group()

class powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/full heart.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.found = False #for spawning
        
    #method to create items    
    def create(self,master):
        while self.found == False:#see if a position is found
            rand1 = random.randint(1,15)    # random y grid
            rand2 = random.randint(1,23)    # x grid
            if master[rand1][rand2] =="0":  #check the text file
                self.rect.y = rand1 * 50    #y coodinate
                self.rect.x = rand2 * 50    #x coordinate
                self.found = True      

class Bullet_up(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/tear.png").convert_alpha()# image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 1
        
    def update(self):
        self.rect.y -= 10 #move by itself

class Bullet_down(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/tear.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 1
 
    def update(self):

        self.rect.y += 10

class Bullet_left(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/tear.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 1
 
    def update(self):
        self.rect.x -= 10
      
class Bullet_right(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/tear.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 1
     
    def update(self):
        self.rect.x += 10
            
class Mob1s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/031.00.00.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.xspeed = 2
        self.yspeed = 2
        self.health = 3
        self.xdirection = '' #direction of moving
        self.ydirection = ''
        self.found = False
        
    def update(self,x_character, y_character):
        #movement of the mob , follows the character
        if self.health > 0:
            if x_character - self.rect.x > 0:
                self.rect.x += self.xspeed
                self.xdirection = "right"
            if x_character - self.rect.x < 0:
                self.rect.x -= self.xspeed
                self.xdirection = "left"
            if y_character - self.rect.y > 0:
                self.rect.y += self.yspeed
                self.ydirection = "down"
            if y_character - self.rect.y < 0:
                self.rect.y -= self.yspeed
                self.ydirection = "up"
        if self.health <= 0:
            self.kill()

    #generation of the mob        
    def create(self,master):
        while self.found == False:
            rand1 = random.randint(1,15)
            rand2 = random.randint(1,23)
            if master[rand1][rand2] =="0":
                self.rect.y = rand1 * 50
                self.rect.x = rand2 * 50
                self.found = True          
            
class Mob2s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/010.01.00.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.xspeed = 2
        self.yspeed = 2
        self.timeCount = 0
        self.health = 2
        self.xdirection = ''
        self.ydirection = ''
        self.found = False

    def update(self,x_character, y_character):
        if self.health > 0:
            #movement of the mob , keep in distance with the character
            if  x_character - self.rect.x > 200:
                self.rect.x += self.xspeed
                self.xdirection = "right"
            if x_character - self.rect.x < -200:
                self.rect.x -= self.xspeed
                self.xdirection = "left"
            if y_character - self.rect.y > 200:
                self.rect.y += self.yspeed
                self.ydirection = "down"
            if y_character - self.rect.y < -200:
                self.ydirection = "up"
                self.rect.y -= self.yspeed
            if  x_character - self.rect.x > 0 and x_character - self.rect.x < 200:
                self.rect.x -= self.xspeed
                self.xdirection = "left"
            if x_character - self.rect.x < 0 and x_character - self.rect.x > -200:
                self.rect.x += self.xspeed
                self.xdirection = "right"
            if  y_character - self.rect.y > 0 and y_character - self.rect.y < 200:
                self.rect.y -= self.yspeed
                self.ydirection = "up"
            if y_character - self.rect.y < 0 and y_character - self.rect.y > -200:
                self.rect.y += self.yspeed
                self.ydirection = "down"
            #shooting bullets in the approximate direction of the character    
            if self.timeCount == 40:
                self.timeCount = 0
                if x_character - self.rect.x > 0:
                    mobbulletright = Bullet_right(self.rect.x,self.rect.y)
                    mobBullets.add(mobbulletright)
                    Bullets.add(mobbulletright)
                if x_character - self.rect.x < 0:
                    mobbulletleft = Bullet_left(self.rect.x,self.rect.y)
                    mobBullets.add(mobbulletleft)
                    Bullets.add(mobbulletleft)
                if y_character - self.rect.y > 0:
                    mobbulletdown = Bullet_down(self.rect.x,self.rect.y)
                    mobBullets.add(mobbulletdown)
                    Bullets.add(mobbulletdown)
                if y_character - self.rect.y < 0:
                    mobbulletup = Bullet_up(self.rect.x,self.rect.y)
                    mobBullets.add(mobbulletup)
                    Bullets.add(mobbulletup)
            else:
                self.timeCount = self.timeCount + 1
                
        if self.health <= 0:
            self.kill()

    def create(self,master):
        while self.found == False:
            rand1 = random.randint(1,15)
            rand2 = random.randint(1,23)
            if master[rand1][rand2] =="0":
                self.rect.y = rand1 * 50
                self.rect.x = rand2 * 50
                self.found = True          

class Mob3s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.xspeed = 3
        self.yspeed = 3
        self.health = 3
        self.found = False
        
    #movement of the mob , follows the character    
    def update(self,x_character, y_character):
        if self.health > 0:
            if x_character - self.rect.x > 0:
                self.rect.x += self.xspeed
                self.xdirection = "right"
            if x_character - self.rect.x < 0:
                self.rect.x -= self.xspeed
                self.xdirection = "left"
            if y_character - self.rect.y > 0:
                self.rect.y += self.yspeed
                self.ydirection = "down"
            if y_character - self.rect.y < 0:
                self.rect.y -= self.yspeed
                self.ydirection = "up"
        if self.health <= 0:
            self.kill()
            
    def create(self,master):
        while self.found == False:
            rand1 = random.randint(1,15)
            rand2 = random.randint(1,23)
            if master[rand1][rand2] =="0":
                self.rect.y = rand1 * 50
                self.rect.x = rand2 * 50
                self.found = True          

class Mob4s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.xspeed = 1
        self.yspeed = 1
        self.health = 3
        self.found = False
        
    #movement of the mob , follows the character    
    def update(self,x_character, y_character):
        if self.health > 0:
            if x_character - self.rect.x > 0:
                self.rect.x += self.xspeed
                self.xdirection = "right"
            if x_character - self.rect.x < 0:
                self.rect.x -= self.xspeed
                self.xdirection = "left"
            if y_character - self.rect.y > 0:
                self.rect.y += self.yspeed
                self.ydirection = "down"
            if y_character - self.rect.y < 0:
                self.rect.y -= self.yspeed
                self.ydirection = "up"
                
        if self.health <= 0:            
            self.kill()
            # does damage tothe character when it dies
            if x_character - self.rect.x < 7:
                char.health = char.health -1
            elif y_character - self.rect.y < 7:
               char.health = char.health -1
            
    def create(self,master):
        while self.found == False:
            rand1 = random.randint(1,15)
            rand2 = random.randint(1,23)
            if master[rand1][rand2] =="0":
                self.rect.y = rand1 * 50
                self.rect.x = rand2 * 50
                self.found = True          
#BOSS
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/Boss.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 400
        self.health = 20
        self.timeCount = 0
        
    #shoot bullets in all 4 directions
    def update(self,x_character, y_character):
        if self.timeCount == 30:
            self.timeCount = 0
            mobbulletright = Bullet_right(self.rect.x,self.rect.y)
            mobBullets.add(mobbulletright)
            Bullets.add(mobbulletright)
            mobbulletleft = Bullet_left(self.rect.x,self.rect.y)
            mobBullets.add(mobbulletleft)
            Bullets.add(mobbulletleft)
            mobbulletdown = Bullet_down(self.rect.x,self.rect.y)
            mobBullets.add(mobbulletdown)
            Bullets.add(mobbulletdown)
            mobbulletup = Bullet_up(self.rect.x,self.rect.y)
            mobBullets.add(mobbulletup)
            Bullets.add(mobbulletup)
        else:
            self.timeCount = self.timeCount + 1
        if self.health == 0:
            self.kill()
    
#creation of groups for later use
Mobs = pygame.sprite.Group()
Mob1 = pygame.sprite.Group()
Mob2 = pygame.sprite.Group()
Mob3 = pygame.sprite.Group()
Mob4 = pygame.sprite.Group()
Bullets = pygame.sprite.Group()
myBullets = pygame.sprite.Group()
mobBullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

#add char to the list
all_sprites_list.add(char)

#font and content of the end screen
font = pygame.font.SysFont("comicsansms", 72)
lose = font.render("YOU LOSE!", True, BLUE)
win = font.render("YOU WIN!", True, BLUE)


    
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
# -------- Main Program Loop -----------

while not done:
    # --- Main event loop

    # if the game is ended

    #lost and display you lost
    if LOST == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(RED)
        screen.blit(lose,(600 - lose.get_width() // 2, 400 - lose.get_height() // 2))
    #win and display you win
    elif WIN == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(RED)
        screen.blit(win,(600 - win.get_width() // 2, 400 - win.get_height() // 2))
    # see if the window is closed
    elif gameover == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
            
            # first level
            if level_1 == True:
                level_1 = False
                level = level + 1
                master=[]
                # spawm mobs
                mob1 = Mob1s()
                mob1.rect.x = 100
                mob1.rect.y = 100
                mob1.health = 4
                mob2 = Mob2s()
                mob2.rect.x = 700
                mob2.rect.y = 700
                mob2.health = 3
                mob3 = Mob3s()
                mob3.rect.x = 300
                mob3.rect.y = 300
                mob3.health = 2
                mob4 = Mob4s()
                mob4.rect.x = 600
                mob4.rect.y = 600
                mob4.health = 1
                Mob1.add(mob1)
                Mob2.add(mob2)
                Mob3.add(mob3)
                Mob4.add(mob4)
                Mobs.add(Mob1,Mob2,Mob3,Mob4)
                
                # read file and creat the level
                with open("Level1.txt","r") as f:
                    for Y in range (0,16):
                        a = f.readline()
                        mylist=[]
                        for X in range (0,24):
                            mylist.append(a[X])
                            if  a[X] == "w":
                                myWall = Wall(X,Y)
                                Walls.add(myWall)
                                all_sprites_list.add(myWall)
                        master.append(mylist)
            # second level
            if len(Mobs) == 0 and level == 1:
                for w in Walls:
                    w.kill()
                char.kill()
                char = Character(500,500)
                all_sprites_list.add(char)
                char.health = health
                level_2 = True

                
            if level_2 == True:
                level_2 = False
                level = level + 1
                # spawm mobs
                mob1 = Mob1s()
                mob1.create(master)
                mob1.health = 6
                mob2 = Mob2s()
                mob2.create(master)
                mob2.health = 4
                mob3 = Mob3s()
                mob3.create(master)
                mob3.health = 3
                mob4 = Mob4s()
                mob4.create(master)
                mob4.health = 1
                Mob1.add(mob1)
                Mob2.add(mob2)
                Mob3.add(mob3)
                Mob4.add(mob4)
                Mobs.add(Mob1,Mob2,Mob3,Mob4)
                
                # read file and creat the level
                with open("Level2.txt","r") as f:
                    for Y in range (0,16):
                        a = f.readline()
                        for X in range (0,24):
                            if  a[X] == "w":
                                myWall = Wall(X,Y)
                                Walls.add(myWall)
                                all_sprites_list.add(myWall)
            
            # third level
            if len(Mobs) == 0 and level == 2:
                for w in Walls:
                    w.kill()
                char.kill()
                char = Character(500,500)
                all_sprites_list.add(char)
                char.health = health
                level_3 = True
                
            if level_3 == True :
                level_3 = False
                level = level + 1
                # spawm mobs
                mob1 = Mob1s()
                mob1.create(master)
                mob1.health = 8
                mob2 = Mob2s()
                mob2.create(master)
                mob2.health = 7
                mob3 = Mob3s()
                mob3.create(master)
                mob3.health = 4
                mob4 = Mob4s()
                mob4.create(master)
                mob4.health = 1
                Mob1.add(mob1)
                Mob2.add(mob2)
                Mob3.add(mob3)
                Mob4.add(mob4)
                Mobs.add(Mob1,Mob2,Mob3,Mob4)
                
                # read file and creat the level
                with open("Level3.txt","r") as f:
                    for Y in range (0,16):
                        a = f.readline()
                        for X in range (0,24):
                            if  a[X] == "w":
                                myWall = Wall(X,Y)
                                Walls.add(myWall)
                                all_sprites_list.add(myWall)
                                
            if len(Mobs) == 0 and level == 3:
                for w in Walls:
                    w.kill()
                char.kill()
                char = Character(500,500)
                all_sprites_list.add(char)
                char.health = health
                level_4 = True

            # Boss level creation                
            if level_4 == True:
                level_4 = False
                level = level + 1
                boss = Boss()
                Mobs.add(boss)
                
                # read file and creat the level
                with open("Level4.txt","r") as f:
                    for Y in range (0,16):
                        a = f.readline()
                        for X in range (0,24):
                            if  a[X] == "w":
                                myWall = Wall(X,Y)
                                Walls.add(myWall)
                                all_sprites_list.add(myWall)
            # WIN                    
            if len(Mobs) == 0 and level ==4:
                WIN = True

            #time count for creating an item 
            if itemtime ==120:
                mypowerup = powerup()
                mypowerup.create(master)
                powerups.add(mypowerup)
                all_sprites_list.add(mypowerup)
                itemkill = itemkill + 1
                itemtime = itemtime + 1
            elif itemtime < 120:
                itemtime = itemtime + 1

            #time count for despawn item  and the despawn of items            
            if itemtime == 121:
                itemkill = itemkill + 1
            if itemkill == 90:
                mypowerup.kill()
                itemtime = 0
                itemkill = 0

           # items and their functions
            if pygame.sprite.spritecollide(char,powerups, True):
                randitem = random.randint(0,5)
                itemlevel = random.randint(1,3)
                if randitem == 0:           # speed boost
                    if itemlevel == 1:      
                        char.xspeed = 6
                        char.yspeed = 6
                    if itemlevel == 2:
                        char.xspeed = 7
                        char.yspeed = 7
                    if itemlevel == 3:
                        char.xspeed = 8
                        char.yspeed = 8
                if randitem == 1:           # health
                    if itemlevel == 1:
                        char.health = char.health + 1
                    if itemlevel == 2:
                        char.health = char.health + 2
                    if itemlevel == 3 :
                        char.health = char.health + 3
                if randitem == 2:           # go through walls
                    characterwall = False
                    if itemlevel == 1:
                        walltime = 300
                    if itemlevel == 2:
                        walltime = 600
                    if itemlevel == 3:
                        walltime = 900
                if randitem == 3:           # invincible
                    invincible = True
                    if itemlevel == 1:
                        invincibletime = 300
                    if itemlevel == 2:
                        invincibletime = 600
                    if itemlevel == 3:
                        invincibletime = 900
                if randitem == 4:           # more damage
                    for b in myBullets:
                        if itemlevel == 1 or itemlevel == 2:
                            b.damage = 2
                        if itemlevel == 3:
                            b.damage = 3
                mypowerup.kill()
                itemtime = 0
                
                    
            #used to allow the character to move     
            if event.type == pygame.KEYDOWN:
                
                # upwards
                if event.key == pygame.K_w:
                    if char.rect.x//50 == xposition and (master[yposition-1][xposition]) != "w" and char.rect.x == xposition * 50:
                        y_speed = -5
                    if char.rect.x//50 < xposition and (master[yposition-1][xposition]) != "w" and (master[yposition-1][xposition-1]) != "w":
                        y_speed = -5
                    if char.rect.x > xposition * 50 and (master[yposition-1][xposition]) != "w" and (master[yposition-1][xposition+1]) != "w":
                        y_speed = -5

                # downwards
                if event.key == pygame.K_s:
                    if char.rect.x//50 == xposition and (master[yposition+1][xposition]) != "w" and char.rect.x == xposition * 50:
                        y_speed = 5
                    if char.rect.x//50 < xposition and (master[yposition+1][xposition]) != "w" and (master[yposition+1][xposition-1]) != "w":
                        y_speed = 5
                    if char.rect.x > xposition * 50 and (master[yposition+1][xposition]) != "w" and (master[yposition+1][xposition+1]) != "w":
                        
                        y_speed = 5
                # left
                if event.key == pygame.K_a:
                    if char.rect.y//50 == yposition and (master[yposition][xposition-1]) != "w" and char.rect.y == yposition * 50:
                        x_speed = -5
                    if char.rect.y//50 < yposition and (master[yposition][xposition-1]) != "w" and (master[yposition+1][xposition-1]) != "w":
                        x_speed = -5
                    if char.rect.y > yposition * 50 and (master[yposition][xposition-1]) != "w" and (master[yposition-1][xposition-1]) != "w":
                        x_speed = -5
                # right        
                if event.key == pygame.K_d:
                    if char.rect.y//50 == yposition and (master[yposition][xposition+1]) != "w" and char.rect.y == yposition * 50:
                        x_speed = 5
                    if char.rect.y//50 < yposition and (master[yposition][xposition+1]) != "w" and (master[yposition+1][xposition+1]) != "w":
                        x_speed = 5
                    if char.rect.y > yposition * 50 and (master[yposition][xposition+1]) != "w" and (master[yposition-1][xposition+1]) != "w":
                        x_speed = 5



                        
            # Used to allow the character to shoot bullets
                if event.key == pygame.K_UP:
                    mybulletup = Bullet_up(char.rect.x + 40, char.rect.y)
                    Bullets.add(mybulletup)
                    myBullets.add(mybulletup)
                if event.key == pygame.K_DOWN:
                    mybulletdown = Bullet_down(char.rect.x + 40, char.rect.y)
                    Bullets.add(mybulletdown)
                    myBullets.add(mybulletdown)
                if event.key == pygame.K_LEFT:
                    mybulletleft = Bullet_left(char.rect.x + 40, char.rect.y)
                    Bullets.add(mybulletleft)
                    myBullets.add(mybulletleft)
                if event.key == pygame.K_RIGHT:
                    mybulletright = Bullet_right(char.rect.x + 40, char.rect.y)
                    Bullets.add(mybulletright)
                    myBullets.add(mybulletright)
                    
            # Used to allow the character stop moving      
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    y_speed = 0
                if event.key == pygame.K_s:
                    y_speed = 0
                if event.key == pygame.K_a:
                    x_speed = 0
                if event.key == pygame.K_d:
                    x_speed = 0


        xposition = char.rect.x // 50 + 1
        yposition = char.rect.y // 50 + 1
        
        # Used to stop the bullets when hit walls           
        pygame.sprite.groupcollide(Bullets, Walls, True ,False)
        
        # Used to stop the mobs when hit walls
        for w in Walls:
            Mob_Wall = pygame.sprite.spritecollide(w,Mobs, False ,False)
            if Mob_Wall:
                for c in Mob_Wall:
                    if c in Mob1 or c in Mob2:
                        if c.xdirection == "left":
                            c.rect.x = c.rect.x + 2
                        elif c.xdirection == "right":
                            c.rect.x = c.rect.x - 2
                        if c.ydirection == "up":
                            c.rect.y = c.rect.y + 2
                        elif c.ydirection == "down":
                            c.rect.y = c.rect.y - 2
                            
        # Used when bullets hit mobs                           
        for m in Mobs:
            Mob_hit = pygame.sprite.spritecollide(m,myBullets, True , False)
            if Mob_hit:
                m.health = m.health - 1
                        

            
        # Used to stop the character when hit walls
        if characterwall == True:
            if pygame.sprite.spritecollideany(char, Walls ,False):
                if char.xspeed > 0 :
                    x_speed = 0
                if char.xspeed < 0 :
                    x_speed = 0
                if char.yspeed > 0 :
                    y_speed = 0
                if char.yspeed < 0 :
                    y_speed  = 0

        # used when character hits mobs            
        if pygame.sprite.spritecollideany(char, Mobs ,False) and invincible == False:
            char.health = char.health - 1
            invincible = True
            invincibletime = 50

        #time limit for invincible
        if invincible == True:
            invincibletime = invincibletime - 1
            if invincibletime == 0:
                invincible = False

                
        # time limit for go thriugh walls        
        if characterwall == False:
            walltime = walltime - 1
            if walltime == 0:
                characterwall = True
                
        # Used when bullets hit the character    
        if pygame.sprite.spritecollide(char, mobBullets, True) and invincible == False:
            char.health = char.health -1
            invincible = True
            invincibletime = 50

        #end the game when the character is dead            
        if char.health <= 0:
            LOST = True

        # Screen-clearing code
        screen.fill(WHITE)
     
        # --- Drawing code and updates
        health = char.health
        char.update(y_speed, x_speed)
        Mobs.update(char.rect.x, char.rect.y)
        Bullets.update()
        Mobs.draw(screen)
        all_sprites_list.add(Bullets)
        all_sprites_list.draw(screen)

        char.draw(screen)
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
