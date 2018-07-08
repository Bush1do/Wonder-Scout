from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

searchTerm='computers'
searchTerm= searchTerm.replace(" ","+")
print(searchTerm)
myUrl='https://www4.bing.com/search?q='+searchTerm

#Opening connection
uClient=uReq(myUrl)
pageHtml=uClient.read()
uClient.close()

#Parsing part
pageSoup=soup(pageHtml, "html.parser")

# Grab products
contain=pageSoup.findAll("li",{"class":"b_algo"})
#How many products found
len(contain)

filename="Results.csv"
f=open(filename,"w")

headers="title, desc, link\n"

f.write("")


c=0
name="g"+str(c)+".txt"
text=open(name,"w")
text.write("")
files=[text]

# Get Data
subcontain=contain[0]

for subcontain in contain:
	title= subcontain.a.text.strip()+""
	desc= subcontain.p.text.strip()+""
	link= subcontain.a["href"]

	files.insert(c,text)
	name="g"+str(c)+".txt"
	text=open(name,"w")
	text.write("")
	files[c].write(title.replace(":",",")+","+desc.replace(":",",")+","+link+"\n")

	print(title,desc,link)
	f.write(title.replace(",","|")+","+desc.replace(",","|")+","+link+"\n")
	c+=1

text.close()
f.close()