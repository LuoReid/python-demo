import random
from PIL import Image, ImageFilter, ImageFont, ImageDraw

im = Image.open('test.jpg')

w, h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w/2, h/2))
print('Resize image to %sx%s' % (w/2, h/2))
im.save('test_thumbnail.jpg', 'jpeg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('test_blur.jpg', 'jpeg')


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


w = 60*4
h = 60
im = Image.new('RGB', (w, h), (255, 255, 255))
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
draw = ImageDraw.Draw(im)
for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor2())
im = im.filter(ImageFilter.BLUR)
im.save('test_code.jpg', 'jpeg')
