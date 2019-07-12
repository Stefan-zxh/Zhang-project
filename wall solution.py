import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x_character = 355
y_character = 255
x_character_speed = 0
y_character_speed = 0
rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")



def draw_character (screen,x,y): 
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
    

    
class Bullet_up(pygame.sprite.Sprite):
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
        self.rect.y -= 5

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
        self.rect.y += 5

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
        self.rect.x -= 5

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
        self.rect.x += 5


all_sprites_list = pygame.sprite.Group()



# Loop until the user clicks the close button.
done = False
varx=0
vary=600
    
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
            if event.key == pygame.K_s:
                y_character_speed = 5
            if event.key == pygame.K_a:
                x_character_speed = -5
            if event.key == pygame.K_d:
                x_character_speed = 5


            if event.key == pygame.K_UP:
                mybulletup = Bullet_up(x_character + 4, y_character)
                all_sprites_list.add(mybulletup)
            if event.key == pygame.K_DOWN:
                mybulletdown = Bullet_down(x_character + 4, y_character)
                all_sprites_list.add(mybulletdown)
            if event.key == pygame.K_LEFT:
                mybulletleft = Bullet_left(x_character + 4, y_character)
                all_sprites_list.add(mybulletleft)
            if event.key == pygame.K_RIGHT:
                mybulletright = Bullet_right(x_character + 4, y_character)
                all_sprites_list.add(mybulletright)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                y_character_speed = 0
            if event.key == pygame.K_s:
                y_character_speed = 0
            if event.key == pygame.K_a:
                x_character_speed = 0
            if event.key == pygame.K_d:
                x_character_speed = 0


    # --- Game logic should go here
    x_character += x_character_speed
    y_character += y_character_speed

    
    if y_character < 0:
        y_character_speed = 0
        y_character = 0
    if y_character > 471:
        y_character_speed = 0
        y_character = 471
    if x_character < 0:
        x_character_speed = 0
        x_character = 0
    if x_character > 690:
        x_character_speed = 0
        x_character = 690
        
 
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here



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
