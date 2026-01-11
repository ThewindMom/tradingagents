import os
from openai import OpenAI
from .config import get_config


def get_stock_news_openai(query, start_date, end_date):
    config = get_config()
    # Use OpenAI-compatible endpoint for zai
    base_url = config.get("openai_compatible_base_url", config["backend_url"])
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = OpenAI(base_url=base_url, api_key=api_key)

    response = client.chat.completions.create(
        model=config["quick_think_llm"],
        messages=[
            {
                "role": "system",
                "content": f"Can you search Social Media for {query} from {start_date} to {end_date}? Make sure you only get to data posted during that period.",
            }
        ],
    )

    return response.choices[0].message.content


def get_global_news_openai(curr_date, look_back_days=7, limit=5):
    config = get_config()
    base_url = config.get("openai_compatible_base_url", config["backend_url"])
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    print(f"DEBUG: get_global_news_openai called with:")
    print(f"  base_url: {base_url}")
    print(f"  model: {config.get('quick_think_llm', 'unknown')}")
    if api_key:
        print(f"  api_key: {api_key[:10]}...{api_key[-5:]}")
    else:
        print(f"  api_key: None")

    try:
        client = OpenAI(base_url=base_url, api_key=api_key)
        print(f"DEBUG: OpenAI client created successfully")

        response = client.chat.completions.create(
            model=config["quick_think_llm"],
            messages=[
                {
                    "role": "system",
                    "content": f"Can you search global or macroeconomics news from {look_back_days} days before {curr_date} to {curr_date} that would be informative for trading purposes? Make sure you only get to data posted during that period. Limit results to {limit} articles.",
                }
            ],
        )
        print(f"DEBUG: OpenAI API call succeeded")

        return response.choices[0].message.content
    except Exception as e:
        print(f"ERROR: OpenAI API call failed: {type(e).__name__}: {e}")
        raise


def get_fundamentals_openai(ticker, curr_date):
    config = get_config()
    # Use OpenAI-compatible endpoint for zai
    base_url = config.get("openai_compatible_base_url", config["backend_url"])
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = OpenAI(base_url=base_url, api_key=api_key)

    response = client.chat.completions.create(
        model=config["quick_think_llm"],
        messages=[
            {
                "role": "system",
                "content": f"Can you search Fundamental for discussions on {ticker} during of the month before {curr_date} to month of {curr_date}. Make sure you only get the data posted during that period. List as a table, with PE/PS/Cash flow/ etc.",
            }
        ],
    )

    return response.choices[0].message.content
