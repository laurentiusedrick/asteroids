import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  
  Player.containers = (updateable, drawable)
  Asteroid.containers = (updateable, drawable, asteroids)
  AsteroidField.containers = (updateable)
  Shot.containers = (updateable, drawable)
  

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return

    screen.fill("#000000")
    for u in updateable:
      u.update(dt)
    for d in drawable:
      d.draw(screen)

    pygame.display.flip()

    for a in asteroids:
       if a.collision(player):
          print("Game over!")
          return
       
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()