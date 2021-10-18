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
    day1 = datetime.date.today() - timedelta(days = 4)
    day2 = datetime.date.today() - timedelta(days = 5)
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
    #     msg = "\nTSLA: 🔺" + str(round(percent_change, 2)) + f"%\n + {a1}. {a2}."
    #     get_news(msg)
  
    # elif (percent_change < 0.95):
    #     percent_change = (percent_change - 1) * 100
    #     msg = "\nTSLA: 🔻" + str(round(percent_change, 2)) + "%\n"


def init_news_data():
    # Init
    newsapi = NewsApiClient(api_key='a521dca8f0894b5590a09c9819ff3760')
    
    # Getting 2 top headlines
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

# Send a seperate message with the percentage change and each article's title and description to given phone number. 
#Noted: this could be outdated because of limited-time API key
def get_news(msg):
    client = Client("ACee44d73f7c774eda61497d88b385aa27", "b4469b7f86d471f9514899f8b5d1bb57")
    message = client.messages \
                    .create(
                        body= msg,
                        from_='+18475841059',
                        to='+16193437689'
                    )
    print(message.status)

init_stock_data()
