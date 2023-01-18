import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1>
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code == 200:
            return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    if not next_page:
        return None
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = (len(selector.css(".comment-list li").getall())) or 0
    summary = selector.xpath("string(//p)").get().rstrip()
    tags = selector.css(".post-tags li a::text").getall()
    category = selector.css("div.entry-details span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    page_html = fetch("https://blog.betrybe.com/")
    news_links = scrape_updates(page_html)
    next_page_link = scrape_next_page_link(page_html)
    news = []

    while len(news_links) < amount:
        page_html = fetch(next_page_link)
        news_links += scrape_updates(page_html)
        next_page_link = scrape_next_page_link(page_html)

    for link in news_links[:amount]:
        news.append(scrape_news(fetch(link)))

    create_news(news)
    return news
