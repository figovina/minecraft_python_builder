
from PIL import Image
with Image.open("buildings/test/1.bmp") as im:
    im.show()
    px = im.load()
print(px[0, 0])