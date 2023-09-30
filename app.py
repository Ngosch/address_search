import requests

# zipcode = input("郵便番号<ハイフン無し7桁>は？")
zipcode = "0287111"

response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")

print(response)
print(response.text)
