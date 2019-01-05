Ownphotos Client
================
Lets you interact with an `Ownphotos <https://github.com/hooram/ownphotos>`_ backend server.


Example::

    #!/usr/bin/python3
    from ownphotos_client import OwnphotosAPI
    
    if __name__ == "__main__":    
        username = "admin"
        password = "admin"
        url= 'https://ownphotos.gnethomelinux.com/'
        a = OwnphotosAPI(url, username, password)
        print(a.avilable())
        for i in a.get_user_photos()["results"]:
            for cover in i["cover_photos"]:
                image_data = a.get_thumbnail(cover["image_hash"])
                with open("/tmp/" + cover["image_hash"] + ".jpg",'wb') as w:
                    w.write(image_data)
