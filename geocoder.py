import requests
# https://zenn.dev/yamadamadamada/articles/3fb198003c5428
def get_coordinate(place_name):
    """
    国土地理院APIを使用して、住所から緯度経度を取得する関数。
    """
    url = "https://msearch.gsi.go.jp/address-search/AddressSearch"
    params = {"q": place_name}
    r = requests.get(url, params=params)
    data = r.json()
    if "error" in data or not data:        
        return None, None
    else:
        # レスポンスと施設名が一致する緯度経度を返す
        for row in data:
            if row["properties"]["title"].startswith(place_name):
                coordinate = row["geometry"]["coordinates"]
                title = row["properties"]["title"]
                return coordinate, title
        
spot = input('ランドマーク ')        
coordinates1,title1 = get_coordinate(str(spot))

print("有名施設：",coordinates1,title1)