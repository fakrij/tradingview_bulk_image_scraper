# tradingview_image_bulk_scraper
Provide a list of TradingView pages that are generated when youre copying screenshot links with Alt+s shortcut. This utility extracts actual image URLs, saves them in a list and downloads all of them to your computer.

Im using TradingView.com for backtests of trading strategies. That is often a mundane task that takes a lot of steps over and over again. There is a very convenient keyboard shortcut Alt+s that lets you copy image URL right in your clipboard and you can paste it in your spreadsheet with backtest. It saves a bit of time you'd spend otherwise by downloading the image to your computer, opening the hosting page, finding the image in your computer, uploading it, getting a link and finally pasting it in the spreadsheet.

The annoying thing with TW screenshots comes when you want to get through them. You click like mad on the links in the spreadsheet, opening one at a time. Imagine that doing 50 or 100x and you really understand why I wrote this nifty script.

HOW-TO:

1. copypaste the column with URLs from your GOOGLE spreadsheet (might work with other SW as well) into the tw_urls.txt file in /io directory
2. one line = one URL
3. be careful if you have more URLs in one cell
4. ony pure URLs, check out if there are no extra characters like ,"': etc. in front or after the URL
5. start the tw_image_scraper.py and let it do its thing
6. check the io directory and dl directory inside it


Id like to add more functions as I'll be learning more about python, ie.:

1. loading URLs right from the public google spreadsheet
2. foolproof URL loading without user having to control if provided URLs are ok
3. extracting images from google drive
4. better URL extracting mechanism that is independent on html class
5. web interface that can load public google spreadsheets


v2 downloads pics from a list in public google spreadsheet and can zip files, next big thing: make it a web app
