import requests

# zipcode = input("郵便番号<ハイフン無し7桁>は？")
zipcode = "0287111"

response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")

# print(response)
# print(response.text)

# 辞書として表示
dic = response.json()
# print(dic)
# print(f"{dic['results'][0]['address1']}{dic['results'][0]['address2']}{dic['results'][0]['address3']}")
address_info = response.json()["results"][0]

prefecture_name = address_info["address1"]
city_name = address_info["address2"]
town_name = address_info["address3"]

address = f"{prefecture_name}{city_name}{town_name}"
print(address)



# # typeを使ってjsonを調べる
# print(type(response.json()))

