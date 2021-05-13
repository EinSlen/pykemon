import pygame
import pytmx
import pyscroll

from player import Player


# important:
# collision
# enter_house1 / enter_house_exit1 / exit_house1 / spawn_house1

class Game:

    def __init__(self):
        self.map = 'world'
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pykemon - Adventure")
        icon = pygame.image.load("img/icon.png")
        pygame.display.set_icon(icon)

        self.tmx_data = pytmx.util_pygame.load_pygame('map/map.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        print('NEW MAP Generate : ' + str(self.tmx_data))
        self.zoom = 2
        map_layer.zoom = self.zoom

        player_position = self.tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        self.walls = []

        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        print("Objets collision Générer : " + str(self.walls.__sizeof__()))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)
        self.enter_house()

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def switch_house(self, map_name, spawn_name, spawn_house):

        self.screen = pygame.display.set_mode((800, 600))
        self.tmx_data = pytmx.util_pygame.load_pygame('map/' + map_name + '.tmx')
        print('NEW MAP Generate : ' + map_name)
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = self.zoom

        self.walls = []

        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        print("Objets collision Générer : " + str(self.walls.__sizeof__()))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        enter_house = self.tmx_data.get_object_by_name(spawn_name)
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        spawn_house_point = self.tmx_data.get_object_by_name(spawn_house)
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20
        self.map = 'house'
        print('Change : ' + self.map)

    def switch_world(self, world_name, house_name, spawn_name):

        self.screen = pygame.display.set_mode((800, 600))
        self.tmx_data = pytmx.util_pygame.load_pygame('map/' + world_name + '.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        print('NEW MAP Generate : ' + world_name)
        map_layer.zoom = self.zoom

        self.walls = []

        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        print("Objets collision Générer : " + str(self.walls.__sizeof__()))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        enter_house = self.tmx_data.get_object_by_name(house_name)
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        spawn_house_point = self.tmx_data.get_object_by_name(spawn_name)
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20
        self.map = 'world'
        print('Change : ' + self.map)

    def enter_house(self):
        enter_house = self.tmx_data.get_object_by_name('enter_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)
        enter_house2 = self.tmx_data.get_object_by_name('enter_house2')
        self.enter_house_rect2 = pygame.Rect(enter_house2.x, enter_house2.y, enter_house2.width, enter_house2.height)
        enter_house3 = self.tmx_data.get_object_by_name('enter_house3')
        self.enter_house_rect3 = pygame.Rect(enter_house3.x, enter_house3.y, enter_house3.width, enter_house3.height)
        enter_world = self.tmx_data.get_object_by_name('enter_world2')
        self.enter_world_rect = pygame.Rect(enter_world.x, enter_world.y, enter_world.width, enter_world.height)

    def get_switch(self):

        for obj in self.tmx_data.objects:
            if obj.name == 'enter_house':
                if self.map == 'world' and self.player.feet.colliderect(self.enter_house_rect): self.switch_house('house1', 'exit_house', 'spawn_house')
            if obj.name == 'exit_house':
                if self.map == 'house' and self.player.feet.colliderect(self.enter_house_rect): self.switch_world('map', 'enter_house', 'enter_house_exit')
            if obj.name == 'enter_house2':
                if self.map == 'world' and self.player.feet.colliderect(self.enter_house_rect2): self.switch_house('house2', 'exit_house2', 'spawn_house2')
            if obj.name == 'exit_house2':
                if self.map == 'house' and self.player.feet.colliderect(self.enter_house_rect): self.switch_world('map', 'enter_house', 'enter_house_exit2')
            if obj.name == 'enter_house3':
                if self.map == 'world' and self.player.feet.colliderect(self.enter_house_rect3): self.switch_house('house3', 'exit_house3', 'spawn_house3')
            if obj.name == 'exit_house3':
                if self.map == 'house' and self.player.feet.colliderect(self.enter_house_rect): self.switch_world('map', 'enter_house', 'enter_house_exit3')


            if obj.name == 'enter_world2':
                if self.map == 'world' and self.player.feet.colliderect(self.enter_world_rect): self.switch_world('map2', 'exit_world2', 'spawn_world2')
            if obj.name == 'exit_world2':
                if self.map == 'world' and self.player.feet.colliderect(self.enter_house_rect): self.switch_world('map', 'enter_house', 'spawn_world1')



    def update(self):
        self.group.update()
        self.get_switch()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):

        clock = pygame.time.Clock()

        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
