import random
import os
import io
import PIL.Image as Image
import base64
import pickle
import io
import random

header = {"signature" : b'BM', "File_Size" : b'0000', "Reserved1" : b'00', "Reserved2" : b'00', "Offset_pixel" : b'0000',

          "HeaderSize": b'0000',"ImageWidth": b'0000',"ImageHeight": b'0000',"Planes": b'00', "BitsPerPixel": b'00',
          "Compression": b'0000', "ImageSize": b'0000', "XpixelsPerMeter": b'0000', "YpixelsPerMeter": b'0000',
          "TotalColors": b'0000', "ImportantColors": b'0000'
          }

example_header = [66, 77,          #signature
                  102, 117, 0, 0,  #File_Size
                  0, 0,            #Reserved1
                  0, 0,            #Reserved2
                  54, 0, 0, 0,     #Offset_pixel
                  40, 0, 0, 0,     #HeaderSize
                  100, 0, 0, 0,    #ImageWidth
                  100, 0, 0, 0,    #ImageHeight
                  1, 0,            #Planes
                  24, 0,           #BitsPerPixel
                  ] + [0] * 24


example_header_bin = b''
for i in example_header:
    example_header_bin += i.to_bytes(1,"big")


def bin_pic():
    with open("pic.bmp", "rb") as file:
        return file.read()



# header = bin_pic()[:54]
# data = b""
# print(header)
#

data = b''
for i in range(30000):
     data += random.randint(0,255).to_bytes(2, "big")

new_data = example_header_bin + data


x = bin_pic()
for i in range(len(x)):
    print(x[i], new_data[i])

# with open("sea.bmp", "wb") as file:
#     file.write(new_data)


# for i in range(len(new_data)):
#     print(new_data[i])

image = io.BytesIO(new_data)
pillow = Image.open(image)
pillow.show()





