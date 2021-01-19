import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

BOT_EMAIL_ADDRESS = os.getenv('BOT_EMAIL_ADDRESS')
BOT_EMAIL_PASSWORD = os.getenv('BOT_EMAIL_PASSWORD')
MY_EMAIL_ADDRESS = os.getenv('MY_EMAIL_ADDRESS')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6'
}

url = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
price_tag = soup.find(name='span', id='priceblock_ourprice').text
price = float(price_tag.split('$')[1])

if price < 200:
    header = f"From: {BOT_EMAIL_ADDRESS}\r\nTo: {MY_EMAIL_ADDRESS}\r\nSubject: Amazon Price Alert"
    body = f"Instant Pot Duo Evo Plus Pressure Cooker 10 in 1,  6 Qt, 48 One Touch Programs is now ${price}.\n{url}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=BOT_EMAIL_ADDRESS,
                         password=BOT_EMAIL_PASSWORD)
        connection.sendmail(from_addr=BOT_EMAIL_ADDRESS, to_addrs=MY_EMAIL_ADDRESS,
                            msg=f"{header}\r\n\r\n{body}".encode("utf8"))
