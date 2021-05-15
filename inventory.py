import pygame
import pytmx
import pyscroll

class Inventory(pygame.sprite.Sprite):
    def __init__(self, screen):
        print('INVENTORY LOAD')
        self.inv = []
        self.inventory_img = 'img/icon.png'
        self.screen = screen

    def draw_inventory(self):
        menu = pygame.image.load("img/menu.jpg").convert_alpha()
        menu = pygame.transform.scale(menu, self.screen.get_size())
        if self.inventory_is_open:
            self.screen.blit(menu, (0, 0))
        else:
            menu.fill((0, 0, 0))


    def add_inventory(self, item):
        if len(self.inv) < 6:
            self.inv.append(item)
        else:
            print("No inventory space")

    def run(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_e]:
            #self.open_inventory()
            self.inventory_is_open = True
            self.draw_inventory()
        else:
            #self.close_inventory()
            self.inventory_is_open = False
            self.draw_inventory()
