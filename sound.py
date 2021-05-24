import pygame

class Sound:

    def __init__(self):
        print('SOUND LOADED')

    def create_sound(self, sound):
        pygame.mixer.music.load('sound/' + sound)
        pygame.mixer.music.play(0)
        print('SOUND PLAYED : ' + sound)
