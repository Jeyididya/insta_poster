from get_quotes import *
from get_image import *
from edit_photo import *

from instagram_api import *
import textwrap
from time import sleep

import random
import os

words=["friend","car","alone","lonely","sad","wealth"]

def check_text(quote):
    lines=textwrap.wrap(quote["quote"],56)
    if len(lines)<4:
        return True
    return False

def start():
    quote=QUOTE()
    get_image=GET_IMAGE()
    _quote=quote.get_quote()
    if check_text(_quote):
        file_name=get_image.search_image(random.choice(words))
        print(file_name,_quote["quote"])
        im=EDIT_IMAGE(file_name)
        file_name_edited=im.add_text(_quote["quote"],_quote["author"])
        os.remove(file_name)
        return file_name_edited
    else:
        start()

def post_insta(file_name,sleep_time):
    photographer=file_name.split("b7")[1].split("_")[0]
    caption="Photographer {},\nImage from Pexeles \nQuote from themotivate365\nnext post in {} hrs".format(photographer,sleep_time)
    cl.photo_upload(
        file_name, 
        caption
        )
    print("photo posted",file_name)
    os.remove(filename)

times=[10,13,11,6]


os.mkdir("downloads")
os.mkdir("photos")


while True:

    filename=start()
    sleep_time=random.choice(times)
    if filename!=None:
        post_insta(filename,sleep_time)
    else:
        continue
    print("sleeping for ",sleep_time)
    sleep(int(sleep_time)*3600)

