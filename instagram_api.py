from instagrapi import Client
import logs_

cl = Client()

cl.login("yididya051@gmail.com", "0113470047j")
# print("successfully logged in")
logs_.send_message("[+]Successfully Logged in")