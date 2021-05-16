import pygame

class Inventory(pygame.sprite.Sprite):
    def __init__(self, screen, group):
        print('INVENTORY LOAD')
        self.inv = []
        self.menu = pygame.image.load("img/menu.jpg").convert_alpha()
        self.screen = screen
        self.group = group
        self.inventory_is_open = False

    def draw_inventory(self):
        if self.inventory_is_open:
            menu = pygame.transform.scale(self.menu, self.screen.get_size())
            self.screen.blit(menu, (0, 0))
            for sprite in self.group.sprites():
                sprite.move_back()
            for i in self.inv:
                print('Inventory' + i)
    def redraw_inventory(self):
        if self.inventory_is_open == False:
            self.menu.fill((0, 0, 0))

    def add_inventory(self, item):
        if len(self.inv) < 6:
            self.inv.append(item)
        else:
            print("No inventory space")

    def remove_inventory(self, item):
        if len(self.inv) <= 1:
            self.inv.remove(item)
        else:
            print('No remove from inventory')

    def run(self):
        pressed = pygame.key.get_pressed()

        self.draw_inventory()

        if pressed[pygame.K_e]:
            #self.open_inventory()
            self.inventory_is_open = True
        elif pressed[pygame.K_ESCAPE]:
            self.inventory_is_open = False
