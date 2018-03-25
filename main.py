#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

      #                               ######
      # #    # #    # #####  #   #    #     # #       ####   ####  #    #  ####
      # #    # ##  ## #    #  # #     #     # #      #    # #    # #   #  #
      # #    # # ## # #    #   #      ######  #      #    # #      ####    ####
#     # #    # #    # #####    #      #     # #      #    # #      #  #        #
#     # #    # #    # #        #      #     # #      #    # #    # #   #  #    #
 #####   ####  #    # #        #      ######  ######  ####   ####  #    #  ####

                         +-+-+ +-+-+-+-+-+-+-+-+-+-+
                         |b|y| |X|e|n|o|n|C|o|d|e|r|
                         +-+-+ +-+-+-+-+-+-+-+-+-+-+

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
* @name        Jumpy Blocks
* @copyright   (c) 2018 Stefano Peris
* @author      Stefano Peris
* @email       xenon77.dev@gmail.com
* @github      https://github.com/XenonCoder/Jumpy-Blocks
* @license     GPL-3.0 (https://www.gnu.org/licenses/gpl-3.0.en.html)
* @create      dom 25 mar 2018 12:15:16 CEST
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

# import libraries
import pygame as pg
import random

# import modules
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def events(self):
        # game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
