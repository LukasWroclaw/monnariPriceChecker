import xlwt
import xlrd
from utilityFunctions import ReplayStatus

import unittest

testIt = 0





class DataBaseHandler(object):
    
    def __init__(self, dataBase = "dataBase.xls"):
        self.baseName = dataBase
        
    def checkIfBaseExist(self):
        try:
            book = xlrd.open_workbook(self.baseName)
            book.release_resources()
            return 1
        except:
            return 0
        
    def getRecordsFromDataBase(self):
        
        if(self.checkIfBaseExist == 0):
            return 0
        
        book = xlrd.open_workbook(self.baseName)
        sheet = book.sheet_by_name("1")
        
        inc = 1
        listOfRecords = []
        
        while True:
            try:
                linkCell = sheet.cell(inc,0)
                link = str(linkCell.value)
                priceCell = sheet.cell(inc,1)
                price = float(priceCell.value)
                element = {"link": link, "price": price}
                listOfRecords.append(element)
            except:
                break
            
            if len(link) < 2:
                break
            
            inc = inc + 1
                   
        return listOfRecords
    
    def addElementsToExcel(self, listOfElements):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('1')

        ws.write(0, 0, "Link")
        ws.write(0, 1, "Price")
        
        inc = 1
        
        for element in listOfElements:
            ws.write(inc, 0, element["link"])
            ws.write(inc, 1, element["price"])
            inc = inc + 1

        wb.save(self.baseName)
        
    def addElement(self, newElement):

        
        if(self.checkIfBaseExist == 0):
            self.addElementsToExcel([newElement])
            return ReplayStatus.OK
            
        
        listOfRecords = self.getRecordsFromDataBase()
        
        if(newElement in listOfRecords):
            return ReplayStatus.DUPLICATE
        
        listOfRecords.append(newElement)
        self.addElementsToExcel(listOfRecords)
            
        return ReplayStatus.OK
        
        
    def removeElement(self, elementToRemove):
        if(self.checkIfBaseExist == 0):
            print("Error, list is empty")
            return ReplayStatus.NOK
        else:
            listOfRecords = self.getRecordsFromDataBase()
            found = 0
            buffor = {}
            
            for element in listOfRecords:
                if(element["link"] == elementToRemove["link"]):
                    buffor = element
                    found = 1
            
            if(found == 1):
                listOfRecords.remove(buffor)
                self.addElementsToExcel(listOfRecords)
                return ReplayStatus.OK
            else:
                print("Error, element not found")
                return ReplayStatus.NOK
                
    def clearDataBase(self):
        self.addElementsToExcel([])
                
        
    
class TestingClass(unittest.TestCase):
  

 

    def test_numberOfElements(self):
        expectedList = [{"link": "Link1", "price": 1}, {"link": "Link2", "price": 2}]
        dataBaseHandler = DataBaseHandler("testBase.xls")
        listOfRecords = dataBaseHandler.getRecordsFromDataBase()
        self.assertEqual(listOfRecords, expectedList)
        
    def test_addtionOfElements(self):
        expectedList = [{"link": "Link1", "price": 1}, {"link": "Link2", "price": 2}]
        dataBaseHandler = DataBaseHandler("testBase1.xls")
        dataBaseHandler.addElementsToExcel(expectedList)
        listOfRecords = dataBaseHandler.getRecordsFromDataBase()
        self.assertEqual(listOfRecords, expectedList)
        
              
    def test_addAndRemoveElement(self):
        expectedList = [{"link": "Link1", "price": 1}, {"link": "Link2", "price": 2}]
        dataBaseHandler = DataBaseHandler("testBase.xls")
        listOfRecords = dataBaseHandler.getRecordsFromDataBase()
        self.assertEqual(listOfRecords, expectedList)
        
        expectedList = [{"link": "Link1", "price": 1}, {"link": "Link2", "price": 2}, {"link": "Link3", "price": 3}]
        resultFromAddition = dataBaseHandler.addElement({"link": "Link3", "price": 3})
        listOfRecords = dataBaseHandler.getRecordsFromDataBase()
        self.assertEqual(listOfRecords, expectedList)
        self.assertEqual(ReplayStatus.OK, resultFromAddition)
        
        expectedList = [{"link": "Link1", "price": 1}, {"link": "Link2", "price": 2}]
        resultFromRemoval = dataBaseHandler.removeElement({"link": "Link3", "price": 3})
        listOfRecords = dataBaseHandler.getRecordsFromDataBase()
        self.assertEqual(listOfRecords, expectedList)
        self.assertEqual(ReplayStatus.OK, resultFromRemoval)
        
    def test_addDuplicatedElement(self):
        expectedList = [{"link": "Link1", "price": 1}, {"link": "Link2", "price": 2}]
        dataBaseHandler = DataBaseHandler("testBase.xls")
        resultFromAddition = dataBaseHandler.addElement({"link": "Link2", "price": 2})
        listOfRecords = dataBaseHandler.getRecordsFromDataBase()
        self.assertEqual(listOfRecords, expectedList)
        self.assertEqual(ReplayStatus.DUPLICATE, resultFromAddition)
        
        
    def test_removeEverything(self):
        expectedList = []
        dataBaseHandler = DataBaseHandler("testBase2.xls")
        dataBaseHandler.clearDataBase()
        listOfRecords = dataBaseHandler.getRecordsFromDataBase()
        self.assertEqual(listOfRecords, expectedList)
        

if(testIt):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingClass)
    unittest.TextTestRunner(verbosity=2).run(suite)  