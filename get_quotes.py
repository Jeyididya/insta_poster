import requests

class QUOTE:
    def __init__(self):
        self.api="https://api.themotivate365.com/stoic-quote"

    def get_quote(self):
        response=requests.get(self.api).json()
        return response


# quo=QUOTE()
# print(quo.get_quote())
