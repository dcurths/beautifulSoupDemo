from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# get page html
try:
    html = urlopen("http://shop.oreilly.com/category/bestselling.do")
except HTTPError:
    print("Page not found")

# create bs object
page = BeautifulSoup(html)

# parse list of books
books = page.find_all("td", {"class":"thumbtext"})

# print header
print("Title|Author|Date|Price")

for book in books:
    # get author
    author = book.find("div", {"class":"AuthorName"})
    author = author.get_text()
    author = author.strip()

    # get title
    title = book.find("div", {"class":"thumbheader"})
    title = title.get_text()
    title = title.strip()

    # get date
    date = book.find("span", {"class":"directorydate"})
    date = date.get_text()
    date = date.strip()

    # get price
    price = book.find("span", {"class":"price"})
    price = price.get_text()
    price = price.strip()

    #print csv
    print(title + "|" + author + "|" + date + "|" + price, end="")
    print()
