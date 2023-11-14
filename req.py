import requests

class API_Request:
    def __init__(self, conf):
        self.url = "https://developer-lostark.game.onstove.com/"
        self.jwt = conf["API_Key"]["JWT"]
        self.headers = {
                "accept": "application/json",
                "authorization": "bearer {}".format(self.jwt),
                "content-Type": "application/json"
        }
    
    def request(self, req):
        url = "{}{}".format(self.url, req)
        resp = requests.get(url, headers = self.headers)
        return resp.text
