import mcpi.minecraft as minecraft
import mcpi.block as block
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200,timeout=1)
if ser.isOpen == False:
    ser.open()

mc = minecraft.Minecraft.create()
GAP = block.AIR.id
WATER_FLOWING = block.WATER_FLOWING.id
SAND = block.SAND.id

try:
    while True:
        line = ser.readline()
        if(line[0:3] == b'got'):
            line=line.strip()
            #print(line)
            cors=line.split()
            num=int(cors[1])
            x=float(cors[2])
            y=float(cors[3])
            z=float(cors[4])
            #print(x, y, z)
            pos = mc.player.getTilePos()
            if(num==1):
                mc.setBlock((int)(pos.x+x), int(pos.y+y), int(pos.z+z), WATER_FLOWING)
            if(num==2):
                mc.setBlock((int)(pos.x+x), int(pos.y+y), int(pos.z+z), SAND)
            print((int)(pos.x+x), (int)(pos.y+y), (int)(pos.z+z))

except KeyboardInterrupt:
    ser.close()
