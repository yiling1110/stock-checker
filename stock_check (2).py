import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://ec.elifemall.com.tw/products/2154913"
LINE_TOKEN = "RbmXo1ELaaNY4g6+rIdyKoDZvp/jD6ZhpDjZIMJ76W9QPcjZs3di6pGym/Yq7EyFnPIczCeYANv3BnaNYuBetTLaqj/EbMC5FikxR0k59VdnYBfHE9GIcQwAbWqI9MuIRRbxfQgE7WO9ChCKoNhZ+wdB04t89/1O/w1cDnyilFU="

def send_line(msg):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": msg}
    requests.post(url, headers=headers, data=data)

def check_stock():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(URL)
        time.sleep(5)

        page_text = driver.page_source

        if "加入購物車" in page_text and "補貨中" not in page_text:
            return True

        return False

    finally:
        driver.quit()


while True:
    print("🔍 檢查中...")

    if check_stock():
        print("✅ 有貨")
        send_line("🎉 有貨了！\n" + URL)
    else:
        print("❌ 沒貨")

    time.sleep(300)