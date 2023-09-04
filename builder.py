#-------------------------------------------------------------------------
#importing modules

from mcpi.minecraft import Minecraft
from PIL import Image
import time

#-------------------------------------------------------------------------
#settings

x_size = 64
z_size = 64

x_min = 0
z_min = 0
y_min = 0

build_mode = 1    # 1 - set one block, 2 - set line

building_folder_name = "test"

enable_blacklist = True # note: blacklist works only if build mode set to 1

sleep_time = 1 # in seconds. change at your own risk. note: works only if build mode set to 2

block_black_list = [
    (255, 255, 255)#,
    #(0, 0, 255)
]

picture_list = [
    "1.bmp",
    "2.bmp",
    "3.bmp"
]

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

#-------------------------------------------------------------------------
#setup

mc = Minecraft.create()

x = 0
y = 0
z = 0

x_pos = 0
y_pos = 0
z_pos = 0
x_pos1 = 0
x_pos2 = 0
x_comp = x_size - 1

x_list = []
last_rgb = (0, 0, 0)

y_size = len(picture_list)

block = ""
rgb = ""

verify_number = 0
black_list_length = len(block_black_list)
verify_result = 0

time_start = 0
time_stop = 0
time_all = 0

#-------------------------------------------------------------------------
#build functions


def setblock():
    global x
    global y
    global z
    global x_pos
    global y_pos
    global z_pos
    global x_min
    global y_min
    global z_min
    global verify_result
    global verify_number
    global block_black_list
    global block
    global rgb

    x_pos = x_min + x
    y_pos = y_min + y
    z_pos = z_min + z

    rgb = px[x, z]
    block = block_list[rgb]

    if enable_blacklist:
        for verify_number in range(0, black_list_length):
            if rgb == block_black_list[verify_number]:
                pass
            else:
                verify_result = verify_result + 1

        if verify_result == black_list_length:
            mc.setBlock(x_pos, y_pos, z_pos, block)
            verify_result = 0
            time.sleep(0.01)
        else:
            verify_result = 0
    else:
        mc.setBlock(x_pos, y_pos, z_pos, block)
        time.sleep(0.01)


def setblocks():
    global x
    global y
    global z
    global x_pos1
    global x_pos2
    global y_pos
    global z_pos
    global x_min
    global y_min
    global z_min
    global last_rgb
    global x_list
    global block
    global rgb
    global x_comp
    global sleep_time

    y_pos = y_min + y
    z_pos = z_min + z

    rgb = px[x, z]

    if rgb == last_rgb and x < x_comp:
        x_list.append(x)
    else:
        block = block_list[last_rgb]

        last_rgb = rgb
        if x_list == []:
            x_pos1 = x_min + x
            x_pos2 = x_min + x
            mc.setBlocks(x_pos1, y_pos, z_pos, x_pos2, y_pos, z_pos, block)
            x_list = []
            time.sleep(sleep_time)
        else:
            x_pos1 = x_min + x_list[0]
            x_pos2 = x_min + x_list[(len(x_list) - 1)] + 1
            mc.setBlocks(x_pos1, y_pos, z_pos, x_pos2, y_pos, z_pos, block)
            x_list = []
            time.sleep(sleep_time)
        return block


#-------------------------------------------------------------------------
#main program


time_start = time.time()

for y in range(0, y_size):

    with Image.open("buildings/%s/%s" % (building_folder_name, picture_list[y])) as im:
        #im.show()
        px = im.load()

    for z in range(0, z_size):
        for x in range(0, x_size):

            if build_mode == 1:
                setblock()
            elif build_mode == 2:
                setblocks()

            else:
                print('''check and correct 'build_mode' parameter''')

time_stop = time.time()
time_all = time_stop - time_start
print("building finished at %s seconds" % time_all)
