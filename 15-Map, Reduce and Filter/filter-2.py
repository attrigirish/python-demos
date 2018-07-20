products=[{'name':'Samsung Galaxy S9','price':54000},{'name':'Vivo X21','price':35000},{'name':'Apple Iphone X','price':83000}]

#List of All Prouducts whose price is above 50000

result=list(filter(lambda x: x['price']<50000,products))

for product in result:
    print("Name : " + product['name'])



http://gadgetworld.000webhostapp.com/getproducts.php?cid=8


import requests
data=requests.get(url)
products=data.json()

#Apply Filter
