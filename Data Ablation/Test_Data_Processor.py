import csv
import io
import os
import pandas as pd
from glob import glob
from PIL import Image, ImageEnhance
import random
import numpy as np
import shutil

""" 
author: Mehdi Mousavi
Fall 2018 
This code takes an Unreal Engine 4 raw screenshot folder with (image,depth) order, and processes each file for use in 
Densedepth.

 """

os.chdir('E:/')
dir_src = ('E:/Dataset/Dataset/Ablation_Final/')
DEPTH =   (dir_src + "Depth/")

PIC =     (dir_src + "Same_domain/")
PIC_imp =     (dir_src + "Same_domain_murky/")
PIC_nolight = (dir_src + "Same_domain_nolight/")

Clay =     (dir_src + "clay/")
Clay_imp =     (dir_src + "clay_murky/")
Clay_nolight = (dir_src + "clay_nolight/")

procedural =     (dir_src + "procedural/")
procedural_imp =     (dir_src + "procedural_murky/")
procedural_nolight = (dir_src + "procedural_nolight/")

cobble =     (dir_src + "cobble/")
cobble_imp =     (dir_src + "cobble_murky/")
cobble_nolight = (dir_src + "cobble_nolight/")

tile =     (dir_src + "tile/")
tile_imp =     (dir_src + "tile_murky/")
tile_nolight = (dir_src + "tile_nolight/")

bluepat =     (dir_src + "bluepat/")
bluepat_imp =     (dir_src + "bluepat_murky/")
bluepat_nolight = (dir_src + "bluepat_nolight/")

whitetile_irregular =     (dir_src + "irregular/")
whitetile_irregular_imp =     (dir_src + "irregular_murky/")
whitetile_irregular_nolight = (dir_src + "irregular_nolight/")

try:
    os.mkdir(DEPTH)
    os.mkdir(PIC)
    os.mkdir(PIC_imp)
    os.mkdir(PIC_nolight)

    os.mkdir(Clay)
    os.mkdir(Clay_imp)
    os.mkdir(Clay_nolight)

    os.mkdir(procedural)
    os.mkdir(procedural_imp)
    os.mkdir(procedural_nolight)

    os.mkdir(cobble)
    os.mkdir(cobble_imp)
    os.mkdir(cobble_nolight)

    os.mkdir(tile)
    os.mkdir(tile_imp)
    os.mkdir(tile_nolight)

    os.mkdir(bluepat)
    os.mkdir(bluepat_imp)
    os.mkdir(bluepat_nolight)

    os.mkdir(whitetile_irregular)
    os.mkdir(whitetile_irregular_imp)
    os.mkdir(whitetile_irregular_nolight)


except OSError:
        print('Directory not created.')



counter = 1
for filename in os.listdir(dir_src):

    if counter == 1:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, DEPTH)
            print("moved " + filename)
            counter = counter+1

    elif counter == 2:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, PIC)
            print("moved " + filename)
            counter = 3

    elif counter == 3:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, PIC_imp)
            print("moved " + filename)
            counter = 4

    elif counter == 4:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, PIC_nolight)
            print("moved " + filename)
            counter = 5

    elif counter == 5:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, Clay)
            print("moved " + filename)
            counter = 6

    elif counter == 6:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, Clay_imp)
            print("moved " + filename)
            counter = 7

    elif counter == 7:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, Clay_nolight)
            print("moved " + filename)
            counter = 8

    elif counter == 8:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, procedural)
            print("moved " + filename)
            counter = 9

    elif counter == 9:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, procedural_imp)
            print("moved " + filename)
            counter = 10

    elif counter == 10:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, procedural_nolight)
            print("moved " + filename)
            counter = 11

    elif counter == 11:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, cobble)
            print("moved " + filename)
            counter = 12

    elif counter == 12:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, cobble_imp)
            print("moved " + filename)
            counter = 13

    elif counter == 13:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, cobble_nolight)
            print("moved " + filename)
            counter = 14

    elif counter == 14:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, tile)
            print("moved " + filename)
            counter = 15

    elif counter == 15:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, tile_imp)
            print("moved " + filename)
            counter = 16

    elif counter == 16:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, tile_nolight)
            print("moved " + filename)
            counter = 17

    elif counter == 17:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, bluepat)
            print("moved " + filename)
            counter = 18

    elif counter == 18:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, bluepat_imp)
            print("moved " + filename)
            counter = 19

    elif counter == 19:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, bluepat_nolight)
            print("moved " + filename)
            counter = 20

    elif counter == 20:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, whitetile_irregular)
            print("moved " + filename)
            counter = 21

    elif counter == 21:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, whitetile_irregular_imp)
            print("moved " + filename)
            counter = 22

    elif counter == 22:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, whitetile_irregular_nolight)
            print("moved " + filename)
            counter = 1


#   ==================================================================        #


directory = [DEPTH, PIC, PIC_imp, PIC_nolight,Clay, Clay_imp, Clay_nolight, procedural,
             procedural_imp, procedural_nolight,cobble, cobble_imp, cobble_nolight, tile, tile_imp, tile_nolight,
             bluepat,bluepat_imp, bluepat_nolight, whitetile_irregular, whitetile_irregular_imp, whitetile_irregular_nolight]
for direc in directory:
    i = 0
    for filename in os.listdir(direc):
        os.rename(direc + '/' + filename, direc + '/' + str(i) + '.png')
        i = i + 1
        print("renamed " + filename)



for directory in [DEPTH, PIC, PIC_imp, PIC_nolight,Clay, Clay_imp, Clay_nolight, procedural,
             procedural_imp, procedural_nolight,cobble, cobble_imp, cobble_nolight, tile, tile_imp, tile_nolight,
             bluepat,bluepat_imp, bluepat_nolight, whitetile_irregular, whitetile_irregular_imp, whitetile_irregular_nolight]:

    for filename in os.listdir(directory):
        im = Image.open(directory + filename)
        im = im.convert('RGB')
        #im = im.resize((640, 480))


        im.save(directory + filename.replace('.png', '_final.png'), quality=100)
        print("processed " + filename)



for filename in os.listdir(DEPTH):
    depth = Image.open(DEPTH+filename)
    depth = depth.convert('L')
    #depth = depth.resize((640, 480))

    depth.save(DEPTH+filename.replace('.png', '_final.png'), quality=100)
    print("processed " + filename)