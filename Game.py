import pygame
import sys
import image

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x_character = 965
y_character = 545
x_character_speed = 0
y_character_speed = 0
x_mob = 0
y_mob = 0
x_mob_speed = 5
y_mob_speed = 5
rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1920, 1080)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")



def draw_character (screen,x,y): 
    # Head
    pygame.draw.ellipse(screen, BLACK,[x,y,10,10],0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [4+x,17+y], [11+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [4+x,17+y], [-1+x,27+y], 2)
 
    # Body
    pygame.draw.line(screen, BLUE, [4+x,17+y], [4+x,7+y], 2)
 
    # Arms
    pygame.draw.line(screen, BLUE, [4+x,7+y], [8+x,17+y], 2)
    pygame.draw.line(screen, BLUE, [4+x,7+y], [x,17+y], 2)

#def draw_mob (screen,x,y): 
    # Head
    pygame.draw.ellipse(screen, BLACK,[x,y,10,10],0)
     
    # Legs
    pygame.draw.line(screen, BLACK, [4+x,17+y], [11+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [4+x,17+y], [-1+x,27+y], 2)
     
    # Body
    pygame.draw.line(screen, RED, [4+x,17+y], [4+x,7+y], 2)
     
    # Arms
    pygame.draw.line(screen, RED, [4+x,7+y], [8+x,17+y], 2)
    pygame.draw.line(screen, RED, [4+x,7+y], [x,17+y], 2)
      

Bullets = pygame.sprite.Group()

myBullets = pygame.sprite.Group()

mobBullets = pygame.sprite.Group()

class Charactor(pygame.sprite.Sprite):
    
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("image/5001.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.speed = 5
        self.x = 960
        self.y = 540
        self.x_speed = 0
        self.y_speed = 0
        self.active = True
        
        
    def move(self):
        if self.active == True:
            self.x = x_charactor
            self.y = y_charactor
    
char = Charactor(size,size)    
        
class Bullet_up(pygame.sprite.Sprite):
 
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([5,10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.active = True
        
    def update(self):
        self.rect.y -= 10

    def delete(self):
        if self.y <= 0:
            self.active = False
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
        self.active = True
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 10

    def delete(self):
        if self.y >= 1080:
            self.active = False
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
        self.active = True
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.x -= 10
        
    def delete(self):
        if self.x <= 0:
            self.active = False        
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
        self.active = True
     
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.x += 10

    def delete(self):
        if self.x >= 1920:
            self.active = False        
class Mob1(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xspeed = 2
        self.yspeed = 2
        self.active = True
        self.health = 3
        
#this is the method for the enermy to be able to move towards the character
    def move(self):
        self.move()
        if x_character - self.x > 0:
            self.x += self.xspeed
        if x_character - self.x < 0:
            self.x -= self.xspeed
        if y_character - self.y > 0:
            self.y += self.yspeed
        if y_character - self.y < 0:
            self.y -= self.yspeed
        if self.x == x_character:
            self.xspeed = 0
        if self.y == y_character:
            self.yspeed = 0
        
    def die(self):
        if self.health == 0:
            self.active = false

            
class Mob2(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xspeed = 2
        self.yspeed = 2
        self.active = True
        timeCount = 0
        
    def move(self):
        self.move()
        if x_character - self.x > 200:
            self.x += self.xspeed
        if x_character - self.x < 200:
            self.x -= self.xspeed
        if y_character - self.y > 200:
            self.y += self.yspeed
        if y_character - self.y < 200:
            self.y -= self.yspeed

    def attack(self):
        if timeCount == 30:
            if x_character - self.x > 0:
                mobbulletright = Bullet_right(self.x,self.y)
            if x_character - self.x > 0:
                mobbulletleft = Bullet_left(self.x,self.y)
            if y_character - self.y > 0:
                mobbulletup = Bullet_up(self.x,self.y)
            if y_character - self.x < 0:
                mobbulletdown = Bullet_down(self.x,self.y)
        else:
            self.timeCount = self.timeCount + 1


mob1 = Mob1(size,size,size,size)
mob2 = Mob2(size,size,size,size)
#here we can add mobs into groups
Mobs = pygame.sprite.Group()
Mobs.add(mob1,mob2)

Mob1 = pygame.sprite.Group()
Mob1.add(mob1)
Mob2 = pygame.sprite.Group()
Mob2.add(mob2)

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
                y_character_speed = -5
                char.y_speed = -5
            if event.key == pygame.K_s:
                y_character_speed = 5
                char.y_speed = 5
            if event.key == pygame.K_a:
                x_character_speed = -5
                char.x_speed = -5
            if event.key == pygame.K_d:
                x_character_speed = 5
                char.x_speed = 5

                
        # Used to allow the character to shoot bullets
            if event.key == pygame.K_UP:
                mybulletup = Bullet_up(x_character + 4, y_character)
                all_sprites_list.add(mybulletup)
                Bullets.add(mybulletup)
                myBullets.add(mybulletup)
            if event.key == pygame.K_DOWN:
                mybulletdown = Bullet_down(x_character + 4, y_character)
                all_sprites_list.add(mybulletdown)
                Bullets.add(mybulletdown)
                myBullets.add(mybulletdown)
            if event.key == pygame.K_LEFT:
                mybulletleft = Bullet_left(x_character + 4, y_character)
                all_sprites_list.add(mybulletleft)
                Bullets.add(mybulletleft)
                myBullets.add(mybulletleft)
            if event.key == pygame.K_RIGHT:
                mybulletright = Bullet_right(x_character + 4, y_character)
                all_sprites_list.add(mybulletright)
                Bullets.add(mybulletright)
                myBullets.add(mybulletright)
                
        # Used to allow the character stop moving      
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                y_character_speed = 0
                char.y_speed = 0
            if event.key == pygame.K_s:
                y_character_speed = 0
                char.y_speed = 0
            if event.key == pygame.K_a:
                x_character_speed = 0
                char.x_speed = 0
            if event.key == pygame.K_d:
                x_character_speed = 0
                char.x_speed = 0

    # --- Game logic should go here
    # Used to udate the position of the character
    x_character += x_character_speed
    y_character += y_character_speed

    # Used to stop the character when hit the boundry of the windows
    if y_character < 0:
        y_character_speed = 0
        y_character = 0
    if y_character > 1051:
        y_character_speed = 0
        y_character = 1051
    if x_character < 0:
        x_character_speed = 0
        x_character = 0
    if x_character > 1910:
        x_character_speed = 0
        x_character =1910


    if char.y < 0:
        char.y_speed = 0
        char.y = 0
    if char.y > 1051:
        cahr.y_speed = 0
        char.y = 1051
    if char.x < 0:
        char.x_speed = 0
        char.x = 0
    if char.x > 1910:
        char.x_speed = 0
        char.x =1910


    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here

    
    screen.blit(char.image, char.rect)
    draw_character(screen,x_character,y_character)
    #myBullet.update()
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
