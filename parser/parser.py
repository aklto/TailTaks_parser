import requests
from bs4 import BeautifulSoup

def scrape_latest_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('a', class_='last-posts__link filter_zoobiznes')

    latest_articles = []

    for article in articles:
        title = article.find('h2', class_='articles-item__title').get_text(strip=True)
        link = article['href']
        image = article.find('img')['src']
        badge = article.find('span', class_='articles-item__badge').get_text(strip=True)
        date = article.find('div', class_='articles-item__time').get_text(strip=True)
        latest_articles.append({'title': title, 'link': link, 'image': image, 'badge': badge, 'date': date})

    def get_article_content(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h1', class_='content-page__title').get_text(strip=True)

        paragraphs = soup.find_all('p')
        content = "\n".join([p.get_text(strip=True) for p in paragraphs])

        return title, content

    articles_dict = {}

    for article in latest_articles:
        title, content = get_article_content(article['link'])
        articles_dict[title] = content

    return articles_dict


