
from PIL import Image
with Image.open("E:/minecraft-spigot_server/building/1.bmp") as im:
    im.show()
    px = im.load()
print(px[0, 0])