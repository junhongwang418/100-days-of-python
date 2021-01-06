from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()

TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=params)
response.raise_for_status()

data = response.json()
data = data["Time Series (Daily)"]
data = [float(value["4. close"]) for (key, value) in data.items()]

closing_stock_price_yesterday = data[0]

# TODO 2. - Get the day before yesterday's closing stock price
closing_stock_price_day_before_yesterday = data[1]

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = closing_stock_price_yesterday - closing_stock_price_day_before_yesterday

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = diff / closing_stock_price_day_before_yesterday * 100

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percentage) > 5:
    print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}
response = requests.get(NEWS_ENDPOINT, params=params)
response.raise_for_status()

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
data = response.json()
data = data["articles"][:3]

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
articles = [(article["title"], article["description"]) for article in data]

# TODO 9. - Send each article as a separate message via Twilio.
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
icon = "🔺" if diff_percentage > 0 else "🔻"
for article in articles:
    client.messages.create(
        body=f"{STOCK_NAME}: {icon}{abs(diff_percentage)}%\nHeadline: {article[0]}\nBrief: {article[1]}",
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
