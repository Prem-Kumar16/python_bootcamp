import requests
import itertools
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
Before_DATE = date.today() - timedelta(3)
account_sid = "Your acc sid"
auth_token = "Your auth token"

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "Your api key"

}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
print(stock_response.status_code)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
first_2_values = dict(itertools.islice(stock_data.items(), 2))
timings_list = [value for (state, value) in first_2_values.items()]
# print(timings_list)
yesterday_opening = float(timings_list[0]["1. open"])
yesterday_opening = 400
# print(yesterday_opening)
DBY_closing = float(timings_list[1]["4. close"])
# print(DBY_closing)

if yesterday_opening > DBY_closing:
    percent = round(((yesterday_opening - DBY_closing) / DBY_closing) * 100)
    symbol = "🔺"
else:
    percent = round(((DBY_closing - yesterday_opening) / yesterday_opening) * 100)
    symbol = "🔻"

percent_increase = (DBY_closing * 0.05) + DBY_closing
# print(percent_increase)
percent_decrease = DBY_closing - (DBY_closing * 0.05)
# print(percent_decrease)

if yesterday_opening > percent_increase or yesterday_opening < percent_decrease:

    # # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": "your api key",
        "from": Before_DATE

    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    print(news_response.status_code)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    print(news_data)

    # # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.

    for news in news_data:
        headline = news["title"]
        brief = news["description"]
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"{COMPANY_NAME}: {symbol}{percent}%\n"
                 f"Headline: {headline}\n"
                 f"Brief: {brief}",
            from_="+19288778722",
            to="+91 99447 38905"
        )


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
