import requests
import pandas as pd
from bs4 import BeautifulSoup
import zipfile
import urllib.request
from datetime import datetime
import os

column_name = "links"
sheet_url = "https://docs.google.com/spreadsheets/d/1Vf6jNCzb4e3FZLgU6ZgY-uKXLEpzBeVh2wVB0oBzh_Y/gviz/tq?tqx=out:csv"


def download_data_from_column(column_name_f, sheet_url_f):
    pic_weblinks = []
    data = pd.read_csv(sheet_url_f)
    for value in data[column_name_f].values:
        pic_weblinks.append(value)
        # print(f"Appending: {value}")
    return pic_weblinks


def fetch_picture_urls(img_links_f):
    pic_urls = []
    for img_link in img_links_f:
        # print(f"Fetching... {img_link}")
        r = requests.get(img_link)
        r_html = r.text
        soup = BeautifulSoup(r_html, features="html.parser")
        for img in soup.find_all("img", "tv-snapshot-image"):  # where img is the tag and the other is the name of class
            pic_urls.append(img.get("src"))  # or: pic_urls.append(img["src"])
    return pic_urls


def download(picture_urls_f):
    folder = "io/img_export"
    if not os.path.exists(folder):
        os.makedirs(folder)
    for picture_url in picture_urls_f:
        response = requests.get(picture_url)
        filename = picture_url.split("/")[-1]
        filepath = os.path.join(folder, filename)
        print(f"Downloading: {picture_url}")
        with open(filepath, "wb") as f:
            f.write(response.content)


def zip_it(picture_urls_f):
    timestamp = str(datetime.now()).replace(":", "-")
    with zipfile.ZipFile(f"tw-scrape-{timestamp}.zip", mode="w") as zf:
        # Download and add the images to the ZIP file
        print(f"Creating: tw-scrape-{timestamp}.zip")
        for picture_url in picture_urls_f:
            image_data = urllib.request.urlopen(picture_url).read()
            filename = picture_url.split("/")[-1]
            print(f"Packing: {filename}")
            zf.writestr(f'{filename}', image_data)


print("Starting...")

img_links = download_data_from_column(column_name, sheet_url)
# for link in img_links:
#    print(link)

picture_urls = fetch_picture_urls(img_links)
# for url in picture_urls:
#    print(url)

download(picture_urls)

zip_it(picture_urls)

print("Done!")
