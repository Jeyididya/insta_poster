import requests
from PIL import Image
import os
class GET_IMAGE:
    def __init__(self):
        self.header={ "Authorization" : "563492ad6f91700001000001cdf5c4ba754b4bb1b220822ab9d8426b"}
        self.base_url="https://api.pexels.com/v1/"
    def save_image(self,image_url,image_name,photographer,color_code):
        # print(image_url)
        # print(image_name)
        # print(photographer)
        img = Image.open(requests.get(image_url, stream = True).raw)

        img.save('./downloads/{} b7 {}_{}.jpg'.format(image_name,photographer,color_code))
        return './downloads/{} b7 {}_{}.jpg'.format(image_name,photographer,color_code)
    
    def check_image_id(self,image_id):
        file_=open("image_id.txt","r").readlines()
        for id in file_:
            print(id," and ",image_id)
            if str(image_id)==str(id).strip():
                # print("---image used")
                return True
        
        open("image_id.txt","a").write(str(image_id)+"\n")
        print("found new image")
        return False



    def search_image(self,text,color=""):
        if color!="":
            search=self.base_url+"search?query={}&color={}&orientation=square".format(text,color)
        else:
            search=self.base_url+"search?query={}&orientation=square".format(text)

        response=requests.get(search,headers=self.header)

        for image in response.json()['photos']:
            # print("-->",images['alt'])
            # TODO check id of picture before downloading
            if not self.check_image_id(image["id"]):
                try:
                    # print("saved file->",self.save_image(image['src']['original'],image['alt'],image["photographer"],image["avg_color"]))
                    return self.save_image(image['src']['original'],image['alt'],image["photographer"],image["avg_color"])
                except:
                    continue
            
    # def test(self):
    #     search=self.base_url
    #     response=requests.get(search,headers=self.header)
    #     print("->",response)


# getImage=GET_IMAGE()
# getImage.search_image("friends")
# getImage.test()

