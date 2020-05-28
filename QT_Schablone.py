# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Schablone.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_bezeichung = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_bezeichung.setObjectName("lineEdit_bezeichung")
        self.verticalLayout_2.addWidget(self.lineEdit_bezeichung)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.pushButton_Geometrie_anpassen = QtWidgets.QPushButton(Dialog)
        self.pushButton_Geometrie_anpassen.setObjectName("pushButton_Geometrie_anpassen")
        self.gridLayout.addWidget(self.pushButton_Geometrie_anpassen, 3, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.doubleSpinBox_offset_x = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_offset_x.setMinimum(-100000.0)
        self.doubleSpinBox_offset_x.setMaximum(100000.0)
        self.doubleSpinBox_offset_x.setSingleStep(0.1)
        self.doubleSpinBox_offset_x.setObjectName("doubleSpinBox_offset_x")
        self.gridLayout.addWidget(self.doubleSpinBox_offset_x, 0, 1, 1, 1)
        self.doubleSpinBox_offset_y = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_offset_y.setMinimum(-100000.0)
        self.doubleSpinBox_offset_y.setMaximum(100000.0)
        self.doubleSpinBox_offset_y.setSingleStep(0.1)
        self.doubleSpinBox_offset_y.setObjectName("doubleSpinBox_offset_y")
        self.gridLayout.addWidget(self.doubleSpinBox_offset_y, 1, 1, 1, 1)
        self.doubleSpinBox_offset_phi = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_offset_phi.setMinimum(-100000.0)
        self.doubleSpinBox_offset_phi.setMaximum(100000.0)
        self.doubleSpinBox_offset_phi.setSingleStep(0.1)
        self.doubleSpinBox_offset_phi.setObjectName("doubleSpinBox_offset_phi")
        self.gridLayout.addWidget(self.doubleSpinBox_offset_phi, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Laden = QtWidgets.QPushButton(Dialog)
        self.pushButton_Laden.setObjectName("pushButton_Laden")
        self.verticalLayout.addWidget(self.pushButton_Laden)
        self.pushButton_exportieren = QtWidgets.QPushButton(Dialog)
        self.pushButton_exportieren.setObjectName("pushButton_exportieren")
        self.verticalLayout.addWidget(self.pushButton_exportieren)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Schablone"))
        self.label.setText(_translate("Dialog", "Bezeichung"))
        self.label_7.setText(_translate("Dialog", "Rotation [°]"))
        self.pushButton_Geometrie_anpassen.setText(_translate("Dialog", "Geometrie anpassen"))
        self.label_6.setText(_translate("Dialog", "Offset X [mm]"))
        self.label_5.setText(_translate("Dialog", "Offset Y [mm]"))
        self.pushButton_Laden.setText(_translate("Dialog", "importieren"))
        self.pushButton_exportieren.setText(_translate("Dialog", "exportieren"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
