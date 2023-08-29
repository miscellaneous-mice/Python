from PIL import Image


# alpha = Transparency value 0 to 255

im_rgb = Image.open('red_color.jpg')
im_rgba = im_rgb.copy()
im_rgba.putalpha(128)
im_rgba.save('saved/red_edited_1.png')

'''
# Converting png to jpg
blue = Image.open('blue_color.png')
blue_im = blue.convert('RGB')
blue_im.save('blue_color.jpg')
'''

blue = Image.open('blue_color.jpg')
blue_rgba = blue.copy()
blue_rgba.putalpha(128)
blue_rgba.save('saved/blue_edited_1.png')

# Overlaying images on top of other
blue_rgba.paste(im_rgba, box=(0,0), mask=im_rgba)
blue_rgba.save('saved/overlay.png')


