from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))

    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    news_list = search_news({"tags": {"$regex": tag, "$options": "i"}})
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))

    return result


# Requisito 9
def search_by_category(category):
    news_list = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    result = []
    for news in news_list:
        result.append((news["title"], news["url"]))

    return result
