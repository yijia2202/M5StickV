# Untitled - By: 37189 - 周日 3月 15 2020

import sensor, image
with open("playwav.py") as f:
    exec(f.read())
from pmu import axp192

pmu = axp192()
pmu.enablePMICSleepMode(True)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
lcd.init()
lcd.rotation(2)

while(True):
    img = sensor.snapshot()
    for tag in img.find_apriltags(): # defaults to TAG36H11 without "families".
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
        degress = 180 * tag.rotation() / 3.1415926
        print(tag.id(),degress)
        print(tag.x_translation())
        print(tag.y_translation())
        print(tag.z_translation())
        print(tag.x_rotation())
        print(tag.y_rotation())
        print(tag.z_rotation())
        if(tag.id() == 1):
            play_wav("/sd/1.wav")
        if(tag.id() == 2):
            play_wav("/sd/2.wav")
        if(tag.id() == 3):
            play_wav("/sd/3.wav")
        if(tag.z_translation()>-5):
            play_wav("/sd/front.wav")
            break
        if(tag.x_translation()<0):
            play_wav("/sd/left.wav")
        else:
            play_wav("/sd/right.wav")
        if(tag.y_translation()>0):
            play_wav("/sd/up.wav")
        else:
            play_wav("/sd/down.wav")

    lcd.display(img)
