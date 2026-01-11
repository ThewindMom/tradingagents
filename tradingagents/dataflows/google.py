from typing import Annotated
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .googlenews_utils import getNewsData


def get_google_news(
    query: Annotated[str, "Query to search with"],
    curr_date: Annotated[str, "Curr date in yyyy-mm-dd format"],
    look_back_days: Annotated[int, "how many days to look back"],
) -> str:
    query = query.replace(" ", "+")

    start_date = datetime.strptime(curr_date, "%Y-%m-%d")
    before = start_date - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    news_results = getNewsData(query, before, curr_date)

    news_str = ""

    for news in news_results:
        news_str += (
            f"### {news['title']} (source: {news['source']}) \n\n{news['snippet']}\n\n"
        )

    if len(news_results) == 0:
        return ""

    return f"## {query} Google News, from {before} to {curr_date}:\n\n{news_str}"


def get_global_news_google(curr_date, look_back_days=7, limit=5):
    """
    Global news function compatible with get_global_news signature.
    Wrapper around get_google_news for global/macroeconomic news.
    """
    print(
        f"DEBUG: get_global_news_google called with curr_date={curr_date}, look_back_days={look_back_days}, limit={limit}"
    )

    query = "global macroeconomics economy market"
    start_date = datetime.strptime(curr_date, "%Y-%m-%d")
    before = start_date - relativedelta(days=look_back_days)
    before = before.strftime("%Y-%m-%d")

    try:
        news_results = getNewsData(query, before, curr_date)

        news_str = ""
        count = 0
        for news in news_results:
            if count >= limit:
                break
            news_str += f"### {news['title']} (source: {news['source']}) \n\n{news['snippet']}\n\n"
            count += 1

        print(f"DEBUG: get_global_news_google returned {count} articles")

        if count == 0:
            return "No global news articles found for the specified period."

        return (
            f"## Global Macroeconomic News from {before} to {curr_date}:\n\n{news_str}"
        )
    except Exception as e:
        print(f"ERROR: get_global_news_google failed: {type(e).__name__}: {e}")
        raise
