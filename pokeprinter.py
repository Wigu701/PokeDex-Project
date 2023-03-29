import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sys

def printimage(name, imagepath):
    imagesource = imagepath + '/' + name

    if not os.path.exists(imagesource):
        return 0
    
    images = os.listdir(imagesource)
    image = np.floor(np.random.rand() * len(images))
    plt.imshow(image)

    return 1


def printstats(name, data):
    index = data['name'].get_loc(name)

    stats = data.iloc[index]
    print('\t\t', stats['name'].upper())
    print('HP: ', stats['hp'])
    print('HP: ', stats['hp'])
    print('HP: ', stats['hp'])
    print('HP: ', stats['hp'])
    print('HP: ', stats['hp'])


def pokeprinter(name, imagepath, data):
    if not printimage(name, imagepath):
        return 0
    
    printstats(name, data)

    return 1

    
