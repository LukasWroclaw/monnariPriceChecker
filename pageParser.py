from httpHandler import HttpHandler
import re
import collections





class PageParser(object):
    
    def __init__(self, url):
        self.urlAddress = url
        
        handler = HttpHandler()
        
        content = handler.getContentFromUrl(self.urlAddress)
        self.strPageContent = str(content)


    def extractNumberFromString(self, str):
        result = re.findall("\d+", str)
           
        strResult = ""
        for element in result:
            strResult += element
        try:    
            intResult = int(strResult)
        except:
            return 999999
        
        return intResult

    def getPrice(self):
        begin = self.strPageContent.find("price\\")
    
        if(begin != (-1)):
            priceAreaString = self.strPageContent[begin: (begin+40)]
            splittedPriceString = priceAreaString.split(".")
            plnPart = splittedPriceString[0]
            grPart = splittedPriceString[1]
            
            
            plnInt = self.extractNumberFromString(plnPart)
            grInt = self.extractNumberFromString(grPart)
            
            price = float(plnInt) + float(grInt/100)
            
            return price
                
        else:
            return 0



##parser = PageParser("https://emonnari.pl/odziez/bluzki/wizytowe/wizytowa-bluzka-z-wiazaniem-z-tylu,p-58908")
##parser.getPrice()

