from pageParser import PageParser
from dataBaseHandler import DataBaseHandler



class userFunctions(object):
    
    def __init__(self):
        self.dataBaseHandler = DataBaseHandler()
    
    def addNewItem(self, link):
        parser = PageParser(link)
        price = parser.getPrice()
        
        self.dataBaseHandler.addElement({"link": link, "price": price})
        
    def deleteExistingItem(self, link):    
        self.dataBaseHandler.removeElement({"link": link})
        
    def checkPrices(self):
        listOfRecords = self.dataBaseHandler.getRecordsFromDataBase()
        
        for element in listOfRecords:
            link = element["link"]
            recordedPrice = element["price"]
            parser = PageParser(link)
            currentPrice = parser.getPrice()
            print("Recorded price", recordedPrice, "current price", currentPrice, "Link", link)
            
            
            
            
            
uF = userFunctions()
uF.addNewItem("https://emonnari.pl/torby/koszyki/torba-koszyk-monnari,p-62408")
uF.addNewItem("https://emonnari.pl/akcesoria/okulary/okulary-w-ksztalcie-kociego-oka,p-60566")

uF.checkPrices()