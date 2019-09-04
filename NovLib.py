# Created By AlamarW
# GUI Partially thank to: PyQt5 UI code generator 5.13.0
# Text thanks to Gutenberg and their free library

from PyQt5 import QtCore, QtGui, QtWidgets
from nltk.corpus import gutenberg as gb
from nltk.tokenize.treebank import TreebankWordTokenizer as TWT
from nltk.tokenize.treebank import TreebankWordDetokenizer as  TWD
from nltk.tokenize import sent_tokenize
    
class text(object):
    #setting up the detokenizer function and the name|filename of the text
    t = TWT()
    d = TWD()
    libd_storage = []
    raw_libd_text =[]
    
    textDict = {
        "Alice in Wonderland"          : "carroll-alice.txt",
        "Moby Dick"                    : "melville-moby_dick.txt",
        "Leaves of Grass"              : "whitman-leaves.txt",
        "King James Bible"             : "bible-kjv.txt",
        "Hamlet"                       : "shakespeare-hamlet.txt",
        "Emma"                         : "austen-emma.txt",
        "Persuasion"                   : "austen-persuasion.txt",
        "Sense and Sensibility"        : "austen-sense.txt",
        "Poems of William Blake"       : "blake-poems.txt",
        "The Wisdom of Father Brown"   : "chesterton-brown.txt",
        "The Man Who Was Thursday"     : "chesterton-thursday.txt",
        "Paradise Lost"                : "milton-paradise.txt",
        "Julius Caesar"                : "shakespeare-caesar.txt",
        "Macbeth"                      : "shakespeare-macbeth.txt"
        }
           
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Test")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setReadOnly
        self.textBrowser.setGeometry(QtCore.QRect(470, 30, 311, 521))
        self.textBrowser.setObjectName("textBrowser")
        
        self.excLib = QtWidgets.QPushButton(self.centralwidget)
        self.excLib.setGeometry(QtCore.QRect(250, 220, 110, 60))
        self.excLib.setObjectName("excLib")
        self.excLib.clicked.connect(self.replace_text)

        self.impText = QtWidgets.QPushButton(self.centralwidget)
        self.impText.setGeometry(QtCore.QRect(250, 60, 110, 60))
        self.impText.setObjectName("Import Text")
        self.impText.clicked.connect(self.show_text)
        
        #setting comboBox where each item holds the text that it's referencing
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 131, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(sorted(text.textDict))
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 85, 16))
        self.label.setObjectName("label")
        
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 360, 163, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.clicked.connect(self.all_libd_text)
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 380, 200, 18))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.clicked.connect(self.lib_sent_only)
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 200, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 260, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 60, 13))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 47, 13))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        
        self.clrBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clrBtn.setGeometry(QtCore.QRect(20, 430, 111, 61))
        self.clrBtn.setObjectName("clrBtn")
        self.clrBtn.clicked.connect(self.clear_libs)

        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        self.menuFil = QtWidgets.QMenu(self.menubar)
        self.menuFil.setObjectName("menuFil")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.setShortcut("Ctrl+Q")
        self.actionClose.setStatusTip('Leave NovLib')
        self.actionClose.triggered.connect(self.close_application)
        self.menuFil.addAction(self.actionClose)
        self.menubar.addAction(self.menuFil.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NovLibs"))
        self.excLib.setText(_translate("MainWindow", "NovLib"))
        self.impText.setText(_translate("MainWindow", "Import Text"))
        self.label.setText(_translate("MainWindow", "Novel To Lib"))
        self.radioButton.setText(_translate("MainWindow", "View Entire Text"))
        self.radioButton_2.setText(_translate("MainWindow", "View Lib\'d Sentences Only"))
        self.label_2.setText(_translate("MainWindow", "Replace"))
        self.label_3.setText(_translate("MainWindow", "With"))
        self.label_4.setText(_translate("MainWindow", "Lib\'d Text"))
        self.clrBtn.setText(_translate("MainWindow", "Clear Libs"))
        self.menuFil.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

    #takes the dictionary from text.textDict and uses the values to search the gutenberg corpora
    def show_text(self, MainWindow):
        text.libd_storage = []
        self.textBrowser.clear()
        comboText = self.comboBox.currentText()
        for i in text.textDict:
            if comboText == i:
                rawText = gb.raw(text.textDict[i])
                self.textBrowser.append(rawText)
                
    #Replaces a word in the text with a word of user's choice
    def replace_text(self, MainWindow):
        original_word = self.lineEdit.text()
        lib_word = self.lineEdit_2.text()
       
        if lib_word not in text.libd_storage:
            text.libd_storage.append(lib_word)
            
        raw = self.textBrowser.toPlainText()
        self.textBrowser.clear()
        word_tokens = text.t.tokenize(raw)
        
        #for loop to replace original_word w/ lib_word
        for idx, w in enumerate(word_tokens):
            if w == original_word:
                word_tokens[idx] = lib_word

        detokenized_words = text.d.detokenize(word_tokens)
        
        #it's a surprise tool that will help us later: ref to all_libd_text method
        text.raw_libd_text = detokenized_words 
        sents = sent_tokenize(detokenized_words)
        
        for sentence in sents:
            self.textBrowser.append(sentence)
            self.textBrowser.append("\n")

    #"Clears" the libs, what it actually does is reload the text that represents what's in the combobox
    def clear_libs(self, MainWindow):
        self.textBrowser.clear()
        comboText = self.comboBox.currentText()
        
        for i in text.textDict:
            if comboText == i:
                rawText = gb.raw(text.textDict[i])
                self.textBrowser.append(rawText)

    #Uses the text.libd_storage to display only sentences with the the words in text.libd_storage
    def lib_sent_only(self, MainWindow):
        #print(text.libd_storage)
        raw = self.textBrowser.toPlainText()
        sents = sent_tokenize(raw)
        self.textBrowser.clear()
        temp_sentence_storage = []
        
        #maybe overly complicated but it does exactly what I needed it to do, somewhat
        for sentence in sents:
            words = text.t.tokenize(sentence)
            for w in words:
                for i in text.libd_storage:
                    if i == w:
                        temp_sentence_storage.append(sentence)
                     
        real_sentence_storage = list(dict.fromkeys(temp_sentence_storage))
        
        for i in real_sentence_storage:
            self.textBrowser.append(i)
            self.textBrowser.append("\n")

    def all_libd_text(self, MainWindow):
        self.textBrowser.clear()
        changed_text = text.raw_libd_text
        sents = sent_tokenize(changed_text)
        for sentence in sents:
            self.textBrowser.append(sentence)
            self.textBrowser.append("\n")
                
    #closes the gotdang application
    def close_application(self):
        sys.exit()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
