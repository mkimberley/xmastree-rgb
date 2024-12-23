from tree import RGBXmasTree
from colorzero import Color
import random
import logging
from time import sleep
from colorzero import Color, Hue

tree = RGBXmasTree()

colors = [Color('red'), Color('green'), Color('blue')] # add more if you like


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

try:
    while True:
        print("Start of sequence...")
        i = 0

        logging.info('Statring RGB cycle...')
        while i < 2:
            for color in colors:
                for pixel in tree:
                    pixel.color = color
            i += 1

        i = 0

        logging.info('Starting one by one...')
        while i < 2:
            for color in colors:
                tree.color = color
                sleep(1)
            i += 1

        i = 0

        tree.color = Color('red')

        logging.info('Statring hue cycle...')
        
        while i < 96:
            tree.color += Hue(deg=1)
            i += 1

        i = 0

        logging.info('Starting random sparkle...')

        while i < 96:
            pixel = random.choice(tree)
            pixel.color = random_color()
            i += 1
except KeyboardInterrupt:
    tree.close()


