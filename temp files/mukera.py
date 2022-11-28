
# import os
# from time import sleep

# for _,_,picture in os.walk("./test_pictures"):
#     print(picture)
#     bot.upload_photo(str(picture),
#                   caption =str(picture))
#     sleep(120)






# response= requests.get("https://api.pexels.com/v1/photos/2014422", headers={ "Authorization" : "563492ad6f91700001000001cdf5c4ba754b4bb1b220822ab9d8426b"})
# print(response.json()['src']['medium'])

# img_url = response.json()['src']['original']
# img = Image.open(requests.get(img_url, stream = True).raw)
# img.save('second.jpg')


# def save_image(image_url,image_name,photographer):
#     print(image_url)
#     print(image_name)
#     print(photographer)
#     img = Image.open(requests.get(image_url, stream = True).raw)
#     print("here")
#     img.save('./downloads/{} by {}.jpg'.format(image_name,photographer))

# def search_image(text):
#     base_url="https://api.pexels.com/v1/"
#     search=base_url+"search?query={}&color={}&orientation=square".format(text,"black")
#     response=requests.get(search,headers={ "Authorization" : "563492ad6f91700001000001cdf5c4ba754b4bb1b220822ab9d8426b"})
#     # print(response.json())
#     for images in response.json()['photos']:
#         print("-->",images['alt'])
#         save_image(images['src']['original'],images['alt'],images["photographer"])
# search_image("cars")    






# # Importing the PIL library
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
 
# # Open an Image
# img = Image.open('car.png')
 
# # Call draw Method to add 2D graphics in an image
# I1 = ImageDraw.Draw(img)
 
# # Custom font style and font size
# myFont = ImageFont.truetype('FreeMono.ttf', 65)
 
# # Add Text to an image
# I1.text((10, 10), "Nice Car", font=myFont, fill =(255, 0, 0))
 
# # Display edited image
# img.show()
 
# # Save the edited image
# img.save("car2.png")





# from instagrapi import Client
# import os
# from time import sleep
# cl = Client()
# cl.login("yididya051@gmail.com", "0113470047j")

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap
import colorsys
import os

# colorsys.hex_to_rgb()

# def write_pic(picture):
#     img = Image.open("./downloads/New folder/"+picture)
#     draw = ImageDraw.Draw(img)
#     # font = ImageFont.truetype(<font-file>, <font-size>)
#     font = ImageFont.truetype("OpenSans-Regular.ttf", 1050)
#     # draw.text((x, y),"Sample Text",(r,g,b))
#     draw.text((40, 800),"Sample Text",(255,255,255),font=font)
#     img.save('./edited/'+picture)
# for _,_,picture in os.walk("./downloads/New folder"):
#     for pic in picture:
#         print(pic)
#         write_pic(pic)
#     # sleep(60)

# for _,_,picture in os.walk("./downloads/New folder"):
#     print(picture)
#     for pic in picture:
#         # cl.photo_upload(
#         # "./test_pictures/"+str(pic),
#         # str(pic),
#         # )
#         print(pic)
#     # sleep(60)


# def get_dominant_color(pil_img):
#     img = pil_img.copy()
#     img = img.convert("hex")
#     img = img.resize((1, 1), resample=0)
#     dominant_color = img.getpixel((0, 0))
#     return dominant_color


# import math
# from colors import rgb_to_hsl,hsl_to_rgb


# img = Image.open("tested.jpg")
# r,g,b=get_dominant_color(img)
# print(r,g,b)
# h,s,l=rgb_to_hsl(r/255,g/255,b/255)
# print("->",h,s,l)


# if h<180:
#     h+=180
# else:
#     h-=180

# print("h",h)
# r,g,b=hsl_to_rgb(h, s, l)
# print("changed",r*255,g*255,b*255)



def write_text(image,text):
    width_im, height = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./fonts/ugly_betty.ttf", width_im//32)
    lines=textwrap.wrap(text,56)
    print(lines)
    y_text=height//2+height//6
    for line in lines:
        width, height = font.getsize(line)
        draw.text(((width_im - width) / 2, y_text), line, font=font, fill=(255,255,255),stroke_fill=(0,0,0),stroke_width=5,alight="center")
        y_text += height
    # xy=draw.text((0, 0),line,(200,0,120),font=font,align="center")

    img.save("./examples/edited.jpg")

text="While we wait for life, life passes."

img = Image.open("first.jpg")
write_text(img, text)

# for _,_,fonts in os.walk("./fonts"):
#     for font in fonts:
        