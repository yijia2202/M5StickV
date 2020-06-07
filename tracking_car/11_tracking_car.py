# Untitled - By: 37189 - 周三 3月 11 2020

import sensor, image, lcd
import sys
from machine import UART
from fpioa_manager import *
from pmu import axp192
import os

pmu = axp192()
pmu.enablePMICSleepMode(True)

fm.register(board_info.CONNEXT_B,fm.fpioa.UART1_TX)  #CONNEXT_B---G34---白
fm.register(board_info.CONNEXT_A,fm.fpioa.UART1_RX)  #CONNEXT_A---G35---黄
uart = UART(UART.UART1, 9600, 8, None, 1, timeout=1000, read_buf_len=4096)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
lcd.init(freq=15000000)
lcd.rotation(2)

i=0

while(True):
    img = sensor.snapshot()
    tag = img.find_apriltags()
    i=i%5
    if tag:
        img.draw_rectangle(tag[0].rect(), color = (255, 0, 0))
        print(tag[0].x_translation(),',', tag[0].z_translation())
        if(i==0):
            if(tag[0].x_translation()<=-1):
                uart.write('left\0')
                print('left')
            if(tag[0].x_translation()>=1):
                uart.write('right\0')
                print('right')
            if (tag[0].z_translation()>=-3.5):
                uart.write('slow\0')
            if (tag[0].z_translation()<=-6):
                uart.write('quick\0')
    else:
        uart.write(b"lost\0")

    lcd.display(img)
    i=i+1
