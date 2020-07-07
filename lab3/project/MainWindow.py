# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Main Window") 

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)  

        popLabel = QLabel("Population Size") 
        popLabel.setAlignment(QtCore.Qt.AlignLeft)
        gridLayout.addWidget(popLabel, 0, 0)
        
        probLabel = QLabel("Probability Of Mutation/Crossover") 
        probLabel.setAlignment(QtCore.Qt.AlignLeft)
        gridLayout.addWidget(probLabel, 1, 0)
        
        genLabel = QLabel("Number Of Generations") 
        genLabel.setAlignment(QtCore.Qt.AlignLeft)
        gridLayout.addWidget(genLabel, 2, 0)

        popText = QLineEdit() 
        popText.setFixedSize(QSize(150, 25))
        popText.setAlignment(QtCore.Qt.AlignRight)
        gridLayout.addWidget(popText, 0, 1)
        
        probText = QLineEdit() 
        probText.setFixedSize(QSize(150, 25))
        probText.setAlignment(QtCore.Qt.AlignRight)
        gridLayout.addWidget(probText, 1, 1)
        
        genText = QLineEdit() 
        genText.setFixedSize(QSize(150, 25))
        genText.setAlignment(QtCore.Qt.AlignRight)
        gridLayout.addWidget(genText, 2, 1)