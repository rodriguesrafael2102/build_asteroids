import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
	
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(x, y)    
    asteroidField = AsteroidField()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)
            if obj == player:
                player.timer -= dt
            
        for obj in asteroids:
            collision_detected = obj.check_collision(player)
            if collision_detected:
                print("Game over!")
                sys.exit()
            for obj_shot in shots:
                shot_asteroid_detected = obj_shot.check_collision(obj)
                if shot_asteroid_detected:
                    obj_shot.kill()
                    obj.split()    


        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60.0))/1000

if __name__ == "__main__":
    main()
