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
# resp=requests.get("https://images.pexels.com/photos/3573351/pexels-photo-3573351.png")


import sqlite3


def convert2Blob(filename):
        with open(filename, 'rb') as file:
                blobData = file.read()  
        return blobData

conn=sqlite3.connect("inspho.db")
curs=conn.cursor()
# sql="CREATE TABLE IF NOT EXISTS photos(id INT PRIMARY KEY,photo BLOB)"
# curs.execute(sql)

# sql1="INSERT INTO photos (id,photo) VALUES(?,?)"
# curs.execute(sql1,(1,convert2Blob("123.jpg")))
# conn.commit()


sql_fetch_blob_query = """SELECT * from photos where id = 1"""
for row in curs.execute(sql_fetch_blob_query):
        img=row[1]


cl.photo_upload(
        img, 
        "caption1231"
        )
# image=Image.open(BytesIO(img))

# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype("./fonts/ugly_betty.ttf", 120)
# draw.text((120, 120), "-hello there", font=font, fill=(255,0,0),
#         stroke_fill=(255,255,255),stroke_width=5)
# image.save("test2.jpg")

