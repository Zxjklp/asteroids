# this allows to use code from the open-source pygame library throughout this file
import pygame 

# importing all the constants from the constants.py file
from constants import * 

# importing the Player class from the player.py file
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField

# main function that will run the game
def main(): 
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize the pygame library
    pygame.init()

    # creating a screen with the specified width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    # creating a clock object to help track time
    clock = pygame.time.Clock() 

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Create player and add to groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Player.containers = (updatable, drawable)
    updatable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()

    # delta time variable that will be used to keep track of the time that has passed since the last frame
    dt = 0 

    # creating a infinite while loop that will keep the game running
    running = True
    while running:
        # fill the screen with black color
        screen.fill((0, 0, 0)) 

        # Update all sprites
        updatable.update(dt)

        # Check collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)

        # get all the events that have occurred since the last frame
        for event in pygame.event.get(): 
            # if the user has clicked the close button
            if event.type == pygame.QUIT: 
                return
            
        # update the display with the new screen
        pygame.display.flip() 
        
        # setting the frame rate to 60 frames per second
        # The .tick() method returns the amount of time that has passed since the last time it was called: the delta time. Dividing the return value by 1000 (to convert from milliseconds to seconds) and saving it into the dt variable created earlier.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
