import requests


def search_address(zipcode):
    response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")

    dic = response.json()
    address_info = response.json()["results"][0]

    prefecture_name = address_info["address1"]
    city_name = address_info["address2"]
    town_name = address_info["address3"]

    address = f"{prefecture_name}{city_name}{town_name}"
    return address

if __name__ == "__main__":
    zipcode = "0287111"

    address = search_address(zipcode)

    assert "岩手県八幡平市大更" == address
    