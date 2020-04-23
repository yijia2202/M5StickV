# Untitled - By: 37189 - 周一 4月 6 2020

import sensor,image,lcd
import KPU as kpu
with open("/sd/playwav.py") as f:
    exec(f.read())
from pmu import axp192

pmu = axp192()
pmu.enablePMICSleepMode(True)

lcd.init()
lcd.rotation(2)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_hmirror(0)
sensor.run(1)
task = kpu.load(0x300000)

anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987,
        5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

while(True):
    img = sensor.snapshot()
    code = kpu.run_yolo2(task, img)
    if code:
        for i in code:
            a = img.draw_rectangle(i.rect())
        play_wav("/sd/welcome.wav")
    a = lcd.display(img)
a = kpu.deinit(task)
