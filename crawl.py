from sys import argv
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm


def get_title(soup):
    title = soup.find('div', {'id': 'News_Body_Title'})
    return ''.join(title.strings)


def get_qa_pairs(soup):
    news_body = soup.find('div', {'class': 'content'})
    body = ''.join(news_body.strings)
    body = body.strip()
    body = body.replace('\n', '')
    body = body.replace('\u3000', '')
    pairs = [
        s.split('答：')
        for s in body.split('问：') if len(s) > 0 and len(s.split('答：')) == 2
    ]
    return pairs


def crawl_page(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    title = get_title(soup)
    if '例行记者会' in title or '答记者问' in title:
        return get_qa_pairs(soup)
    else:
        return []


if __name__ == '__main__':
    page_urls_file = argv[1]
    page_urls = []
    with open(page_urls_file, 'r') as f_in:
        for line in f_in:
            page_urls.append(line.strip('\n'))
    print(f'Total {len(page_urls)} pages.')

    qa_pairs = []
    for page in tqdm(page_urls):
        qa_pairs += crawl_page(page)
        time.sleep(1)

    print(f'Total {len(qa_pairs)} QA pairs')
    with open(argv[2], 'w+') as f_out:
        for pair in qa_pairs:
            print(f'Q:{pair[0]}', file=f_out)
            print(f'A:{pair[1]}', file=f_out)
            print(file=f_out)
