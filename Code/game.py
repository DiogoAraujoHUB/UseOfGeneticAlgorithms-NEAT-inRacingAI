#Import necessary files (pygame is most important)
import pygame
import time
import math

#Create window for game (size is same as track)
WIDTH = 1920
HEIGHT = 1080

#Car size (used to format car)
CAR_SIZE_X = 60
CAR_SIZE_Y = 60

#Color To Crash on Hit
BORDER_COLOR = (255, 255, 255)

#Color of finish line
FINISH_COLOR = (0, 255, 0)

#Set display caption
pygame.display.set_caption("Path Following AI")

#Define rotation function
def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

#Define scaling function
def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

#Game Info that allows it to run with info
class GameInfo:
    def __init__(self):
        self.started = False
        self.level_start_time = 0

    #Start the level
    def start_game(self):
        self.started = True
        self.level_start_time = time.time()

    #Get current level time
    def get_game_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)

    #Reset the AI
    def reset(self):
        self.started = False
        self.level_start_time = 0

    #Finish game after reaching finish line
    def path_finished(self):
        return self.started

#Car class used to define car entities
class Car:
    def __init__(self):
        self.START_POS = [885, 920]  # Starting Position
        self.img = scale_image(pygame.image.load("../Images/red-car.png"), 0.7)

        # Load Car Sprite and Rotate
        self.sprite = pygame.image.load('../Images/red-car.png').convert()  # Convert Speeds Up A Lot
        self.sprite = pygame.transform.scale(self.sprite, (CAR_SIZE_X, CAR_SIZE_Y))
        self.rotated_sprite = self.sprite

        #Calculate car corners (giving it more space so that it plays smoother)
        self.width = CAR_SIZE_X / 2
        self.height = CAR_SIZE_Y / 2

        self.position = self.START_POS
        self.x, self.y = self.position
        self.angle = 270
        self.speed = 0

        #Define acceleration parameters
        self.max_speed = 6
        self.acceleration = 0.1
        self.rotation_speed = 3

        self.alive = True  # Boolean To Check If Car is Crashed

    #Draw Car Sprite
    def draw(self, screen):
        blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)

    #Reset the car on level finish
    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 270
        self.speed = 0

    #Check for car collision<w
    def check_collision(self):
        corners = [(self.x, self.y),
                   (self.x + self.width, self.y),
                   (self.x, self.y + self.height),
                   (self.x + self.width, self.y + self.height)]
        for point in corners:
            #If Any Corner Touches Border Color -> Crash
            if game_map.get_at((int(point[0]), int(point[1]))) == BORDER_COLOR:
                return 1
            #If Any Corner Touches Finish Color -> Finish
            if game_map.get_at((int(point[0]), int(point[1]))) == FINISH_COLOR:
                return 2

        return 0

    # Rotate the car
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_speed
        elif right:
            self.angle -= self.rotation_speed

    def move_forward(self):
        self.speed = min(self.speed + self.acceleration, self.max_speed)
        self.move()

    def move_backward(self):
        self.speed = max(self.speed - self.acceleration, -self.max_speed / 2)
        self.move()

    def reduce_speed(self):
        self.speed = max(self.speed - self.acceleration / 2, 0)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.speed
        horizontal = math.sin(radians) * self.speed

        self.y -= vertical
        self.x -= horizontal

    def stop(self):
        self.speed = 0

#Define keys to move player (WASD)
def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()

#Handle all collisions in game window (can only happen between ai, track border and finish line)
def handle_collision(car, game_info):
    #Get current collision
    collision = car.check_collision()

    #Check if it hits border
    if collision == 1:
        car.stop()

    ##Check if it hits finish line
    if collision == 2:
        finish_text = main_font.render("Finish line has been reached!", True, (0, 0, 0))
        text_rect = finish_text.get_rect()
        text_rect.center = (900, 450)
        screen.blit(finish_text, text_rect)
        pygame.display.update()
        pygame.time.wait(5000)
        game_info.reset()
        player_car.reset()

#Start the game
if __name__ == "__main__":
    #Initialize pygames
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    #Create the Map
    game_map = pygame.image.load('../Images/Maps/simpleMap.png').convert()  # Convert Speeds Up A Lot

    #Set the game font
    main_font = pygame.font.SysFont("Arial", 30)

    #Setup game
    run = True
    clock = pygame.time.Clock()
    player_car = Car()
    game_info = GameInfo()

    #Run the game
    while run:
        clock.tick(60) #60 FPS

        #Reset screen (display game map)
        screen.blit(game_map, (0,0))

        #Had to be done outside draw function due to font errors (draw images)
        # Setup text in window (time and current velocity)
        time_text = main_font.render(f"Time: {game_info.get_game_time()}s", 0, (0, 0, 0))
        screen.blit(time_text, (10, HEIGHT - time_text.get_height() - 40))

        speed_text = main_font.render(f"Car Speed: {round(player_car.speed, 1)}px/s", 0, (0, 0, 0))
        screen.blit(speed_text, (10, HEIGHT - speed_text.get_height() - 10))

        # Draw the car
        player_car.draw(screen)

        # Update the display
        pygame.display.update()

        #Display menu before game start
        while not game_info.started:
            #Display start text
            start_text = main_font.render("Press any button to start the game!", True, (0,0,0))
            text_rect = start_text.get_rect()
            text_rect.center = (900, 450)
            screen.blit(start_text, text_rect)
            pygame.display.update()

            #Either start game or quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:
                    game_info.start_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        #Move the car (player)
        move_player(player_car)

        #Handle collision for car
        handle_collision(player_car, game_info)

    #Exit pygame fully
    pygame.quit()