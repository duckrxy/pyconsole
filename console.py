import javlibrary
import time
import re
import os

# print(os.path.curdir)
# print(os.path.abspath(os.path.curdir))
os.path.join(os.path.abspath(os.path.curdir), 'test')
jav = javlibrary.JavLibrary()
# info = jav.SearchNumber('adn-011')
# print(info['actress'])
# print(info['title'])
workingFolder = '\\\\xiazaibao_e547\\移动磁盘-C(Elements)\\shared_x9\\duckrxy1(107316079)\\TDDOWNLOAD\\AV\\Japan\\'
print(workingFolder)
#os.mkdir(os.path.join(os.path.abspath(os.path.curdir), 'test'))
#os.rmdir(os.path.join(os.path.abspath(os.path.curdir), 'test'))
result = os.scandir(workingFolder)
for item in result:
    #print(item.name, item.path)
    print(item.name)
    print(re.findall('^([a-zA-Z]{2,5})-{0,1}([0-9]{2,5})([abcrABCR]{0,1}).(.*)', item.name))
    regSplit = re.findall('^([a-zA-Z]{2,5})-{0,1}([0-9]{2,5})([abcrABCR]{0,1}).(.*)', item.name)
    avnumber = regSplit[0][0] + '-' + regSplit[0][1]
    print(avnumber)
    javResult = jav.SearchNumber(avnumber)
    print(javResult)
    #print(jav.SearchNumber(re.findall('^([a-zA-Z]{2,5}-[0-9]{2,4}).*', item.name)[0]))
    time.sleep(1)

    
