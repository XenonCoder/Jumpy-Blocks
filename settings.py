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
* @create      dom 25 mar 2018 12:35:15 CEST
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""

# options/settings
TITLE = "Jumpy Blocks"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE
