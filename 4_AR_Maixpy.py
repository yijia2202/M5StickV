# Untitled - By: 37189 - 周日 3月 15 2020

import sensor, image, time, lcd
from pmu import axp192

pmu = axp192()
pmu.enablePMICSleepMode(True)


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
lcd.init()
lcd.rotation(2)
clock = time.clock()

while(True):
    img = sensor.snapshot()

    for tag in img.find_apriltags(): # defaults to TAG36H11 without "families".
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))

        print("got",tag.id(),tag.x_translation(),
            tag.y_translation(),tag.z_translation())
    lcd.display(img)
