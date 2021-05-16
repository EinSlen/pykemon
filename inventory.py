import pygame
from function import Function

class Inventory(pygame.sprite.Sprite):
    def __init__(self, screen, group, tmx_data):
        print('INVENTORY LOAD')
        self.inv = []
        self.menu = pygame.image.load("img/menu.jpg").convert_alpha()
        self.screen = screen
        self.group = group
        self.inventory_is_open = False
        self.function = Function(self.screen)
        self.tmx_data = tmx_data

    def draw_inventory(self):
        if self.inventory_is_open:
            menu = pygame.transform.scale(self.menu, self.screen.get_size())
            self.screen.blit(menu, (0, 0))
            for sprite in self.group.sprites():
                sprite.move_back()
            for i in self.inv:
                print('Inventory : ' + i)

    def add_inventory(self):
        if len(self.inv) < 6:
            self.inv.append('Add')
        else:
            self.function.error('No add inventory')

    def remove_inventory(self, item):
        if len(self.inv) <= 1:
            self.inv.remove(item)
        else:
            self.function.error('No remove inventory')

    def run(self, tmx_data, map):
        self.tmx_data = tmx_data
        self.map = map
        pressed = pygame.key.get_pressed()

        self.draw_inventory()
        if pressed[pygame.K_e]:
            self.inventory_is_open = True
        elif pressed[pygame.K_ESCAPE]:
            self.inventory_is_open = False
        elif pressed[pygame.K_f]:
            self.add_inventory()

