import re
import requests
from bs4 import BeautifulSoup
import csv

session = requests.Session()
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,en-US;q=0.4",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.aqistudy.cn",
    "Referer": "https://www.aqistudy.cn/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

fieldnames = ['Date', 'AQI', 'PM2.5', 'PM10']
result = []
for month in range(1, 13):
    if month < 10:
        strMonth = '20160'
    else:
        strMonth = '2016'
    strMonth = strMonth + str(month)
    url = "https://www.aqistudy.cn/historydata/daydata.php?city=%E6%98%86%E6%98%8E&month={0}".format(
        strMonth)
    r = session.get(url, headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find_all('tr')
    for row in table:
        print(row.get_text())
        for td in row.children:
            print(td.string)
         

        


    # htmltree = html.fromstring(r.content)
    # table = htmltree.xpath('//td/text()')
    # dateindex = 0
    # while table[dateindex].startswith('2016-'):
    #     result.append([table[dateindex],table[dateindex + 1],table[dateindex + 3],table[dateindex +4]])
    #     dateindex += 10

with open('aqi12.csv', 'w') as csvfile:
    csvwriter = csv.DictWriter(csvfile,fieldnames = fieldnames)
    for row in result:
        csvwriter.writerow({'Date':row[0], 'AQI':row[1],'PM2.5':row[2],'PM10':row[3]})