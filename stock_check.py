import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PRODUCT_ID = "2154913"
LINE_TOKEN = "RbmXo1ELaaNY4g6+rIdyKoDZvp/jD6ZhpDjZIMJ76W9QPcjZs3di6pGym/Yq7EyFnPIczCeYANv3BnaNYuBetTLaqj/EbMC5FikxR0k59VdnYBfHE9GIcQwAbWqI9MuIRRbxfQgE7WO9ChCKoNhZ+wdB04t89/1O/w1cDnyilFU="

def send_line(msg):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    requests.post(url, headers=headers, data={"message": msg})

def get_stock():
    url = f"https://ec.elifemall.com.tw/api/product/{PRODUCT_ID}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://ec.elifemall.com.tw/",
        "Accept": "application/json"
    }

    try:
        res = requests.get(url, headers=headers, timeout=5, verify=False)
        data = res.json()

        print("回傳資料:", data)

        # 🔥 關鍵在這裡（你提供的結構）
        stock = data[0]["stock"]

        print("目前庫存:", stock)

        return stock > 0

    except Exception as e:
        print("錯誤:", e)
        return None


while True:
    print("檢查中...")

    result = get_stock()

    if result is True:
        print("✅ 有貨")
        send_line("🎉 有貨了！")
    elif result is False:
        print("❌ 沒貨")
    else:
        print("⚠️ 取得失敗")

    time.sleep(300)
