from pageParser import PageParser
from dataBaseHandler import DataBaseHandler
from utilityFunctions import FiltersOption



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
        
    def checkPrices(self, listOfFilters):
        listOfRecords = self.dataBaseHandler.getRecordsFromDataBase()
        
        listOfItems = []
                
        for element in listOfRecords:
            link = element["link"]
            recordedPrice = element["price"]
            parser = PageParser(link)
            currentPrice = parser.getPrice()
            summaryDict = {"RecordedPrice": str(recordedPrice), "CurrentPrice": str(currentPrice), "Link": str(link)}
            
            if(self.matchCurrentFilter(listOfFilters, recordedPrice, currentPrice, link)):
                listOfItems.append(summaryDict)
            
        return listOfItems
    
    def matchCurrentFilter(self, listOfFilters, recordedPrice, currentPrice, link):
        filterMatch = 1
        
        if(FiltersOption.ZERO_PRICE in listOfFilters and currentPrice != 0):
            filterMatch = 0
        
        if(FiltersOption.CHANGED_ONLY in listOfFilters and recordedPrice == currentPrice):
            filterMatch = 0
            
        if(FiltersOption.PROMOD in listOfFilters and not ("promod" in link)):
            filterMatch = 0
            
        if(FiltersOption.MONNARI in listOfFilters and not ("monnari" in link)):
            filterMatch = 0     

        if(FiltersOption.QUIOSQUE in listOfFilters and not ("quiosque" in link)):
            filterMatch = 0            
            
      
        return filterMatch
            
            
            
            
            
#uF = userFunctions()
#uF.addNewItem("https://emonnari.pl/torby/koszyki/torba-koszyk-monnari,p-62408")
#uF.addNewItem("https://emonnari.pl/akcesoria/okulary/okulary-w-ksztalcie-kociego-oka,p-60566")

#uF.checkPrices(False)