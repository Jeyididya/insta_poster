from instabot import Bot
from time import sleep

 
bot = Bot()
sleep(20)
bot.login(username="yididya051@gmail.com", password="0113470047",use_cookie=False)
 
# user_id = bot.get_user_id_from_username("lego")
# user_info = bot.get_user_info(user_id)
# print(user_info['biography'])
# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo


# bot.upload_photo("pic2.jpg",
#                  caption ="test 3")

import os
from time import sleep

for _,_,picture in os.walk("./test_pictures"):
    print(picture)
    for pic in picture:
        bot.upload_photo("./test_pictures/"+str(pic),
                    caption =str(pic))
        sleep(60)