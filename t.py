# a="EDIT Silhouette of Man Standing on Hallway b7 Vojtech Okenka_#2F313B"


# def save_image():
#     # print("name->",self.image_path.split("/")[-1])
#     # self.image.save("./photos/EDIT "+self.image_path.split("/")[-1])
#     return "./photos/EDIT "+a.split("/")[-1]
#     print("saved")


# # a=a.split("b7")[1].split("_")[0]
# print(save_image())

from PIL import Image,ImageDraw, ImageFont
from instagram_api import *
import requests
from io import BytesIO
resp=requests.get("https://images.pexels.com/photos/3573351/pexels-photo-3573351.png")
image=Image.open(BytesIO(resp.content))

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("./fonts/ugly_betty.ttf", 120)
draw.text((120, 120), "-hello there", font=font, fill=(255,0,0),
        stroke_fill=(255,255,255),stroke_width=5)
image.save("test2.png")

cl.photo_upload(
        BytesIO(image), 
        "pl"
        )
