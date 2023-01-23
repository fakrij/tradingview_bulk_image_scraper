import requests
import pandas as pd
from bs4 import BeautifulSoup

column_name = "links"
sheet_url = "https://docs.google.com/spreadsheets/d/1Vf6jNCzb4e3FZLgU6ZgY-uKXLEpzBeVh2wVB0oBzh_Y/gviz/tq?tqx=out:csv"


def download_data_from_column(column_name_f, sheet_url_f):
    pic_weblinks = []
    data = pd.read_csv(sheet_url_f)
    for value in data[column_name_f].values:
        pic_weblinks.append(value)
        # print("Appending: " + value)
    return pic_weblinks


def fetch_picture_urls(img_links_f):
    pic_urls = []
    for img_link in img_links_f:
        # print(f"Fetching... {img_link}")
        r = requests.get(img_link)
        r_html = r.text
        soup = BeautifulSoup(r_html, features="html.parser")
        for img in soup.find_all("img", "tv-snapshot-image"):  # where img is the tag and the other is the name of class
            pic_urls.append(img.get("src"))  # nebo: picture_links.append(img["src"])
    return pic_urls


def download(pic_urls):
    for picture_url in pic_urls:
        response = requests.get(picture_url)
        open(picture_url[-12:], "wb").write(response.content)
        print("Downloading: " + picture_url)


print("Starting...")

img_links = download_data_from_column(column_name, sheet_url)
# for link in img_links:
#    print(link)

picture_urls = fetch_picture_urls(img_links)
# for url in picture_urls:
#    print(url)

download(picture_urls)

print("Done!")
