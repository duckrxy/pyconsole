"""Get Jav Title"""
import re
import requests

class JavLibrary(object):
    __header__ = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"en-US,en;q=0.8",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Referer":"http://www.javlibrary.com/cn/",
}
    __javHomeUrl__ = 'http://www.javlibrary.com/cn/'
    __javSearchUrl__ = 'http://www.javlibrary.com/cn/vl_searchbyid.php'

    def __init__(self):
        self.session = requests.Session()
        self.session.get(self.__javHomeUrl__, headers = self.__header__)

    def GetTitle(self, text, reg):
        titles = re.findall(reg, text)
        if (titles[0]):
            return titles[0]
        else:
            return ''
    
    def SearchNumber(self, number):
        upperNumber = str(number).upper()
        query = {'keyword':upperNumber}
        r = self.session.get(self.__javSearchUrl__, headers=self.__header__,params = query)
        title = self.GetTitle(r.text, '<title>(.*) - JAVLibrary<\/title>')
        if (title == ""):
            raise Exception('Not Found')
        if (title.find('识别码搜寻结果') != -1):
            redirectedUrlReg = str.format("<a href=\"(.*)\" title=\"{0}.*\">",upperNumber)
            redirectedPageUrl = self.__javHomeUrl__ + self.GetTitle(r.text, redirectedUrlReg)
            redirectedPage = self.session.get(redirectedPageUrl, headers = self.__header__)
            redirectedTitle = self.GetTitle(redirectedPage.text, '<title>(.*) - JAVLibrary<\/title>')
            if (redirectedTitle != ""):
                return redirectedTitle
            else:
                raise Exception('Not Found')
        return title
            