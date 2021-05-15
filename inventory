import pygame
import pytmx
import pyscroll

class Inventory(pygame.sprite.Sprite):
    def __init__(self, screen):
        print('INVENTORY LOAD')
        self.player = 'yaya'
        self.inv = []
        self.inventory_img = 'img/icon.png'
        self.screen = screen

    def open_inventory(self):
        print('Open Inventory is ' + str(self.inv))



    def close_inventory(self):
        print('Close Inventory for ' + str(self.player))



    def add_inventory(self, item):
        if len(self.inv) < 6:
            self.inv.append(item)
        else:
            print("No inventory space")
