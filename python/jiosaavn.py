from googlesearch import search
import urllib.request as req
from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


file = open('jio.txt','wb')
query = "tum hi aana jiosaavn"
#mystr = "<button"
#index = 0
#file = open('abcd.mp3','wb')


ff = webdriver.Firefox()
ff.get('https://www.google.com')
ActionChains(ff).context_click().send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()

for j in search(query, tld="com", stop=1):
    r = requests.get(j)
    #file.write(r.content)
    #html = req.urlopen(j)
    #soup = BS(html)
    #while(index != -1):
        #index = html.find(mystr,index+1)
        #print(index)
        #file.write(html)

file.close()
    
#print(html[5073:5273])


#mp3 = req.urlopen('https://aa.cf.saavncdn.com/287/247b628325eda0b21f808fffcf218c4e.mp3?Expires=1579627194&Signature=H4WyEgR8njllXKmNugVdRGaUpEX2LRZhl9f5crT632noF5cXl0AcjkmD37n-TTazmM~XIHZkGRMVBnDUnSSlP45zXAbdZfsoQJViASncgah1EpXpQ5WcvBysdNUP4Ngvr~vQN8jPzaQEguvBjJrDdmH1SovuetmYU1FoOs1s6aRZsm0X2Pak1ZJqlQBvAVIiOiKKS6mSTuoWZfO9Gj6-DGmypmVZHz~IjYji9wKLdD~4wcVPdd1PTDinBFmLNsXfcby~pfuwc23gTSD4NHoBahyKy4L22PByz66-F6nD6Xkvn0Maf4-u2SydaKPGrKW~wnTowy4kphx~E1SfDW4hHg__&Key-Pair-Id=APKAJB334VX63D3WJ5ZQ').read()
#file.write(mp3)
#print(html.find('<button class="play"'))