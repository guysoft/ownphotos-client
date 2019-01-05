import requests


class OwnphotosAPI():
    def __init__(self,url, username, password):
        self.url = url
        self.url_api = url + "/api"
        self.url_media = url + "/media"
        self.username = username
        self.password = password
        self.login()
        
    def login(self):
        r = requests.post(self.url_api + '/auth/token/obtain/', data = {'username': self.username,
                                                      'password': self.password})
        data = r.json()
        
        self.refresh = data["refresh"]
        self.access = data["access"]
        self.cookies = {"jwt": self.access,
           "csrftoken": self.refresh}
        self.headers = {"Authorization": "Bearer " + self.access}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.7,he;q=0.3',
            'Referer': 'https://pics.gnethomelinux.com/',
            'Authorization': 'Bearer ' + self.access,
            'TE': 'Trailers',
            }
    def avilable(self):
        response = requests.get(self.url_api + '/rqavailable/', headers=self.headers)
        return response.json()
    
    def get_photos_no_timestamp(self):
        response = requests.get(self.url_api + '/photos/notimestamp/list/', headers=self.headers, cookies=self.cookies)
        return response.json()
    
    def get_user_photos(self):
        response = requests.get(self.url_api + '/albums/user/list/', headers=self.headers, cookies=self.cookies)        
        return response.json()
    
    def get_thumbnail(self, img_hash):
        response = requests.get(self.url_media + '/square_thumbnails/' + img_hash + '.jpg', headers=self.headers, cookies=self.cookies)
        return response.content
        





