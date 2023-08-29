from PIL import Image

mac = Image.open('example.jpg')

print("Type of file is {}".format(type(mac)))

# print(mac.show())

print("Size of image Width x Height : {}".format(mac.size))
print("file name : {}".format(mac.filename))

print("Format {}".format(mac.format_description))

print("\nCropping Images")
mac_cropped = mac.crop((0, 0, 100, 100)) # Starting and ending co-ordinates
mac_cropped.save("saved/mac_edited_1.jpg")

pencils  = Image.open('pencils.jpg')

print("\n")
print(pencils)
print(pencils.size)


x = 0
y = 0

width = 1950 / 3 # Grabbing 30% of width
height = 1300 / 10

pencils_cropped = pencils.crop((x, y, width, height))
pencils_cropped.save("saved/pencils_edited_1.jpg")


x = 0
y = 1100

width = 1950 / 3 # Grabbing 30% of width
height = 1300

pencils_cropped = pencils.crop((x, y, width, height))
pencils_cropped.save("saved/pencils_edited_2.jpg")


halfway = 1993/2
x = halfway - 200
y = 800

width = halfway + 200
height = 1257

mac_cropped = mac.crop((x, y, width, height))
mac_cropped.save("saved/mac_edited_2.jpg")

print("\nPasting the cropped image into another image")
mac.paste(im=mac_cropped, box=(0,0))
mac.save("saved/mac_edited_3.jpg")

mac.paste(im=mac_cropped, box=(796,0))
mac.save("saved/mac_edited_4.jpg")

print("\nresize")
mac_expanded = mac.resize((3000, 500))
mac_expanded.save("saved/mac_edited_5.jpg")

print("\nRotate")
mac_rotated = mac.rotate(90)
mac_rotated.save("saved/mac_edited_6.jpg")

