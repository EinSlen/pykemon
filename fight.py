import pygame
import random
from PIL import Image, ImageDraw
import time

import config
from function import Function
from sound import Sound

class Fight:

    def __init__(self, screen):
        print("FIGHT LOADED")
        self.screen = screen
        self.function = Function(self.screen)
        self.in_fight = False
        self.zone = []
        self.capa = []
        self.pokemon = ["florizarre", "dracaufeu", "tortank", "papilusion", "roucool", "rattata", "onix", "smogogo", "arcanin", "akwakwak", "triopikeur", "nosferalto", "staross", "insecateur", "ptera", "ronflex", "evoli", "sulfura"]
        self.capacity = ["charge", "Acid", "Acrobatics", "Aeroblast", "MaxAirstream", "GrassPledge", "WaterPledge", "AquaJet", "Assurance", "MorningSun", "PyroBall", "Sing", "DefenseCurl", "ElectroBall", "BugBuzz", "BrutalSwing", "Tickle"]
        self.wait = 250
        self.in_attak = True
        self.change = False
        self.transition = False
        self.transitionWait = 0
        self.no_capture = False
        self.sound = Sound()

    def get_fight(self):
        if self.map == 'world':
            for obj in self.tmx_data.objects:
                if obj.name == "fight_zone":
                    self.zone.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                    for sprite in self.group.sprites():
                        if sprite.feet.collidelist(self.zone) > -1:
                            n = random.randint(1, 1000)
                            if n == 1000:
                                self.in_attak = True
                                self.transition = True
                                self.life_battle = 100
                                self.pokemon_number = random.randint(0, len(self.pokemon))
                                self.number_capa = 0
                                print('FIGHT VERSUS ' + self.pokemon[self.pokemon_number - 1])
                                for i in range(2 ** 2):
                                    n = random.randint(0, len(self.capacity))
                                    if i == n:
                                        n = random.randint(0, len(self.capacity))
                                    self.capa.append(self.capacity[n - 1])
                                    self.get_capacity()
                                    self.sound.create_sound('pokemon-battle.mp3')



    def for_fight(self):
        for sprite in self.group.sprites():
            sprite.move_back()
        battle_scene = pygame.image.load("img/battle.png").convert_alpha()
        menu = pygame.transform.scale(battle_scene, self.screen.get_size())
        self.screen.blit(menu, (0, 0))

        pokemon_img = pygame.image.load("img/" + self.pokemon[self.pokemon_number - 1] + ".png")
        pokemon_img = pygame.transform.scale(pokemon_img, (154, 154))
        self.screen.blit(pokemon_img, (510, 90))

        img = Image.new('RGB', (295, 35), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        if self.life_battle > 50:
            d.text((295/3, 35/3), 'Life : ' + str(self.life_battle) + '/100', fill=(50, 202, 50))
        elif self.life_battle >= 20 and self.life_battle <= 50:
            d.text((295/3, 35/3), 'Life : ' + str(self.life_battle) + '/100', fill=(255, 105, 180))
        elif self.life_battle < 20:
            d.text((295/3, 35/3), 'Life : ' + str(self.life_battle) + '/100', fill=(255, 0, 0))
        img.save('img/life.png')
        draw_image = pygame.image.load("img/life.png").convert_alpha()
        self.screen.blit(draw_image, (50, 105))

        img2 = Image.new('RGB', (295, 40), color=(255, 255, 255))
        d2 = ImageDraw.Draw(img2)
        d2.text((295/3, 40/2), self.pokemon[self.pokemon_number - 1], fill=(135, 206, 250))
        img2.save('img/name.png')
        draw_image_pokemon = pygame.image.load('img/name.png').convert_alpha()
        self.screen.blit(draw_image_pokemon, (50, 65))


        self.get_inv()

    def get_capacity(self):
        for i in str(len(self.capa)):
            self.number_capa = self.number_capa + 1
            capa_one = Image.new('RGB', (100, 40), color=(255, 255, 255))
            one_draw = ImageDraw.Draw(capa_one)
            print('Capacity "' + self.capa[int(i) - 1] + '" as create.')
            one_draw.text((100/4, 40/4), self.capa[int(i) - 1], fill=(192, 192, 192))
            capa_one.save('img/charge' + str(self.number_capa) + '.png')

    def get_inv(self):
            if len(self.inventory.inv) >= 1 and self.inventory.life[0] >= 0:
                self.draw_get_inv(self.inventory.inv[0], self.inventory.life[0])
            elif len(self.inventory.inv) >= 2 and self.inventory.life[1] >= 0:
                self.draw_get_inv(self.inventory.inv[1], self.inventory.life[1])
            elif len(self.inventory.inv) >= 3 and self.inventory.life[2] >= 0:
                self.draw_get_inv(self.inventory.inv[2], self.inventory.life[2])
            elif len(self.inventory.inv) >= 4 and self.inventory.life[3] >= 0:
                self.draw_get_inv(self.inventory.inv[3], self.inventory.life[3])
            elif len(self.inventory.inv) >= 5 and self.inventory.life[4] >= 0:
                self.draw_get_inv(self.inventory.inv[4], self.inventory.life[4])
            elif len(self.inventory.inv) >= 6 and self.inventory.life[5] >= 0:
                self.draw_get_inv(self.inventory.inv[5], self.inventory.life[5])
            elif len(self.inventory.inv) >= 7 and self.inventory.life[6] >= 0:
                self.draw_get_inv(self.inventory.inv[6], self.inventory.life[6])
            elif len(self.inventory.inv) >= 8 and self.inventory.life[7] >= 0:
                self.draw_get_inv(self.inventory.inv[7], self.inventory.life[7])
            else:
                self.function.error("You don't have Pokemon")
                self.in_attak = None
                Fuir = pygame.draw.rect(self.screen, (255, 255, 255), (90, 450, 80, 30))
                if pygame.mouse.get_pressed()[0] and Fuir.collidepoint(pygame.mouse.get_pos()):
                    self.Quit_fight()
                fuir = pygame.image.load('img/Fuir.png').convert_alpha()
                self.screen.blit(fuir, (90, 450))

    def draw_get_inv(self, item, life):
        draw_mypok = pygame.image.load('img/' + item + '.png').convert_alpha()
        draw_mypok = pygame.transform.scale(draw_mypok, (154, 154))
        draw_mypok = pygame.transform.flip(draw_mypok, True, False)
        self.screen.blit(draw_mypok, (100, 265))
        image = Image.new('RGB', (100, 30), color=(255, 255, 255))
        d = ImageDraw.Draw(image)
        if life > 50:
            d.text((10, 10), 'Life : ' + str(life) + '/100', fill=(50, 202, 50))
        elif life >= 20 and life <= 50:
            d.text((10, 10), 'Life : ' + str(life) + '/100', fill=(255, 105, 180))
        elif life < 20:
            d.text((10, 10), 'Life : ' + str(life) + '/100', fill=(255, 0, 0))
        d.textsize('Life : ' + str(life) + '/100')
        image.save('img/life_set.png')
        draw_image = pygame.image.load('img/life_set.png').convert_alpha()
        self.screen.blit(draw_image, (450, 385))

        draw_image_name = Image.new('RGB', (100, 30), color=(255, 255, 255))
        d_name = ImageDraw.Draw(draw_image_name)
        d_name.text((10, 10), item, fill=(135, 206, 250))
        draw_image_name.save('img/name_battle.png')
        draw_image_name_load = pygame.image.load('img/name_battle.png').convert_alpha()
        self.screen.blit(draw_image_name_load, (450, 355))

        self.item_battle()

    def draw_item(self, item, x, y, life):
        image = Image.new('RGB', (100, 30), color=(255, 255, 255))
        d = ImageDraw.Draw(image)
        if life > 50:
            d.text((10, 10), 'Life : ' + str(life) + '/100', fill=(50, 202, 50))
        elif life >= 20 and life <= 50:
            d.text((10, 10), 'Life : ' + str(life) + '/100', fill=(255, 105, 180))
        elif life < 20:
            d.text((10, 10), 'Life : ' + str(life) + '/100', fill=(255, 0, 0))
        d.textsize('Life : ' + str(life) + '/100')
        image.save('img/life.png')
        draw_image = pygame.image.load('img/life.png').convert_alpha()
        self.screen.blit(draw_image, (x + 80, y + 25))

        draw_image_name = Image.new('RGB', (100, 30), color=(255, 255, 255))
        d_name = ImageDraw.Draw(draw_image_name)
        d_name.text((10, 10), item, fill=(135, 206, 250))
        draw_image_name.save('img/name.png')
        draw_image_name_load = pygame.image.load('img/name.png').convert_alpha()
        self.screen.blit(draw_image_name_load, (x + 80, y))

        draw_image_poke = pygame.image.load("img/" + item + ".png")
        draw_image_poke = pygame.transform.scale(draw_image_poke, (65, 50))
        self.screen.blit(draw_image_poke, (x, y))

        Rectplace_close = pygame.draw.rect(self.screen, (255, 255, 255), (340, 480, 120, 60))
        close = pygame.image.load("img/close.png").convert_alpha()
        self.screen.blit(close, (340, 480))
        if pygame.mouse.get_pressed()[0] and Rectplace_close.collidepoint(pygame.mouse.get_pos()):
            self.change = False

    def item_battle(self):
        Fuir = pygame.draw.rect(self.screen, (255, 255, 255), (90, 450, 80, 30))
        if pygame.mouse.get_pressed()[0] and Fuir.collidepoint(pygame.mouse.get_pos()):
            self.Quit_fight()
        Change = pygame.draw.rect(self.screen, (255, 255, 255), (90, 485, 80, 30))
        if pygame.mouse.get_pressed()[0] and Change.collidepoint(pygame.mouse.get_pos()):
            self.change = True

        Capture = pygame.draw.rect(self.screen, (255, 255, 255), (90, 520, 80, 30))
        if pygame.mouse.get_pressed()[0] and Capture.collidepoint(pygame.mouse.get_pos()):
            self.capture()

        Attak = pygame.draw.rect(self.screen, (255, 255, 255), (470, 450, 210, 110))
        if pygame.mouse.get_pressed()[0] and Attak.collidepoint(pygame.mouse.get_pos()) or self.in_attak == False:
            self.attack()

        fuir = pygame.image.load('img/Fuir.png').convert_alpha()
        self.screen.blit(fuir, (90, 450))

        change = pygame.image.load('img/Change.png').convert_alpha()
        self.screen.blit(change, (90, 485))

        capture = pygame.image.load('img/Capture.png').convert_alpha()
        self.screen.blit(capture, (90, 520))

        change1 = pygame.image.load('img/charge1.png').convert_alpha()
        self.screen.blit(change1, (470, 450))

        change2 = pygame.image.load('img/charge2.png').convert_alpha()
        self.screen.blit(change2, (470, 520))

        change3 = pygame.image.load('img/charge3.png').convert_alpha()
        self.screen.blit(change3, (580, 450))

        change4 = pygame.image.load('img/charge4.png').convert_alpha()
        self.screen.blit(change4, (580, 520))



    def Change(self):
        menu = pygame.image.load("img/menu.jpg").convert_alpha()
        menu = pygame.transform.scale(menu, self.screen.get_size())
        self.screen.blit(menu, (0, 0))

        pokeball_img = Image.new('RGB', (120, 30), color=(255, 255, 255))
        draw_pokeball = ImageDraw.Draw(pokeball_img)
        draw_pokeball.text((120 / 4, 30 / 4), 'Pokéball : ' + str(self.inventory.pokeball), fill=(229, 100, 52))
        pokeball_img.save('img/pokeball.png')

        draw_pokeball_img = pygame.image.load('img/pokeball.png').convert_alpha()
        self.screen.blit(draw_pokeball_img, (350, 0))

        if len(self.inventory.inv) >= 1:
            self.draw_item(self.inventory.inv[0], 180, 140, self.inventory.life[0])
        if len(self.inventory.inv) >= 2:
            self.draw_item(self.inventory.inv[1], 180, 220, self.inventory.life[1])
        if len(self.inventory.inv) >= 3:
            self.draw_item(self.inventory.inv[2], 180, 305, self.inventory.life[2])
        if len(self.inventory.inv) >= 4:
            self.draw_item(self.inventory.inv[3], 180, 390, self.inventory.life[3])
        if len(self.inventory.inv) >= 5:
            self.draw_item(self.inventory.inv[4], 425, 140, self.inventory.life[4])
        if len(self.inventory.inv) >= 6:
            self.draw_item(self.inventory.inv[5], 425, 225, self.inventory.life[5])
        if len(self.inventory.inv) >= 7:
            self.draw_item(self.inventory.inv[6], 425, 305, self.inventory.life[6])
        if len(self.inventory.inv) == 8:
            self.draw_item(self.inventory.inv[7], 425, 390, self.inventory.life[7])


    def Quit_fight(self):
        self.in_attak = True
        self.in_fight = False
        self.change = False
        self.no_capture = False
        self.sound.create_sound('escape_pokemon.mp3')
        time.sleep(1.5)
        self.sound.create_sound('spawn_world.mp3')

    def capture(self):
        if self.inventory.pokeball >= 0:
            self.inventory.pokeball = self.inventory.pokeball - 1
            n = random.randint(1, 10)
            if n > 9:
                if len(self.inventory.inv) < 8:
                    self.inventory.add_inventory(self.pokemon[self.pokemon_number - 1])
                    self.Quit_fight()
                else:
                    self.errorMess = "No add inventory"
                    self.no_capture = True
            else:
                self.errorMess = "Capture as failed"
                self.no_capture = True
        else:
            self.errorMess = "You don't have Pokeball"
            self.no_capture = True

    def attack(self):
        if self.in_attak == True:
            n = random.randint(10, 25)
            self.life_battle = self.life_battle - n
            print("Life pokemon : " + str(self.life_battle))
            self.in_attak = False
            if self.life_battle <= 0:
                self.Quit_fight()
        else:
            n = random.randint(10, 35)
            if len(self.inventory.inv) >= 1 and self.inventory.life[0] >= 0:
                self.inventory.life[0] = self.inventory.life[0] - n
            elif len(self.inventory.inv) >= 2 and self.inventory.life[1] >= 0:
                self.inventory.life[1] = self.inventory.life[1] - n
            elif len(self.inventory.inv) >= 3 and self.inventory.life[2] >= 0:
                self.inventory.life[2] = self.inventory.life[2] - n
            elif len(self.inventory.inv) >= 4 and self.inventory.life[3] >= 0:
                self.inventory.life[3] = self.inventory.life[3] - n
            elif len(self.inventory.inv) >= 5 and self.inventory.life[4] >= 0:
                self.inventory.life[4] = self.inventory.life[4] - n
            elif len(self.inventory.inv) >= 6 and self.inventory.life[5] >= 0:
                self.inventory.life[5] = self.inventory.life[5] - n
            elif len(self.inventory.inv) >= 7 and self.inventory.life[6] >= 0:
                self.inventory.life[6] = self.inventory.life[6] - n
            elif len(self.inventory.inv) >= 8 and self.inventory.life[7] >= 0:
                self.inventory.life[7] = self.inventory.life[7] - n
            print('Attack pokemon to player : -' + str(n))
            self.in_attak = True

    def run(self, tmx_data, group, map, player, inventory):
        if config.Config.fight(self):
            self.tmx_data = tmx_data
            self.group = group
            self.map = map
            self.player = player
            self.inventory = inventory

            try:
                if self.in_fight == False:
                    self.get_fight()
                else:
                    self.for_fight()
                if self.change:
                    self.Change()
                if self.transition == True:
                    if self.transitionWait <= self.wait:
                        self.transitionWait = self.transitionWait + 1
                        transition = pygame.image.load('img/noir.jpg').convert_alpha()
                        transition = pygame.transform.scale(transition, self.screen.get_size())
                        self.transition = False
                        self.in_fight = True
                        return self.screen.blit(transition, (0, 0))
                if self.no_capture:
                    img = Image.new('RGB', (155, 30), color=(0, 0, 0))
                    d = ImageDraw.Draw(img)
                    d.text((10, 10), self.errorMess, fill=(255, 0, 0))
                    img.save('img/error.png')

                    draw_image = pygame.image.load("img/error.png")
                    self.screen.blit(draw_image, (350, 0))
            except:
                print('ERROR FIGHT')
