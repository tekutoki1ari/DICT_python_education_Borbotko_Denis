import string
import requests
from bs4 import BeautifulSoup
from colorama import Fore


def start_parser(r):
    while True:
        soup = BeautifulSoup(r.content, "lxml")

        columns = soup.find_all('div', 'c-card__body u-display-flex u-flex-direction-column')
        href = list()
        for i in columns:
            j = i.find('a')
            href.append(j.get('href'))

        article_types = soup.find_all('span', 'c-meta__type')

        urls = list()
        for g in range(len(href)):
            if article_types[g].string == 'News':
                urls.append(f'https://www.nature.com{href[g]}')

        if len(urls) == 0:
            print("This site does not contain articles with the type of news")
            break

        saved_articles = list()
        for url in urls:
            r2 = requests.get(url)
            soup = BeautifulSoup(r2.content, "lxml")
            body = soup.find('div', 'c-article-body u-clearfix')
            just_paragraphs = body.find_all('p', {'class': ''})

            title = soup.title.text
            title_without_punctuation = title.translate(str.maketrans('', '', string.punctuation))
            article_name = title_without_punctuation.translate(str.maketrans(" ", "_", "—"))
            while "__" in article_name:
                article_name = article_name.replace("__", "_")

            saved_articles.append(f'{article_name}.txt')

            file = open(f'{article_name}.txt', "wb+")
            for p in just_paragraphs:
                file.write(bytes(p.text, 'utf8'))
            file.close()

        print(f'Saved articles: {saved_articles}')
        break


while True:
    try:
        url_input = input("Enter the URL:\n> ")
        r1 = requests.get(url_input)
        if r1.status_code != 200:
            print(f'\n{Fore.RED}The URL returned {r1.status_code}!{Fore.RESET}\n')
        elif 'nature.com/nature/articles' not in url_input:
            print(f'\n{Fore.RED}Incorrect URL. '
                  f'Write links only from "https://www.nature.com/nature/articles"{Fore.RESET}\n')
        else:
            start_parser(r1)
            break
    except requests.exceptions.ConnectionError:
        print(f'\n{Fore.RED}Invalid URL. Check that the website domain is entered correctly.{Fore.RESET}\n')
    except requests.exceptions.MissingSchema:
        print(f'\n{Fore.RED}Missing protocol. '
              f'Maybe you forgot to include "http://" or "https://" in the link?{Fore.RESET}\n')
    except requests.exceptions.InvalidSchema:
        print(f'\n{Fore.RED}Invalid protocol. '
              f'Check that the "http://" or "https://" in the link is entered correctly.{Fore.RESET}\n')
    except requests.exceptions.InvalidURL:
        print(f'\n{Fore.RED}Invalid URl. No host supplied.{Fore.RESET}\n')
