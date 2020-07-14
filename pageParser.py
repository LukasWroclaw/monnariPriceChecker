from httpHandler import HttpHandler
import re





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
        if("promod" in self.urlAddress):
            return self.getPricePromod()
        elif("monnari" in self.urlAddress):
            return self.getPriceMonnari()
        elif("quiosque" in self.urlAddress):
            return self.getPriceQuiosque()
        else:
            return 0
        
        
        return self.getPriceMonnari()

    def getPriceMonnari(self):
        begin = self.strPageContent.find("price\\")
    
        if(begin != (-1)):
            priceAreaString = self.strPageContent[begin: (begin+40)]
            splittedPriceString = priceAreaString.split(".")
            plnPart = splittedPriceString[0]
            grPart = splittedPriceString[1][:4]
            
            
            plnInt = self.extractNumberFromString(plnPart)
            grInt = self.extractNumberFromString(grPart)
            
            price = float(plnInt) + float(grInt/100)
            
            return price
                
        else:
            return 0
        
    def getPricePromod(self):
        begin = self.strPageContent.find("unitprice_ati\\")
    
        if(begin != (-1)):
            priceAreaString = self.strPageContent[begin: (begin+40)]
            splittedPriceString = priceAreaString.split(".")
            plnPart = splittedPriceString[0]
            grPart = splittedPriceString[1][:4]
            
            
            plnInt = self.extractNumberFromString(plnPart)
            grInt = self.extractNumberFromString(grPart)
            
            price = float(plnInt) + float(grInt/100)
            
            return price
                
        else:
            return 0
        
    def getPriceQuiosque(self):
        begin = self.strPageContent.find("finalPrice\" class=\"price-wrapper \" ><span class=\"price\">")
            
        if(begin != (-1)):
            priceAreaString = self.strPageContent[begin : (begin+70)]
            splittedPriceString = priceAreaString.split(",")
            plnPart = splittedPriceString[0]
            grPart = splittedPriceString[1][:4]
            
            plnInt = self.extractNumberFromString(plnPart)
            grInt = self.extractNumberFromString(grPart)
            
            price = float(plnInt) + float(grInt/100)
            
            return price
                
        else:
            return 0
        
        


#parser = PageParser("https://quiosque.pl/bezowy-prazkowany-sweter-6jb001102.html")#"https://quiosque.pl/czarny-kardigan-z-blyszczacymi-kolkami-6ig002299.html")
#print("Cena",parser.getPriceQuiosque())

##parser = PageParser("https://emonnari.pl/odziez/bluzki/wizytowe/wizytowa-bluzka-z-wiazaniem-z-tylu,p-58908")
##parser.getPrice()

