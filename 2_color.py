# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

import sensor, image, time, lcd
from pmu import axp192

pmu = axp192()
pmu.enablePMICSleepMode(True)

lcd.init(freq=15000000)
lcd.rotation(2)

sensor.reset()                      # Reset and initialize the sensor. It will
                                    # run automatically, call sensor.run(0) to stop
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
green_threshold  = (0, 80, -70, -13, -20, 13)
#(Lmin, Lmax, Amin, Amax, Bmin, Bmax)

while(True):
    img = sensor.snapshot()         # Take a picture and return the image.
    blobs = img.find_blobs([green_threshold])
    if blobs:
        for b in blobs:             #枚举所有的blob
            img.draw_rectangle(b[0:4]) #from b[0] - b[3]
    lcd.display(img)                # Display on LCD

