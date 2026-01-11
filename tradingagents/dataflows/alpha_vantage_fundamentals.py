import os
from .alpha_vantage_common import _make_api_request


def get_fundamentals(ticker: str, curr_date: str = None) -> str:
    """
    Retrieve comprehensive fundamental data for a given ticker symbol using Alpha Vantage.

    Args:
        ticker (str): Ticker symbol of company
        curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

    Returns:
        str: Company overview data including financial ratios and key metrics
    """
    print(
        f"DEBUG: get_fundamentals (alpha_vantage) called with ticker={ticker}, curr_date={curr_date}"
    )

    params = {
        "symbol": ticker,
    }

    try:
        print(f"DEBUG: Making Alpha Vantage API request for {ticker}")
        result = _make_api_request("OVERVIEW", params)
        print(f"DEBUG: Alpha Vantage fundamentals retrieved successfully")
        return result
    except Exception as e:
        print(
            f"ERROR: get_fundamentals (alpha_vantage) failed: {type(e).__name__}: {e}"
        )
        raise


def get_balance_sheet(
    ticker: str, freq: str = "quarterly", curr_date: str = None
) -> str:
    """
    Retrieve balance sheet data for a given ticker symbol using Alpha Vantage.

    Args:
        ticker (str): Ticker symbol of the company
        freq (str): Reporting frequency: annual/quarterly (default quarterly) - not used for Alpha Vantage
        curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

    Returns:
        str: Balance sheet data with normalized fields
    """
    params = {
        "symbol": ticker,
    }

    return _make_api_request("BALANCE_SHEET", params)


def get_cashflow(ticker: str, freq: str = "quarterly", curr_date: str = None) -> str:
    """
    Retrieve cash flow statement data for a given ticker symbol using Alpha Vantage.

    Args:
        ticker (str): Ticker symbol of the company
        freq (str): Reporting frequency: annual/quarterly (default quarterly) - not used for Alpha Vantage
        curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

    Returns:
        str: Cash flow statement data with normalized fields
    """
    params = {
        "symbol": ticker,
    }

    return _make_api_request("CASH_FLOW", params)


def get_income_statement(
    ticker: str, freq: str = "quarterly", curr_date: str = None
) -> str:
    """
    Retrieve income statement data for a given ticker symbol using Alpha Vantage.

    Args:
        ticker (str): Ticker symbol of the company
        freq (str): Reporting frequency: annual/quarterly (default quarterly) - not used for Alpha Vantage
        curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

    Returns:
        str: Income statement data with normalized fields
    """
    params = {
        "symbol": ticker,
    }

    return _make_api_request("INCOME_STATEMENT", params)
