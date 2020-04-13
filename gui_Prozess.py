from PyQt5 import QtCore, QtGui, QtWidgets
import model_Prozess
from file_handling import FileHandling
import copy
import my_Json

import QT_Prozess as mw



class gui_Prozess(FileHandling):

    def __init__(self, parent):
        FileHandling.__init__(self, ".pro")
        self.Dialog = QtWidgets.QDialog(parent)
        self.ui = mw.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.new_prozess: model_Prozess.Prozess = None
        self.prozess: model_Prozess.Prozess = None

        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)

        self.ui.pushButton_Laden.clicked.connect(self.pushButton_Laden)
        self.ui.pushButton_exportieren.clicked.connect(self.pushButton_exportieren)


    def show(self, prozess: model_Prozess.Prozess):
        self.ui.lineEdit_bezeichung.setText(prozess.name)

        self.prozess = prozess
        self.new_prozess = copy.deepcopy(prozess)

        self.Dialog.show()
        self.Dialog.exec()

    def pushButton_Laden(self):
        data = self.open_file()
        if data is not None:
            self.new_prozess.__init__(**data)
        self.update_gui()

    def pushButton_exportieren(self):
        self.update_model()
        self.safe_file(self.new_prozess, self.new_prozess.name)

    def accepted(self):
        self.update_model()
        self.prozess.__dict__.update(self.new_prozess.__dict__)
        # print(self.new_prozess.__dict__)
        # # self.arbeitsschritt.__dict__.update(self.new_arbeitsschritt.__dict__)
        # print("blub")
        # print(my_Json.dumps(self.new_prozess))
        # self.prozess.__init__(**my_Json.symply_dumps(self.new_prozess))


    def rejected(self):
        pass

    def update_model(self):
        self.new_prozess.name = self.ui.lineEdit_bezeichung.text()

    def update_gui(self):
        self.ui.lineEdit_bezeichung.setText(self.new_prozess.name)