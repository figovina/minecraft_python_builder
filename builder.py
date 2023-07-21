#-------------------------------------------------------------------------
#importing modules

from mcpi.minecraft import Minecraft
from PIL import Image
import time

#-------------------------------------------------------------------------
#settings

x_size = 64
z_size = 64
y_size = 3

x_min = 0
z_min = 0
y_min = 10

block_list = {
    (255, 255, 255) : 0,  # air
    (255, 0, 0) : 11,     # lava
    (0, 255, 0): 3,       # dirt
    (0, 0, 255): 9,       # water
    (255, 255, 0): 12,    # sand
    (0, 255, 255): 98,    # stone bricks
    (255, 0, 255): 80,    # snow block
    (0, 0, 0): 1          # stone

}

picture_list = [
    "1.bmp",
    "2.bmp",
    "3.bmp"
]

#-------------------------------------------------------------------------
#setup

mc = Minecraft.create()

x = 0
y = 0
z = 0

x_pos = 0
y_pos = 0
z_pos = 0

block = ""
rgb = ""

time_start = 0
time_stop = 0
time_all = 0

#-------------------------------------------------------------------------
#main program

time_start = time.time()

for y in range(0, y_size):

    with Image.open("E:/minecraft-spigot_server/building/%s" % picture_list[y]) as im:
        #im.show()
        px = im.load()

    y_pos = y_min + y

    for z in range(0, z_size):

        z_pos = z_min + z

        for x in range(0, x_size):

            x_pos = x_min + x

            rgb = px[x, z]
            block = block_list[rgb]

            mc.setBlock(x_pos, y_pos, z_pos, block)
            #print("set %s at X = %s, Y = %s, Z = %s" % (block, x_pos, y_pos, z_pos))

            time.sleep(0.01)

time_stop = time.time()
time_all = time_stop - time_start
print("building finished at %s seconds" % time_all)