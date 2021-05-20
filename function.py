from PIL import Image, ImageDraw
import pygame

class Function:
    def __init__(self, screen):
        self.screen = screen

    def error(self, msg):
        img = Image.new('RGB', (130, 30), color=(0, 0, 0))
        d = ImageDraw.Draw(img)
        d.text((10, 10), msg, fill=(255, 0, 0))
        img.save('img/error.png')

        draw_image = pygame.image.load("img/error.png").convert_alpha()
        self.screen.blit(draw_image, (0, 0))

    def information(self, msg):
        img = Image.new('RGB', (150, 30), color=(0, 0, 0))
        d = ImageDraw.Draw(img)
        d.text((10, 10), msg, fill=(255, 165, 0))
        img.save('img/info.png')

        draw_image = pygame.image.load('img/info.png').convert_alpha()
        self.screen.blit(draw_image, (650, 1))




