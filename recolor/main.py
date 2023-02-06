import sys
from PIL import Image
from palette import *
from palette_test import *
from util import *
from transfer import *

if __name__ == '__main__':
    if len(sys.argv) > 1:
        image_name = sys.argv[1]
    else:
        image_name = 'chest.png'

    image = Image.open(image_name)
    print(image_name, image.format, image.size, image.mode)

    image_lab = rgb2lab(image)
    palette = build_palette(image_lab, 5)
    new_palette = palette.copy()
    new_palette[0] = (0,0,0)
    image_lab_m = image_transfer(image_lab, palette, new_palette, sample_level=10, luminance_flag=0)
    image_rgb_m = lab2rgb(image_lab_m)
    image_rgb_m.show()
    # pilimage = Image.fromarray(image_rgb_m)
    # pilimage.show()

    #lab = rgb2lab(image)
    #palette_argument_test(lab).show()
