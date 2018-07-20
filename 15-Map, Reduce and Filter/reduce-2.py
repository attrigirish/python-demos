#List of All Prouducts whose price is above 50000

import requests
from functools import reduce

url="http://gadgetworld.000webhostapp.com/getproducts.php?cid=8"
data=requests.get(url)
products=data.json()


product=reduce(lambda a,b: a if float(a['price'])>float(b['price']) else b,products)

print(product['name'])


