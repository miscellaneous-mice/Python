from PIL import Image

mask = Image.open('mask.png')

message = Image.open('word_matrix.png')

print(mask.size)
print(message.size)

'''
(width, height)
(505, 251) mask size
(1015, 559) message size
'''
mask_width = mask.size[0]
mask_height = mask.size[1]
message_width = message.size[0]
message_height = message.size[1]

# mask_resize_width = mask_width * (message_width/mask_width)
# mask_resize_height = mask_height* (message_height/mask_height)

mask.putalpha(128)

mask_code = mask.resize((message_width, message_height))
message.paste(mask_code, box=(0,0), mask=mask_code)
message.save("saved/exercise.png")

