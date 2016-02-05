import urllib2
import ctypes
import re
import os

url = urllib2.urlopen("http://photography.nationalgeographic.com/photography/photo-of-the-day/")
read_url = url.read()
img = "http:" + re.sub(r'(.|\n)+?<div class="primary_photo">(.|\n)+?<img src="(.+?)"(.|\n)+', r'\3', read_url)

print img

url2 = urllib2.urlopen(img)
#saving image to current directory
my_dir = os.path.expanduser('~\\temp')
if not os.path.exists(my_dir):
    os.makedirs(my_dir)

with open('wallpaper.jpg', "wb") as f:
    f.write(url2.read())
os.rename("wallpaper.jpg", my_dir + '\\' + "wallpaper.jpg")
imagePath = my_dir + '\\' + 'wallpaper.jpg'
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
