import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image


_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

x = 30
y = 30


clock = pygame.time.Clock()

color = (200,0,200)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue

        screen.fill((255, 255, 255))
        screen.blit(get_image('images/ball.png'), (100, 200))
        play_sound("sounds/m1.ogg")
        # draw a rectangle
        pygame.draw.rect(screen, color, pygame.Rect(10, 10, 100, 100), 10)
        # draw a circle
        pygame.draw.circle(screen, color, (300, 60), 50, 10)
        pygame.display.flip()


        clock.tick(60)
