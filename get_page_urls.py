from sys import argv
import requests
import urllib.parse
from bs4 import BeautifulSoup
import time
from tqdm import tqdm


# URL of the 发言人表态 Page, which contains a list of links
base_url = 'https://www.fmprc.gov.cn/web/wjdt_674879/fyrbt_674889/'

# The total number of pages in 发言人表态, you may need click on 尾页 to find out
max_pages = 66


def get_index_page_urls():
    indices = [
        f'default_{i}.shtml'
        for i in range(1, max_pages)
    ]
    indices.insert(0, 'default.shtml')
    page_urls = [
        urllib.parse.urljoin(base_url, index)
        for index in indices
    ]
    return page_urls


def get_context_urls(index_page_url):
    r = requests.get(index_page_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    news_box = soup.find('div', {'class': 'rebox_news'})
    ul = news_box.find('ul')
    a_s = ul.findAll('a')
    hrefs = [
        a.attrs['href']
        for a in a_s
    ]
    return hrefs


if __name__ == '__main__':
    index_page_urls = get_index_page_urls()

    hrefs = []
    for page in tqdm(index_page_urls):
        hrefs += get_context_urls(page)
        time.sleep(1)

    with open(argv[1], 'w') as f_out:
        for href in hrefs:
            print(urllib.parse.urljoin(base_url, href), file=f_out)

