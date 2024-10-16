import requests
from bs4 import BeautifulSoup
def getdata(url):
 r = requests.get(url)
 return r.content
htmldata = getdata("https://sjcetpalai.ac.in")
soup = BeautifulSoup(htmldata,'html.parser')
print("Gayathri Suresh")
print("28")
links = soup.find_all("a")
print("Total number of links : ",len(links))
for link in links:
 if link.get("href") != "":
  print("Link :",link.get("href"),"Text :",link.string)