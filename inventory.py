import pygame
from function import Function
from PIL import Image, ImageDraw, ImageFont


class Inventory(pygame.sprite.Sprite):
    def __init__(self, screen, group, tmx_data):
        print('INVENTORY LOAD')
        self.inv = ["pikachu"]
        self.life = [100, 100, 100, 100, 100, 100, 100, 100]
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
            if len(self.inv) >= 1:
                self.draw_item(self.inv[0], 180, 140, self.life[0])
            if len(self.inv) >= 2:
                self.draw_item(self.inv[1], 180, 225, self.life[1])
            if len(self.inv) >=3:
                self.draw_item(self.inv[2], 180, 305, self.life[2])
            if len(self.inv) >=4:
                self.draw_item(self.inv[3], 180, 390, self.life[3])
            if len(self.inv) >=5:
                self.draw_item(self.inv[4], 425, 140, self.life[4])
            if len(self.inv) >=6:
                self.draw_item(self.inv[5], 425, 225, self.life[5])
            if len(self.inv) >=7:
                self.draw_item(self.inv[6], 425, 305, self.life[6])
            if len(self.inv) >= 8:
                self.draw_item(self.inv[7], 425, 390, self.life[7])



    def draw_item(self, item, x, y, life):
        image = Image.new('RGB', (100, 30), color=(255, 255, 255))
        d = ImageDraw.Draw(image)
        d.text((10, 10), 'Life : ' + str(life) + '/100', fill=(255, 105, 180))
        image.save('img/life.png')
        draw_image = pygame.image.load('img/life.png').convert_alpha()
        self.screen.blit(draw_image, (x  + 80, y + 25))

        draw_image_name = Image.new('RGB', (100, 30), color=(255, 255, 255))
        d_name = ImageDraw.Draw(draw_image_name)
        d_name.text((10, 10), item, fill=(135,206,250))
        draw_image_name.save('img/name.png')
        draw_image_name_load = pygame.image.load('img/name.png').convert_alpha()
        self.screen.blit(draw_image_name_load, (x  + 80, y))

        draw_image_supp = pygame.image.load("img/trash.png")
        self.draw_image_supp = pygame.transform.scale(draw_image_supp, (32,32))
        self.Rectplace = pygame.draw.rect(self.screen, (255, 0, 0), (x - 40, y + 10, 32, 32))
        self.screen.blit(self.draw_image_supp, (x - 40, y + 10))

        draw_image_poke = pygame.image.load("img/" + item + ".png")
        draw_image_poke = pygame.transform.scale(draw_image_poke, (65,50))
        self.screen.blit(draw_image_poke, (x, y))

        self.get_trash(item, life)
        self.get_close()

    def add_inventory(self, item):
        if len(self.inv) < 8:
            self.inv.append(item)
        else:
            self.function.error('No add inventory')

    def remove_inventory(self, item, life):
        if len(self.inv) > 1:
            self.inv.remove(item)
            life = 100
            print(str(item) + " as delete | set variable " + str(life))
        else:
            self.function.error('No remove inventory')

    def get_trash(self, item, life):
        if pygame.mouse.get_pressed()[0] and self.Rectplace.collidepoint(pygame.mouse.get_pos()):
            self.remove_inventory(item, life)

    def get_close(self):
        Rectplace_close = pygame.draw.rect(self.screen, (255, 255, 255), (340, 480, 120, 60))
        close = pygame.image.load("img/close.png").convert_alpha()
        self.screen.blit(close, (340, 480))
        if pygame.mouse.get_pressed()[0] and Rectplace_close.collidepoint(pygame.mouse.get_pos()):
            self.inventory_is_open = False


    def run(self, tmx_data, map):
        self.tmx_data = tmx_data
        self.map = map
        pressed = pygame.key.get_pressed()
        if self.inventory_is_open:
            pygame.mouse.set_visible(True)
        self.draw_inventory()
        if pressed[pygame.K_e]:
            self.inventory_is_open = True

