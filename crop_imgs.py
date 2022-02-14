from PIL import Image
import os

for img in os.listdir(pth):
    if img.endswith('png'):
        print(img)
        
        impth = os.path.join(pth, img)
        opth = os.path.join(pth, f'cropped_{img}')
    im = Image.open(impth)

    # Setting the points for cropped image
    left = 127
    top = 67
    right = 621
    bottom = 522

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    # Shows the image in image viewer
    im1.save(opth)
