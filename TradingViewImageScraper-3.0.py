from bs4 import BeautifulSoup
import urllib.request
import os
from datetime import datetime
from flask import Flask, request, send_file
import shutil

timestamp = (str(datetime.now()).replace(":", "-"))[:-7]
app = Flask(__name__)

# ---------------------------------------------------------------------------------------------- FUNKCE


@app.route('/download', methods=['POST'])
def download_data_from_form():
    pic_weblinks = request.form.getlist('urls')
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


@app.route("/io/tw_export_<timestamp_f>")
def zip_it_send_it(timestamp_f):
    print(f"Creating: tw-scrape-{timestamp_f}.zip")
    folder_name = f"io/tw_export_{timestamp_f}"
    zip_name = f"tw_export_{timestamp_f}.zip"
    shutil.make_archive(folder_name, "zip", folder_name)
    shutil.rmtree(folder_name)
    return send_file(zip_name, as_attachment=True)


# ---------------------------------------------------------------------------------------------- FLOW

print("Starting...")

img_links = download_data_from_form()
# for link in pic_weblinks:
#    print(link)

picture_urls = fetch_picture_urls(img_links)
# for url in picture_urls:
#    print(url)

download(picture_urls, timestamp)

zip_it_send_it(timestamp)

print("Done!")

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
