import os
import sys
import time
import random
from pykeyboard import PyKeyboard
from Probe.Core.Probe_utils import Probe, WindowMgr, KeyUtils

ku = KeyUtils()
p = Probe()
k = PyKeyboard()

WINDOWS = 'win32'
if sys.platform == WINDOWS:
    # In Windows, we can use the class defined above
    w = WindowMgr()
    w.find_window_wildcard(".*(64-bit Development PCD3D_SM5)")
    #w.find_window_wildcard(".*64-bit/Windows")
    w.set_foreground()

imageset = 4


def gen_settings():

    light = random.randint(0,1)
    cam = random.randint(0,1)
    capsule = random.randint(0,1)

    if light == cam == capsule == 0:
        gen_settings()

    return light,cam,capsule


def data_ablation():
    p.stop()
    p.depth()
    time.sleep(0.1)
    p.screenshot()
    p.depth()
    time.sleep(0.1)
    
    for mat in range(0,5):
        p.changemat()                                              
        time.sleep(0.1)
        p.screenshot()
        time.sleep(0.1)
        p.murky()
        time.sleep(0.1)
        p.screenshot()
        p.no_light()
        time.sleep(0.1)
        p.screenshot()

        p.murky()
        time.sleep(0.1)
        p.no_light()
        time.sleep(0.1)
    p.stop()


old_setting = "000"     # For Comparing the settings, so we can discard a repeated one.

time.sleep(4)

for image in range(imageset):

    light, cam, capsule = gen_settings()
    new_setting = str(light)+str(cam)+str(capsule)

    if (old_setting == new_setting):
        light, cam, capsule = gen_settings()
        new_setting = str(light) + str(cam) + str(capsule)

    else:

        print("settings," + " light" + str(light) + ",camera" + str(cam) + ",capsule" + str(capsule))

        if light:
            p.rotate_lights()                

        if cam:
            p.camera()

        if capsule:
            p.capsule()

        if random.randint(0,4) == 4:
            k.tap_key('a',2)
            k.tap_key('x',2)

        time.sleep(0.1)
        for frame in range(26):

            if random.randint(0,1) == 1:

                p.camrotate()
                data_ablation()

            else:

                data_ablation()


        old_setting = new_setting

        p.reset_scene()
        time.sleep(.5)