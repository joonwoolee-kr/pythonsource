import requests
from bs4 import BeautifulSoup


def main(keyword):
    url = f"https://news.google.com/search?q={keyword}&hl=ko&gl=KR&ceid=KR%3Ako"

    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        news = data_extract(soup)

        for item in news:
            for k, v in item.items():
                print(f"{k}: {v}")
            print()


def data_extract(soup):
    base_url = "https://news.google.com"

    news = []

    articles = soup.select("article")
    # print(articles)
    for article in articles:
        news_item = {}
        element = article.select_one(".JtKRv")
        # 타이틀
        title = element.text.strip()
        # 기사링크
        link = base_url + element["href"][1:]
        # 작성자
        if article.select_one(".bInasb"):
            # writer = article.select_one(".bInasb").text.split(":")[1].strip()
            writer = article.select_one(".bInasb").text.strip()
        else:
            writer = ""
        # 작성일시
        datetime = article.select_one(".hvbAAd")["datetime"].split("T")
        date = datetime[0]
        time = datetime[1][:-1]

        news_item["title"] = title
        news_item["link"] = link
        news_item["writer"] = writer
        news_item["date"] = date
        news_item["time"] = time
        news.append(news_item)

    return news


if __name__ == "__main__":
    main("파이썬")
