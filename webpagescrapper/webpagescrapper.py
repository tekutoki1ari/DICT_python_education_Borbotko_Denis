import string
import requests
from bs4 import BeautifulSoup
from colorama import Fore
import os


def creating_links(soup):
    columns = soup.find_all('div', 'c-card__body u-display-flex u-flex-direction-column')
    href = list()
    for i in columns:
        j = i.find('a')
        href.append(j.get('href'))

    all_links = list()
    for g in range(len(href)):
        all_links.append(f'https://www.nature.com{href[g]}')

    return all_links


def article(soup):
    body = soup.find('div', 'c-article-body')

    find_sections = body.find_all('h2',
                                  'c-article-section__title js-section-title js-c-reading-companion-sections-item')
    sections = list()
    for item in find_sections:
        sections.append(item.text)
    if 'Methods' not in sections:
        sections = ['Abstract']

    section_contents = soup.find_all('div', 'c-article-section__content')
    result_body_text = list()
    for s in range(len(sections)):
        result_body_text.append(section_contents[s])
        if sections[s] == 'Methods':
            break

    find_title = soup.find('meta', {'name': "dc.title"})
    result_title = find_title.get('content')
    return result_body_text, result_title


def other_types(soup):
    find_body = soup.find('div', 'c-article-body u-clearfix')
    result_body_text = find_body.find_all('p', {'class': ''})

    result_title = soup.title.text
    return result_body_text, result_title


def writing_to_file(given_body_text, given_title):
    title_without_punctuation = given_title.translate(str.maketrans('', '', string.punctuation))
    article_name = title_without_punctuation.translate(str.maketrans(" ", "_", "—"))
    while "__" in article_name:
        article_name = article_name.replace("__", "_")

    file = open(f'{article_name}.txt', "wb+")
    for p in given_body_text:
        file.write(bytes(p.text, 'utf8'))
    file.close()


def process(all_links, article_type):
    for link in all_links:
        r2 = requests.get(link)
        soup2 = BeautifulSoup(r2.content, 'lxml')
        if article_type == "Article":
            body, title = article(soup2)
        else:
            body, title = other_types(soup2)
        writing_to_file(body, title)


while True:
    try:
        print("\nAvailable article types:")
        print("Article, News, Book Review, Outlook, Nature Briefing, News Feature, Comment, Career Feature,")
        print("Futures, Editorial, World View, Books and Arts, Where i work")

        types = ["Article", "News", "Book Review", "Outlook", "Nature Briefing", "News Feature", "Comment", "Futures",
                 "Career Feature", "Editorial", "World View", "Books and Arts", "Where i work"]

        a_type = input(f'\nEnter the article type:\n> ')
        if a_type not in types:
            raise ValueError
        else:
            a_type = a_type.translate(str.maketrans(' ', '-'))
            url = f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2022&type={a_type.lower()}'
        break
    except ValueError:
        print(f'\n{Fore.RED}Invalid article type, try again.{Fore.RESET}\n')

while True:
    try:
        n_pages = int(input("Enter the number of pages:\n> "))
        test_url = f'{url}&page={n_pages}'
        test_request = requests.get(test_url)
        if test_request.status_code != 200:
            print(f'\n{Fore.RED}Sorry, there are too many pages, try again with a fewer pages.{Fore.RESET}\n')
            continue
        break
    except ValueError:
        print(f'\n{Fore.RED}Invalid input. Try again, write only numbers.{Fore.RESET}\n')

for n in range(n_pages):
    os.mkdir(f'Page_{n + 1}')
    os.chdir(f'Page_{n + 1}')

    url = f'{url}&page={n + 1}'
    r = requests.get(url)
    soup1 = BeautifulSoup(r.content, 'lxml')

    links = creating_links(soup1)
    process(links, a_type)
    os.chdir("..")