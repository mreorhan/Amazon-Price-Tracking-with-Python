import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com.tr/Xiaomi-MDZ-22-AB-Mi-Box-Ultra/dp/B07K3KC5CP/?_encoding=UTF8&pd_rd_w=HBL1b&pf_rd_p=84e5ee78-99ba-4bbf-ab40-3d08d46687dd&pf_rd_r=VP3NY9AZ6ZG6BKRPZ3J1&pd_rd_r=54fcd669-fee2-434e-b177-f94f81420c8d&pd_rd_wg=hOuQr&ref_=pd_gw_crs_zg_bs_12466497031'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52"
}

def price_check(URL, max_price):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").getText().strip()

    price = soup.find(id="priceblock_ourprice").getText().strip()

    new_price = float(price[1:-1].replace(",","."))

    print(new_price)

    if(new_price <= max_price):
        send_email("TO_EMAIL",URL)
    else: 
        print("ürün fiyatı düşmedi!")


def send_email(toMail, url):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("FROM_EMAIL","123456Ky.")


    subject = 'Fiyat Dustu!'

    body = 'Urun linki: ' + url

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        "FROM_EMAIL",
        "TO_EMAIL",
        msg
    )
    print("mesaj gönderildi")
    server.quit() 

while(True):
    price_check(URL,100)
    time.sleep(6)