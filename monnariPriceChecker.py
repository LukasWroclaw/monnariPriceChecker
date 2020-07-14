import sys
import time
from userFunctions import userFunctions
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPlainTextEdit, QTableWidget, QTableWidgetItem,
                             QPushButton, QApplication, QMessageBox, QLineEdit, QCheckBox)



numberOfRowsInATable = 300


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.userFunctions = userFunctions()
        self.tableWidget = 0;
        self.initUI()

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        
        self.createAddSection()
        self.createRemoveSection()
        self.createResetSection()
        self.createCheckSection()
        self.createStatusInfo()
        self.createTable()



        ##self.move(300, 150)
        self.setWindowTitle('Monnari Price Checker')
        self.setGeometry(100, 100, 900, 900) 
        self.show()
        
    def createAddSection(self):
        buttonAdd = QPushButton("Add_Item")
        self.grid.addWidget(buttonAdd, 0,0)
        
        textBoxAdd = QLineEdit(self)
        textBoxAdd.setMinimumWidth(600)
        self.grid.addWidget(textBoxAdd, 0,1)
        
        def on_buttonAdd_clicked():
            textFromBox = str(textBoxAdd.text())
            if(len(textFromBox) > 4):
                self.userFunctions.addNewItem(textFromBox)
            textBoxAdd.setText("")
            self.updateStatusInfo("New element added succesfully")
            
            
        buttonAdd.clicked.connect(on_buttonAdd_clicked)
        
    def createRemoveSection(self):
        buttonRemove = QPushButton("Remove_Item")
        self.grid.addWidget(buttonRemove, 1, 0)
        
        textBoxRemove = QLineEdit(self)
        textBoxRemove.setMinimumWidth(600)
        self.grid.addWidget(textBoxRemove, 1,1)
        
        def on_buttonRemove_clicked():
            textFromBox = str(textBoxRemove.text())
            if(len(textFromBox) > 4):
                self.userFunctions.deleteExistingItem(textFromBox)
            textBoxRemove.setText("")
            
        buttonRemove.clicked.connect(on_buttonRemove_clicked)
        
        
    def createResetSection(self):
        buttonReset = QPushButton("Reset_base")     
        self.grid.addWidget(buttonReset, 1,3)
        
        def on_buttonReset_clicked():
            self.userFunctions.resetBase()
            
        buttonReset.clicked.connect(on_buttonReset_clicked)  
        
        
        
    def createCheckSection(self):
        buttonCheck = QPushButton("Check_Prices")     
        self.grid.addWidget(buttonCheck, 3,0)
        
        boxCheck = QCheckBox("Show_Only_Changed")
        boxCheck.setChecked(True)
        self.grid.addWidget(boxCheck, 3,1)
        
               
        def on_buttonCheck_clicked():
            self.resetTable()       
            changedOnly = boxCheck.isChecked()
            listOfItems = self.userFunctions.checkPrices(changedOnly)

            self.updateTable(listOfItems)
                                   
        buttonCheck.clicked.connect(on_buttonCheck_clicked)
        
    def createStatusInfo(self):
        self.textBoxStatus = QLineEdit(self)
        self.textBoxStatus.setMinimumWidth(300)
        self.grid.addWidget(self.textBoxStatus, 4,0)
        self.textBoxStatus.setText("")
        
    def updateStatusInfo(self, text):
        self.textBoxStatus.setText(text)



             
    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(numberOfRowsInATable)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Recorded price', 'Current price', 'Link'])
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setColumnWidth(2,650)
                       
        self.grid.addWidget(self.tableWidget, 5,0, 3, 3)
        
    def updateTable(self, listOfItems):
        rowIncrement = 0
        
        for element in listOfItems:
            self.tableWidget.setItem(rowIncrement,0, QTableWidgetItem(element["RecordedPrice"]))
            self.tableWidget.setItem(rowIncrement,1, QTableWidgetItem(element["CurrentPrice"]))
            self.tableWidget.setItem(rowIncrement,2, QTableWidgetItem(element["Link"]))
            rowIncrement = rowIncrement + 1
        
    def resetTable(self):
        for i in range(1, numberOfRowsInATable - 2):
            self.tableWidget.setItem(i,0, QTableWidgetItem(""))
            self.tableWidget.setItem(i,1, QTableWidgetItem(""))
            self.tableWidget.setItem(i,2, QTableWidgetItem(""))
        
        
        
        
        
        


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()