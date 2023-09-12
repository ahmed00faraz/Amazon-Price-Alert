from bs4 import BeautifulSoup
import requests

# SMTP CREDENTIALS
EMAIL = "series00movies@gmail.com"
PASSWORD = "qswixiomxzsrqrdt"

TARGET_PRICE = 2000

# HEADER
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'DNT': "1",
    'Accept-Language': 'en-US,en;q=0.8'
}

PRODUCT_URL = "https://www.amazon.in/dp/B09HT1KYNH?ref_=cm_sw_r_cp_ud_dp_1RQ0E3G695AMBQWEFPFJ"
# PRODUCT_URL = "https://www.amazon.in/dp/B0C1GGG789?ref_=cm_sw_r_cp_ud_dp_D2SGJY3PQ692N39GS5BJ_2"
response = requests.get(url=PRODUCT_URL, headers=HEADER).text
soup = BeautifulSoup(response, "html.parser")
product_title = soup.find(name="span", id="productTitle").text
price_whole = soup.find(name="span", class_="a-price-whole").text
price_fraction = soup.find(name="span", class_="a-price-fraction").text
price_symbol = soup.find(name="span", class_="a-price-symbol").text
price = float((price_whole + price_fraction).replace(",", ""))
print(price, TARGET_PRICE)


def send_mail():
    import smtplib
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="ahmed00faraz3@gmail.com",
            msg=f"Subject:PRICE DROPPED!\n{product_title} is now {price_symbol}{price}\n{PRODUCT_URL}".encode('utf-8')
        )
        print("Mail sent")


if price <= TARGET_PRICE:
    send_mail()
