import sys
from userFunctions import userFunctions
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPlainTextEdit, QTableWidget,
                             QPushButton, QApplication, QMessageBox, QLineEdit, QCheckBox)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.userFunctions = userFunctions()

        self.initUI()

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        
        self.createAddSection()
        self.createResetSection()
        self.createCheckSection()


        self.move(300, 150)
        self.setWindowTitle('Monnari Price Checker')
        self.show()
        
    def createAddSection(self):
        buttonAdd = QPushButton("Add_Price")
        self.grid.addWidget(buttonAdd, 0,0)
        
        textBoxAdd = QLineEdit(self)
        textBoxAdd.setMinimumWidth(600)
        self.grid.addWidget(textBoxAdd, 0,1)
        
        def on_buttonAdd_clicked():
            textFromBox = str(textBoxAdd.text())
            if(len(textFromBox) > 4):
                self.userFunctions.addNewItem(textFromBox)
            textBoxAdd.setText("")
            
        buttonAdd.clicked.connect(on_buttonAdd_clicked)
        
    def createResetSection(self):
        buttonReset = QPushButton("Reset_base")     
        self.grid.addWidget(buttonReset, 1,0)
        
        def on_buttonReset_clicked():
            self.userFunctions.resetBase()
            
        buttonReset.clicked.connect(on_buttonReset_clicked)  
        
        
        
    def createCheckSection(self):
        buttonCheck = QPushButton("Check_Prices")     
        self.grid.addWidget(buttonCheck, 2,0)
        
        boxCheck = QCheckBox("Show_Only_Changed")
        self.grid.addWidget(boxCheck, 2,1)
        
        textBoxPrices = QPlainTextEdit(self)
        self.grid.addWidget(textBoxPrices, 3,0)        
             
        def on_buttonCheck_clicked():
            textBoxPrices.clear()
            changedOnly = boxCheck.isChecked()
            listOfItems = self.userFunctions.checkPrices(changedOnly)
            textToShow = ""
            
            for item in listOfItems:
                textToShow = textToShow+ item + "\n"
                         
            textBoxPrices.insertPlainText(textToShow)
            
        buttonCheck.clicked.connect(on_buttonCheck_clicked) 
        
        


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()