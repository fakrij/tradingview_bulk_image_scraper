import requests
from bs4 import BeautifulSoup

picture_links = []
picture_urls = []

with open("io/tw_urls.txt", "r") as url_list:
    line_with_url = url_list.readline()
    while line_with_url:
        picture_links.append(line_with_url[0:-2])
        line_with_url = url_list.readline()

for picture_link in picture_links:
    print(f"Fetching... {picture_link}")
    r = requests.get(picture_link)
    r_html = r.text
    soup = BeautifulSoup(r_html, features="html.parser")
    for img in soup.find_all("img", "tv-snapshot-image"):  # where img is the tag and the other is the name of class
        picture_urls.append(img.get("src"))  # nebo: picture_links.append(img["src"])

with open("io/tw_pic_links.txt", "w") as f:
    for picture_url in picture_urls:
        f.write(picture_url + "\n")
        response = requests.get(picture_url)
        open(picture_url[-12:], "wb").write(response.content)
        print(picture_url)