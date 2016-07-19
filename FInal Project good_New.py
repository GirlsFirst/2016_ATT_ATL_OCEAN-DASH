import pygame
import random
import time


AQUA = (0, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PALE = (255, 240, 245)
BLUEISH = (0, 139, 139)

colors = [(255, 182, 193), (0, 255, 127), (122, 55, 139), (255, 193, 37) ]

#def random_color():
 #   return random.choice(colors)

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ocean Dash")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(→).
            A negative integer draws the building left to right (←).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up ↑
            A negative integer draws the building down ↓
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x_point, y_point, width, height, color):
        # Store the paramets as local stuff and
        # initialize anything else that you want to start
        # note: anything NOT stored as self.* cannot be used in other class functions
        self.x_point = x_point-width/2
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        # Draw the ball (pygame.draw)
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height], 0)

    def move(self, speed):
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right →
            A negative integer moves the building to the left  ←
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """
        # Modify self.x_point by speed
        self.speed = speed
        self.x_point += -speed  

class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, color, speed):
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.buildingsleft = []
        self.buildingsright = []
        self.add_building(300-1)
        self.obstacles = pygame.sprite.Group()
        
    def add_buildings(self):
        """
        Will call add_building until there the buildings fill up the width of the
        scroller.
        """
        # Keep calling add_building until it fills up the width of the scroller
        # Hint: Look at where the last building in the list ends
        # self.add_buildings(0)
        last_sprite =0
        
        while self.buildingsleft[-1].x_point <= 300-1-self.buildingsleft[-1].width:
            self.add_building(300-1)
            #self.buildings

        while self.buildingsright[-1].x_point >= 300-1+self.buildingsright[-1].width:
            self.add_building(300-1)
            #self.buildings
        
    def add_building(self, x_location):
        self.x_location = x_location 
        building_width = 6
        building_height = 0
        #self.buildings.append(Building(x_location, 300-0.5*building_height, building_width, building_height, self.color))
        self.buildingsleft.append(Building(x_location, 300-1-0.5*building_height, building_width, building_height, self.color))
        self.buildingsright.append(Building(x_location, 300-1-0.5*building_height, building_width, building_height, self.color))
    
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a building.
        Adds a building to list of buildings.
        """
        
        # Append a Building to the buildings list
        # Hint: This is where random comes in, to choose a width and height for the new building

    def draw_buildings(self):
        """
        This calls the draw method on each building.
        """
        # Use a 'for loop' to
        #for building in self.buildings:
            #building.draw()
        for building in self.buildingsleft:
            building.draw()
        for building in self.buildingsright:
            building.draw()

    def move_buildings(self):
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """
        # Use a for loop to call the move function for each building
        for building in self.buildingsleft:
            # TODO: if a building goes off the screen, delete it from self.buildingslist
            if building.x_point + building.width <= 0:
                self.buildingsleft.pop(0)




            
            building.move(self.speed)
            building.height = (600*(299-building.x_point))/300
            building.y_point = 299-0.5*building.height

        for building in self.buildingsright:
            if building.x_point >= 600:
                self.buildingsright.pop(0)
            building.move(-self.speed)
            building.height = (600*(299-building.x_point))/300
            building.y_point = 299-0.5*building.height

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x_location,y_location, width, height, color, speed):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.x_location = x_location
        self.y_location = y_location
        self.move_left = 1
        self.move_right = -1
        self.rect = pygame.Rect(self.x_location-self.width/2, self.y_location-self.height/2, width, height)
        
    def draw_object(self):
        pygame.draw.rect (screen, self.color, [self.x_location-self.width/2, self.y_location-self.height/2, self.width, self.height])

    def resize_object(self):
        self.width +=2
        self.height +=1
        if self.width >= 100:
            self.width = 100
        if self.height >= 50:
            self.height = 50
        self.rect.width = self.width
        self.rect.height = self.height
        
    def move_object(self, direction):
        if direction is "Center":
            self.x_location == 0
        if direction is "RIGHT":
            self.x_location += 1
        elif direction is "LEFT":
            self.x_location -= 1

            
        self.y_location += self.speed
        self.rect.y = self.y_location-self.height/2
        self.rect.x = self.x_location-self.width/2
            
            
        
        
class Obstacle_Scroller(object):    
    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.obstacle_list = []
        self.add_obstacle(0)        
        
    def add_obstacles(self):
        while (self.obstacle_list[0].y_location + self.obstacle_list[0].height <= 600):
            self.add_obstacle(299)

    def add_obstacle(self, y_location):
        self.y_location = y_location
        self.obstacle_list.add(Obstacle(self.x_location, self.y_location, self.width, self.height, self.color, self.speed))

    def draw_obstacle(self):
        for obstacle in self.obstacle_list:
            obstacle.draw_object()

    def move_obstacle(self):
        for obstacle in self.obstacle_list:
            obstacle.move_object()
            if self.obstacle_list[0].y_location + self.obstacle_list[0].height >= 400:
                self.obstacle_list.remove(obstacle)
            if self.obstacle_list[0].x_location + self.obstacle_list[0].width >= 400:
                self.obstacle_list.remove(obstacle)
                

    def resive_obstacle(self):
        for obstacle in self.obstacle_list:
            obstacle.resive_object()
        
class player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("squirtle3.png")
        self.rect = self.image.get_rect ()
        self.rect.x=SCREEN_WIDTH/2-self.rect.width/2
        self.rect.y = SCREEN_HEIGHT-100
    
    def add_player(self, x_location):
        self.x_location = x_location 
        player_width = 2
        player_height = 2
        
    #def draw_players (self):
    def move_players (self):
        for player in self.players:
            player.move (self.speed)
            player.height = 200
            player.y_point = 300

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3/2) #how long it stays on screen
    
def GameOver():
    Over = True
    while Over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(RED)
        message_display("Game Over!")
        done = True
def Winner():
    Over = True
    while Over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(PALE)
        message_display("Winner!!!!!!!")
        done = True

    
def things_dodged(count):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render ("Dodged: " + str(count), True, BLACK)
    screen.blit(text, (230, 0))







                

BACK_SCROLLER_COLOR = (0, 134, 139)
BACKGROUND_COLOR = (17, 9, 89)

dodged = 0

direction_list = ["RIGHT", "LEFT", "FORWARD"]

obstacle_list = pygame.sprite.Group()

obstacle = Obstacle(SCREEN_WIDTH/2-1, SCREEN_HEIGHT/2, 10, 10, colors, 3)
#obstacle_list.append(obstacle)
back_scroller = Scroller(SCREEN_WIDTH, 200, BACK_SCROLLER_COLOR, 1)
#back_scroller.add_obstacle(200)

player_group = pygame.sprite.Group()
squirtle = player ()
player_group.add(squirtle)

start = time.time()

direction_move = random.choice (direction_list)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and squirtle.rect.x >= 125:
                squirtle.rect.x -= 108.33
            elif event.key == pygame.K_RIGHT and squirtle.rect.x <= 450:
                squirtle.rect.x += 108.33

    # --- Game logic should go here

        # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(AQUA)
    
    # --- Drawing code should go here
    
    back_scroller.add_buildings()
    
    back_scroller.draw_buildings()

    things_dodged(dodged)
    
    #print(pygame.time.get_ticks ())
    
    if pygame.sprite.spritecollide(squirtle, obstacle_list, False):
        time.sleep(1)
        GameOver()
    
    pygame.draw.rect(screen, AQUA, [SCREEN_WIDTH/2 -15, SCREEN_HEIGHT/2 -30, 30, 60])
    end = time.time()
    if (pygame.time.get_ticks () > 6100 ):
        #add obstacle to obstacle_list
        if end - start > 2.0:
            start = end
            new_direction_move = random.choice (direction_list)
            while new_direction_move == direction_move:
                new_direction_move = random.choice (direction_list)
            direction_move = new_direction_move
            square_color = random.choice (colors)
            obstacle = Obstacle(SCREEN_WIDTH/2 -5 -1, SCREEN_HEIGHT/2 -4, 10, 10, square_color, 2)
            obstacle_list.add(obstacle)
        #obstacle_list.append(Obstacle(SCREEN_WIDTH/2 -5, SCREEN_HEIGHT/2 -5, 10, 10, RED, 1))
        for obstacle in obstacle_list:
            obstacle.draw_object()
            obstacle.move_object(direction_move)
            obstacle.resize_object()
        for obstacle in obstacle_list:
            if obstacle.y_location-0.5*obstacle.height >= 600:
                obstacle_list.remove(obstacle)
                dodged += 1
        if dodged >= 20:
            Winner()
      
    #   back_scroller.move_obstacles ()
    
    back_scroller.move_buildings()

    player_group.draw(screen)
   
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()





