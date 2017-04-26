__author__ = "SakuraYUI"

# -*- coding:utf-8 -*-
import urllib
import urllib2

#def __init__(self):
#   self.suffix = ["nlp", "machine-learning", "data-mining", "search-enging", "recommend-system", "compute-ad", "big-data", "others"]
#   self.user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
#   self.headers = {"User-Agent" : self.user_agent}
#   self.enable = False

def getPage():
    suffix = ["nlp", "machine-learning", "data-mining", "search-enging", "recommend-system", "compute-ad", "big-data", "others"]
    for index in suffix:
        print 'starting to deal with:' + index + '...'
        getPageIndex(index)
def getPageIndex(index):
    try:
        pageNum = 1
        while True:
            url = "http://www.nlpjob.com/jobs/" + index + "/shixi/?p=" + bytes(pageNum)
            UrlNext = "http://www.nlpjob.com/jobs/" + index + "/shixi/?p=" + bytes(pageNum+1)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            getPageItem(pageCode)
            pageNum = pageNum + 1
            if outOfPage(UrlNext, pageCode):
                break
            #return pageCode
    except urllib2.URLError, e:
        if hasattr(e, "reason"):
            print "Connecting failed",e.reason
            return None
def outOfPage(url, pageCode):
    strUrl = 'class="current_page" href="' + url
    offset = pageCode.find(strUrl)
    if offset != -1:
        return False
    else:
        return True
def getPageItem(pageCode):
    itemList = []
    offset = pageCode.find('<div class="row">')
    while True:
        itemUrl = ""
        offset = pageCode.find('< a href="http://www.nlpjob.com/job/', offset)
        if offset == -1:
            break
        offset += 9
        while pageCode[offset] != '"':
            itemUrl += pageCode[offset]
            offset = offset + 1
        #print itemUrl
        itemList.append(itemUrl)
    #return itemList
    getItem(itemList)
def getItem(itemList):
    f = open('/home/lzy/workspace/pythonbug/res.txt','w') 
    dictArr = []
    for itemUrl in itemList:
        request = urllib2.Request(itemUrl)
        response = urllib2.urlopen(request)
        page = response.read().decode('utf-8')
        index = ''
        title = ''
        company = ''
        city = ''
        offset = page.find('class="selected"')
        offset = page.find('<span>', offset)
        offset += 6
        while page[offset] != '<':
            index += page[offset]
            offset = offset + 1
        offset = page.find('<h2>')
        offset = offset + 10
        offset = page.find('>', offset)
        offset = offset + 1
        while page[offset] != '<':
            title += page[offset]
            offset = offset + 1
        offset = page.find('<strong>', offset)
        offset += 8
        while page[offset] != '<':
            company += page[offset]
            offset = offset + 1
        offset = page.find('<strong>', offset)
        offset += 8
        while page[offset] != '<':
            city += page[offset]
            offset = offset + 1
        print index.strip()
        print title.strip()
        print company.strip()
        print city.strip()
        d = {}
        d['index'] = index.strip()
        d['title'] = title.strip()
        d['company'] = company.strip()
        d['city'] = city.strip()
        dictArr.append(d)
    f.wirte(dictArr)
    f.close()
           