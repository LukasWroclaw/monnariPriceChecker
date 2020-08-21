from pageParser import PageParser
from dataBaseHandler import DataBaseHandler



class userFunctions(object):
    
    def __init__(self):
        self.dataBaseHandler = DataBaseHandler()
    
    def addNewItem(self, link):
        parser = PageParser(link)
        price = parser.getPrice()
        
        replayStatus = self.dataBaseHandler.addElement({"link": link, "price": price})
        return replayStatus
        
    def resetBase(self):
        self.dataBaseHandler.clearDataBase()
        
    def deleteExistingItem(self, link):
        self.dataBaseHandler.removeElement({"link": link})
        
    def checkPrices(self, changedOnly):
        listOfRecords = self.dataBaseHandler.getRecordsFromDataBase()
        
        listOfItems = []
                
        for element in listOfRecords:
            link = element["link"]
            recordedPrice = element["price"]
            parser = PageParser(link)
            currentPrice = parser.getPrice()
            summaryDict = {"RecordedPrice": str(recordedPrice), "CurrentPrice": str(currentPrice), "Link": str(link)}
            
            if(not changedOnly or recordedPrice != currentPrice):
                listOfItems.append(summaryDict)
            
        return listOfItems
            
            
            
            
            
#uF = userFunctions()
#uF.addNewItem("https://emonnari.pl/torby/koszyki/torba-koszyk-monnari,p-62408")
#uF.addNewItem("https://emonnari.pl/akcesoria/okulary/okulary-w-ksztalcie-kociego-oka,p-60566")

#uF.checkPrices(False)