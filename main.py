from get_quotes import *
from get_image import *
from edit_photo import *

# from instagram_api import *
import textwrap
from time import sleep


import random

words=["friend","car","alone","lonely","sad","wealth"]

# def check_text(quote):
#     lines=textwrap.wrap(quote["quote"],56)
#     if len(lines)<4:
#         return True
#     return False

# def start():
#     quote=QUOTE()
#     get_image=GET_IMAGE()
#     _quote=quote.get_quote()
#     if check_text(_quote):
#         file_name=get_image.search_image(random.choice(words))
#         print(file_name,_quote["quote"])
#         im=EDIT_IMAGE(file_name)
#         file_name_edited=im.add_text(_quote["quote"],_quote["author"])
#         return file_name_edited
#     else:
#         start()

# def post_insta(file_name):
#     photographer=file_name.split("b7")[1].split("_")[0]
#     caption="Photographer {},\nImage from Pexeles \nQuote from themotivate365".format(photographer)
#     cl.photo_upload(
#         file_name, 
#         caption
#         )
#     print("photo posted",file_name)

# times=[10,13,11,6]

# while True:
#     # file_=open("image_id.txt","r").readlines()
#     # for id in file_:
#     #     print("id",id)
#     filename=start()

#     if filename!=None:
#         post_insta(filename)
#     sleep_time=random.choice(times)
#     print("sleeping for ",sleep_time)
#     sleep(int(sleep_time)*3600)

get_image=GET_IMAGE()
import os
os.mkdir("downloads")

print("-->GOT",get_image.search_image("friends"))


print(os.listdir("."))
