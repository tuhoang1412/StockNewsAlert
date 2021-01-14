from email.utils import make_msgid
import requests
from datetime import timedelta
import datetime
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
TRIAL_NUMBER = "+18475841059"

stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": "922GA812RWRMIKAD"
    }

def init_stock_data():
    stock_data = requests.get(url="https://www.alphavantage.co/query", params= stock_params)
    stock_prices = stock_data.json()
    day1 = datetime.date.today() - timedelta(days = 1)
    day2 = datetime.date.today() - timedelta(days = 2)
    stock_price_day1 = stock_prices["Time Series (Daily)"][str(day1)]["4. close"]
    stock_price_day2 = stock_prices["Time Series (Daily)"][str(day2)]["4. close"]
    percent_change = float(stock_price_day1)/float(stock_price_day2)
    articles = init_news_data()
    a1 = articles[0]
    a2 = articles[1]

    msg = "\nTSLA: " + str(round(percent_change, 2)) + f"%\n {a1}. {a2}."
    print(msg)
    # if (percent_change > 1.02):
    #     percent_change = (percent_change - 1) * 100
    #     msg = f"\nTSLA: 🔺" + str(round(percent_change, 2)) + "%\n + {articles[0]}. {articles[1]}."
    #     #get_news(msg)
    #     print(msg)
    #     print("up")
    # elif (percent_change < 0.95):
    #     percent_change = (percent_change - 1) * 100
    #     msg = "\nTSLA: 🔻" + str(round(percent_change, 2)) + "%\n"
    #     print("dw")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def init_news_data():
    # Init
    newsapi = NewsApiClient(api_key='a521dca8f0894b5590a09c9819ff3760')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                            category='business',
                                            language='en',
                                            country='us')
    if not top_headlines["articles"]:
        return "There are no major articles"
        
    else: 
        articles = [article["title"] for article in top_headlines["articles"][:2]]
        print(articles)
        return articles
        
        
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


def get_news(msg):
    client = Client("ACee44d73f7c774eda61497d88b385aa27", "b4469b7f86d471f9514899f8b5d1bb57")
    message = client.messages \
                    .create(
                        body= msg,
                        from_='+18475841059',
                        to='+16193437689'
                    )
    print(message.status)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


init_stock_data()