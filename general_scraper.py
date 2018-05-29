import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

#base_url = "http://web.mit.edu/jesstess/www/scraper_test/"
base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod"

to_visit = set((base_url,))
visited = set()

while to_visit:
    # Pick a link to visit
    current_page = to_visit.pop()
    # Visit the link
    print("visiting: ", current_page)
    visited.add(current_page)
    content = urllib.request.urlopen(current_page).read()

    # Extract any new links from that page
    for link in BeautifulSoup(content,"lxml").findAll("a"):
        absolute_link = urljoin( current_page, link["href"])
        if absolute_link not in visited:
            print("Haven't visited, so adding: ", absolute_link)
            to_visit.add(absolute_link)
        else:
            print("Already visited: ", absolute_link)

    # Download any images on that page
    for img in BeautifulSoup(content,"lxml").findAll("img"):
        img_href = urljoin(current_page, img["src"])
        print ("Downloading: ", img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory,img_name))