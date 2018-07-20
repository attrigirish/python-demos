#List of All Prouducts whose price is above 50000

import requests

url="http://gadgetworld.000webhostapp.com/getproducts.php?cid=8"
data=requests.get(url)
products=data.json()

result=list(filter(lambda x: float(x['price'])<50000,products))

for product in result:
    print("Name : " + product['name'])

