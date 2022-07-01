import requests, random

def downloadNewWallpaper():
    '''
    Download a new wallpaper for new questions
    '''
    #Getting search results
    wallpaper_req = requests.get('https://imsea.herokuapp.com/api/1?q=aesthetic laptop wallpaper').json()

    #Choosing an image
    wallpaper_link = wallpaper_req["results"][random.randint(0, 91)]

    #Downloading the image
    wallpaper_img = requests.get(wallpaper_link, allow_redirects=True)
    open('th.jpg', 'wb').write(wallpaper_img.content)