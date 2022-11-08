Hromadné stahování obrázků z TradingView:

Používám tradingview na backtesty. Zkratka Alt+s ukládá aktuální graf jako obrázek. Respektive uloží webovou stránku v níž je obrázek vložený. Takže máme 100 tradů v tabulce s backtestem a chcete si otevřít všechny screenshoty najednou a "nakoukat" je. V tabulce tak klikáte jak zběsilí a v internetovém prohlížeči vám naskakují jednotlivé taby... Za mě teda dost naprd. Takž jsem udělal tuhle věcičku, které dáte seznam URL s obrázky a ona vám jednak vygeneruje přímé odkazy na obrázky a zároveň je taky všechny stáhne.

Je to první verze a nepovedlo se mi to zatím udělat jako spustitelný soubor. Hádám tak, že si budete muset nainstalovat python a pak to spustit z příkazové řádky. Prozatím je to uplně primitivo věc - načítá to URL které dodáte v textovém souboru. Jak se naučim jiný věci, tak přidám funkcionalitu když bude čas. Konečný ideál = web appka která si URL umí natáhnou přímo z google sheetu. Návod:

1. Do souboru tw_urls.txt ve složce io zkopírujte sloupec s URL adresami stránek se screenshoty na tradingview, např.: https://www.tradingview.com/x/Byux5Vze/
2. jeden řádek texťáku = jedna URL
3. pozor pokud máte více url v jedné buňce spreadsheetu, zkontrolujte si co do texťáku vkládáte
4. vkládejte jen URL adresy, dejte pozor ať před nebo za adresou nejsou žádné extra znaky jako ,.'!:" apod.
5. uložte texťák a spusťte skript tw_image_scraper.py, vše pak najdete v adresáři io
