import javlibrary
import time
import re
import os

# print(os.path.curdir)
# print(os.path.abspath(os.path.curdir))
os.path.join(os.path.abspath(os.path.curdir), 'test')
jav = javlibrary.JavLibrary()
#print(jav.SearchNumber('adn-011'))
info = jav.SearchNumber('adn-011')
print(info['actress'])
print(info['title'])
#os.mkdir(os.path.join(os.path.abspath(os.path.curdir), 'test'))
#os.rmdir(os.path.join(os.path.abspath(os.path.curdir), 'test'))
# result = os.scandir('\\\\TIGER-NAS\\Ad\\日本专业\\浜崎真緒\\')
# for item in result:
#     #print(item.name, item.path)
#     print(item.name)
#     print(re.findall('^([a-zA-Z]{2,5}-[0-9]{2,5}).*', item.name))
#     print(jav.SearchNumber(re.findall('^([a-zA-Z]{2,5}-[0-9]{2,4}).*', item.name)[0]))
#     time.sleep(1)

    
