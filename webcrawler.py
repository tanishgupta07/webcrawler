import requests
from bs4 import BeautifulSoup

def crawl(i, url):
    newAdditions = []
    print("(" + str(i) + ") Traversing: " + url)

    # connecting to the url
    page = requests.get(url)

    # BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    # parsing through the links
    for link in soup.findAll('a'):
        nextLink = link.get('href')
        #print(nextLink)
        try:
            if "https://example.in/" in nextLink and nextLink not in urlList:
                urlList.append(nextLink)
                newAdditions.append(nextLink)
                file.write(nextLink + "\n")
        except:
            continue

    print("---------------------")
    print(str(len(newAdditions)) + " new additions were made in this crawl ->")
    print(newAdditions)

    print("---------------------")
    print(urlList)
    print("Total: " + str(len(urlList)))


def main():
    i = 0;
    while i < len(urlList):
        crawl(i, urlList[i])
        i += 1
#name of the file in which list is stored
file = open("textFile.txt", "w")
#url of the website that is to be crawled
urlList = ["https://testsite.in"]

main()
