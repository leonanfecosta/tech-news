from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    news_most_commented = sorted(
        news, key=lambda x: x["comments_count"], reverse=True
    )
    top_5_news = []
    for notice in news_most_commented[:5]:
        top_5_news.append((notice["title"], notice["url"]))
    return top_5_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
