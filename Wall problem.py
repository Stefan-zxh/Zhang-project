import pygame
import sys
import image

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x_speed = 0
y_speed = 0
x_mob = 0
y_mob = 0
x_mob_speed = 5
y_mob_speed = 5
rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5
x1 = 0
y1 = 0
x2 = 1000
y2 = 1000
level_1 = True

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1200,800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")


class Character(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/5001.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self,y_speed,x_speed):
        self.rect.y += y_speed
        self.rect.x += x_speed
        
char = Character(500,500)


class Wall(pygame.sprite.Sprite):

    def __init__(self,x,y):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/wall.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x*50
        self.rect.y = y*50
        
class Bullet_up(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([5,10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

class Bullet_down(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self,x,y):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([5,10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 10
        if self.rect.y > 1080:
            self.kill()

class Bullet_left(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self,x,y):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([10,5])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.x -= 10
        if self.rect.x < 0:
            self.kill()       
class Bullet_right(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self,x,y):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([10,5])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
     
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.x += 10
        if self.rect.x > 1920:
            self.kill()
            
class Mob1(pygame.sprite.Sprite):
    def __init__(self,x,y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/031.00.00.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xspeed = 2
        self.yspeed = 2
        self.health = 3
        
#this is the method for the enermy to be able to move towards the character
    def update(self,x_character, y_character):
        if self.health > 0:
            if x_character - self.rect.x > 0:
                self.rect.x += self.xspeed
            if x_character - self.rect.x < 0:
                self.rect.x -= self.xspeed
            if y_character - self.rect.y > 0:
                self.rect.y += self.yspeed
            if y_character - self.rect.y < 0:
                self.rect.y -= self.yspeed
        if self.health <= 0:
            self.kill()

            
class Mob2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/010.01.00.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xspeed = 2
        self.yspeed = 2
        self.timeCount = 0
        self.health = 2
        
    def update(self,x_character, y_character):
        
        if self.health > 0:   
            if  x_character - self.rect.x > 200:
                self.rect.x += self.xspeed
            if x_character - self.rect.x < -200:
                self.rect.x -= self.xspeed
            if y_character - self.rect.y > 200:
                self.rect.y += self.yspeed
            if y_character - self.rect.y < -200:
                self.rect.y -= self.yspeed
            if  x_character - self.rect.x > 0 and x_character - self.rect.x < 200:
                self.rect.x -= self.xspeed
            if x_character - self.rect.x < 0 and x_character - self.rect.x > -200:
                self.rect.x += self.xspeed
            if  y_character - self.rect.y > 0 and y_character - self.rect.y < 200:
                self.rect.y -= self.yspeed
            if y_character - self.rect.y < 0 and y_character - self.rect.y > -200:
                self.rect.y += self.yspeed
            
            if self.timeCount == 30:
                self.timeCount = 0
                if x_character - self.rect.x > 0:
                    mobbulletright = Bullet_right(self.rect.x,self.rect.y)
                if x_character - self.rect.x > 0:
                    mobbulletleft = Bullet_left(self.rect.x,self.rect.y)
                if y_character - self.rect.y > 0:
                    mobbulletup = Bullet_up(self.rect.x,self.rect.y)
                if y_character - self.rect.x < 0:
                    mobbulletdown = Bullet_down(self.rect.x,self.rect.y)
            else:
                self.timeCount = self.timeCount + 1
                
        if self.health <= 0:
            self.kill()
                      

mob1 = Mob1(50,50)
mob2 = Mob2(1000,1000)
#here we can add mobs into groups
Mobs = pygame.sprite.Group()
Mobs.add(mob1,mob2)

Mob1 = pygame.sprite.Group()
Mob1.add(mob1)
Mob2 = pygame.sprite.Group()
Mob2.add(mob2)
Walls = pygame.sprite.Group()
Bullets = pygame.sprite.Group()
myBullets = pygame.sprite.Group()
mobBullets = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        # Used to move the character 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_speed = -5
            if event.key == pygame.K_s:
                y_speed = 5
            if event.key == pygame.K_a:
                x_speed = -5
            if event.key == pygame.K_d:
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

    # --- Game logic should go here
    # Used to stop the character when hit the boundry of the windows


    if char.rect.y < 0:
        char.y_speed = 0
        char.rect.y = 0
    if char.rect.y > 800:
        cahr.y_speed = 0
        char.rect.y = 800
    if char.rect.x < 0:
        char.x_speed = 0
        char.rect.x = 0
    if char.rect.x > 1200:
        char.x_speed = 0
        char.rect.x =1200

    if level_1 == True:
        level_1 = False
        with open("Level.txt","r") as f:
            for Y in range (0,16):
                a = f.readline()
                
                for X in range (0,24):
                    if  a[X] == "w":
                        myWall = Wall(X,Y)
                        Walls.add(myWall)
        


    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here
    char.update(y_speed, x_speed)
    Mobs.update(char.rect.x, char.rect.y)
    Bullets.update()
    Mobs.draw(screen)
    all_sprites_list.add(Walls)
    all_sprites_list.add(char)
    all_sprites_list.add(Bullets)
    all_sprites_list.draw(screen)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
