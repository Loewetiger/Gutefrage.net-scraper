# Gutefrage.net-scraper
A script for scraping questions off of the popular german Q&A site "gutefrage.net".

## Installation

 1. Download the latest release or clone the repo.
 2. Install Python 3 (v3.7 in my case): https://www.python.org/.
 3. Unpack the release and open a command prompt.
 4. Install the requirements with `pip install -r requirements.txt`.

## Usage

> Basic usage: python gf_scraper.py -o \<output file\> -t \<tag\> -p
> \<pages\>
> -o, --output: Set the output filename, default: "output.txt"
> -t, --tag: Set the tag for the question, default: "neue"
> https://www.gutefrage.net/beliebte_tags
> -p, --pages: Set the amount of pages to be scraped, default: "1"
> -h, --help: View the usage
