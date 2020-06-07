import image
import lcd
import sensor
import sys
import time
import KPU as kpu
from fpioa_manager import *

import KPU as kpu


lcd.init()
lcd.rotation(2)

try:
    from pmu import axp192
    pmu = axp192()
    pmu.enablePMICSleepMode(True)
except:
    pass

try:
    img = image.Image("/sd/startup.jpg")
    lcd.display(img)
except:
    lcd.draw_string(lcd.width()//2-100,lcd.height()//2-4, "Error: Cannot find start.jpg", lcd.WHITE, lcd.RED)


task = kpu.load("/sd/a203c301b9a9e55d_mbnet10_quant.kmodel")

labels=["1","2","3"] #You can check the numbers here to real names.

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.run(1)

lcd.clear()


while(True):
    img = sensor.snapshot()
    fmap = kpu.forward(task, img)
    plist=fmap[:]
    pmax=max(plist)
    max_index=plist.index(pmax)
    a = lcd.display(img)
    if pmax > 0.95:
        lcd.draw_string(40, 60, "Accu:%.2f Type:%s"%(pmax, labels[max_index].strip()))
a = kpu.deinit(task)
