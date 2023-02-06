import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import zipfile
import os
from datetime import datetime

column_name = "links"
sheet_url = "https://docs.google.com/spreadsheets/d/1Vf6jNCzb4e3FZLgU6ZgY-uKXLEpzBeVh2wVB0oBzh_Y/gviz/tq?tqx=out:csv"
timestamp = (str(datetime.now()).replace(":", "-"))[:-7]

# ---------------------------------------------------------------------------------------------- FUNKCE


def download_data_from_column(column_name_f, sheet_url_f):
    pic_weblinks = []
    data = pd.read_csv(sheet_url_f)
    for value in data[column_name_f].values:
        pic_weblinks.append(value)
        print(f"Appending: {value}")
    return pic_weblinks


def fetch_picture_urls(img_links_f):
    pic_urls = []
    for img_link in img_links_f:
        print(f"Fetching... {img_link}")
        r = urllib.request.urlopen(img_link)
        r_html = r.read()
        soup = BeautifulSoup(r_html, features="html.parser")
        for img in soup.find_all("img", "tv-snapshot-image"):
            pic_urls.append(img.get("src"))
    return pic_urls


def download(picture_urls_f, timestamp_f):
    folder = os.path.join(f"io/tw_export_{timestamp_f}")
    if not os.path.exists(folder):
        os.makedirs(folder)
    # with open(f"io/tw_export_{timestamp_f}/tw-pic-links-{timestamp_f}.txt", "w") as f_txt:
    with open(os.path.join(f"io/tw_export_{timestamp_f}/tw-pic-links-{timestamp_f}.txt"), "w") as f_txt:
        for picture_url in picture_urls_f:
            filename = picture_url.split("/")[-1]
            filepath = os.path.join(folder, filename)
            f_txt.write(picture_url + "\n")
            with urllib.request.urlopen(picture_url) as url:
                image_data = url.read()
                with open(filepath, "wb") as f:
                    print(f"Downloading: {picture_url}")
                    f.write(image_data)


def zip_it(picture_urls_f, timestamp_f):
    with zipfile.ZipFile(os.path.join("io", f"tw-scrape-{timestamp_f}.zip"), mode="w") as zf:
        print(f"Creating: tw-scrape-{timestamp_f}.zip")
        with open(f"tw-pic-links-{timestamp_f}.txt", "w") as f_txt:
            for picture_url in picture_urls_f:
                f_txt.write(picture_url + "\n")
                with urllib.request.urlopen(picture_url) as url:
                    image_data = url.read()
                    filename = picture_url.split("/")[-1]
                    print(f"Packing: {filename}")
                    zf.writestr(f'{filename}', image_data)
        zf.write(f"tw-pic-links-{timestamp_f}.txt")
        os.remove(f"tw-pic-links-{timestamp_f}.txt")


# ---------------------------------------------------------------------------------------------- FLOW

print("Starting...")

img_links = download_data_from_column(column_name, sheet_url)
# for link in img_links:
#    print(link)

picture_urls = fetch_picture_urls(img_links)
# for url in picture_urls:
#    print(url)

download(picture_urls, timestamp)

zip_it(picture_urls, timestamp)

print("Done!")
