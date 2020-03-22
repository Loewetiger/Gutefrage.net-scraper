from bs4 import BeautifulSoup
import urllib.request

output_file = "output.txt"  # ouput file
tag = "neue"  # tag (https://www.gutefrage.net/beliebte_tags or "neue")
pages = 1  # amount of pages getting scraped (100 questions per page)

it = 1

outfile = open(output_file, 'w', encoding="utf-8")
while it <= pages:
    with urllib.request.urlopen("https://www.gutefrage.net/tag/" + tag + "/"
                                + str(it)) as url:
        page = url.read()
    soup = BeautifulSoup(page, 'html.parser')
    only = soup.find_all("div",
                         {'class': 'H4 Question-title u-big u-mbm'})[:100]
    for i in only:
        outfile.write(i.get_text() + "\n")
    it = it + 1
outfile.close()
