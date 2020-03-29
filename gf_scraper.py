from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm
import sys
import getopt

page = []


def main(argv):
    output_file = "output.txt"  # ouput file
    tag = "neue"  # tag (https://www.gutefrage.net/beliebte_tags or "neue")
    pages = 1  # amount of pages getting scraped (100 questions per page)
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'o:t:p:h', ['output', 'tag',
                                   'pages', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-o', '--output'):
            output_file = arg
        elif opt in ('-t', '--tag'):
            tag = arg
        elif opt in ('-p', '--pages'):
            pages = arg
        else:
            usage()
            sys.exit(2)
    print("Scraping ~" + str(int(pages) * 100) + ' questions with the tag "'
          + tag + '" from https://www.gutefrage.net ...')
    print("\nAppending pages")
    appendSites(pages, tag)
    print("\nGetting text and writing to file")
    pageToFile(output_file, page)
    print("\nFinished!")


def appendSites(pages, tag):
    for n in tqdm(range(0, int(pages))):
        with urllib.request.urlopen("https://www.gutefrage.net/tag/" + tag
                                    + "/" + str(n + 1)) as url:
            page.append(url.read())


def pageToFile(output_file, page):
    outfile = open(output_file, 'w', encoding="utf-8")
    for p in tqdm(page):
        soup = BeautifulSoup(p, 'html.parser')
        only = soup.find_all("div",
                             {'class': 'H4 Question-title u-big u-mbm'})[:100]
        for i in only:
            outfile.write(i.get_text() + "\n")
    outfile.close()


def usage():
    print('Usage:')
    print('python gf_scraper.py -o <output file> -t <tag> -p <pages>\n')
    print('-o, --output: Set the output filename, default: "output.txt"')
    print('-t, --tag:    Set the tag for the question, default: "neue"')
    print('              https://www.gutefrage.net/beliebte_tags')
    print('-p, --pages:  Set the amount of pages to be scraped, default: "1"')
    print('-h, --help:   View this text')


if __name__ == "__main__":
    main(sys.argv)
