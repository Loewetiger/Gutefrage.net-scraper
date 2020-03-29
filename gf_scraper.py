from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm

output_file = "output.txt"  # ouput file
tag = "neue"  # tag (https://www.gutefrage.net/beliebte_tags or "neue")
pages = 1  # amount of pages getting scraped (100 questions per page)

page = []

outfile = open(output_file, 'w', encoding="utf-8")
print("Appending pages")
for n in tqdm(range(0, pages)):
    with urllib.request.urlopen("https://www.gutefrage.net/tag/" + tag + "/"
                                + str(n + 1)) as url:
        page.append(url.read())
print("Getting text and writing to file")
for p in tqdm(page):
    soup = BeautifulSoup(p, 'html.parser')
    only = soup.find_all("div",
                         {'class': 'H4 Question-title u-big u-mbm'})[:100]
    for i in only:
        outfile.write(i.get_text() + "\n")
outfile.close()
print("Finished!")
