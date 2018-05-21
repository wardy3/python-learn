# From the APOD archive, follow each link, find the image, download the image

# Concepts
# 1) download stuff => urllib
# 2) parse html and links => BeautifulSoup

# download Index https://apod.nasa.gov/apod/archivepix.html
# for each link on index page, 
#   follow the link and pull down the image on the linked page

import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Download index page
base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod"
content  = urllib.request.urlopen(base_url).read()

# For each link on the index page
for link in BeautifulSoup(content,"lxml").findAll("a"):
    print ("Following link:", link)
    href = urljoin( base_url, link["href"] )

    # Follow the link and pull down the image on that linked page
    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content,"lxml").findAll("img"):
        img_href = urljoin( href, img["src"])

        print("Downloading: ",img_href)

        img_name = img_href.split("/")[-1]

        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))