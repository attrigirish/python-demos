import requests

#To Download the Data
webcontent=requests.get("http://gadgetworld.000webhostapp.com/getcategories.php")

#To Parse Json Data
data=webcontent.json()

#Iterating through list
for category in data:
    print(category['name'])




