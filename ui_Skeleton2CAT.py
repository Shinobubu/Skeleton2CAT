# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Skeleton2CATvNSicG.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

pysideVersion = 6
try:
    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
        QDialog, QDoubleSpinBox, QGridLayout, QGroupBox,
        QHBoxLayout, QHeaderView, QLabel, QLayout,
        QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
        QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
        QWidget)
except:
    pysideVersion = 2   
    from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
            QMetaObject, QObject, QPoint, QRect,
            QSize, QTime, QUrl, Qt)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
            QFont, QFontDatabase, QGradient, QIcon,
            QImage, QKeySequence, QLinearGradient, QPainter,
            QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide2.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
            QDialog, QDoubleSpinBox, QGridLayout, QGroupBox,
            QHBoxLayout, QHeaderView, QLabel, QLayout,
            QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
            QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
            QWidget)

class Ui_skeleton2CatDialog(object):
    def setupUi(self, skeleton2CatDialog):
        if not skeleton2CatDialog.objectName():
            skeleton2CatDialog.setObjectName(u"skeleton2CatDialog")
        skeleton2CatDialog.resize(991, 681)
        self.verticalLayout = QVBoxLayout(skeleton2CatDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.saveSettingsBtn = QToolButton(skeleton2CatDialog)
        self.saveSettingsBtn.setObjectName(u"saveSettingsBtn")

        self.toolbarLayout.addWidget(self.saveSettingsBtn)

        self.loadSettingsBtn = QToolButton(skeleton2CatDialog)
        self.loadSettingsBtn.setObjectName(u"loadSettingsBtn")

        self.toolbarLayout.addWidget(self.loadSettingsBtn)

        self.toolbarSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.toolbarLayout.addItem(self.toolbarSpacer)

        self.resetSettingsBtn = QToolButton(skeleton2CatDialog)
        self.resetSettingsBtn.setObjectName(u"resetSettingsBtn")

        self.toolbarLayout.addWidget(self.resetSettingsBtn)


        self.verticalLayout.addLayout(self.toolbarLayout)

        self.tabWidget = QTabWidget(skeleton2CatDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainTab.sizePolicy().hasHeightForWidth())
        self.mainTab.setSizePolicy(sizePolicy1)
        self.formLayoutWidget = QWidget(self.mainTab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 261, 241))
        self.gridLayout_3 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.CATBoxModeDisplayChk = QCheckBox(self.formLayoutWidget)
        self.CATBoxModeDisplayChk.setObjectName(u"CATBoxModeDisplayChk")

        self.gridLayout_3.addWidget(self.CATBoxModeDisplayChk, 3, 0, 1, 1)

        self.lengthAxisLabel = QLabel(self.formLayoutWidget)
        self.lengthAxisLabel.setObjectName(u"lengthAxisLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lengthAxisLabel.sizePolicy().hasHeightForWidth())
        self.lengthAxisLabel.setSizePolicy(sizePolicy2)
        self.lengthAxisLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lengthAxisLabel, 4, 0, 1, 1)

        self.taperfactorLabel = QLabel(self.formLayoutWidget)
        self.taperfactorLabel.setObjectName(u"taperfactorLabel")
        sizePolicy2.setHeightForWidth(self.taperfactorLabel.sizePolicy().hasHeightForWidth())
        self.taperfactorLabel.setSizePolicy(sizePolicy2)
        self.taperfactorLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.taperfactorLabel, 0, 0, 1, 1)

        self.moveBaseToCharacterChk = QCheckBox(self.formLayoutWidget)
        self.moveBaseToCharacterChk.setObjectName(u"moveBaseToCharacterChk")

        self.gridLayout_3.addWidget(self.moveBaseToCharacterChk, 1, 0, 1, 1)

        self.deleteOldBonesChk = QCheckBox(self.formLayoutWidget)
        self.deleteOldBonesChk.setObjectName(u"deleteOldBonesChk")

        self.gridLayout_3.addWidget(self.deleteOldBonesChk, 2, 0, 1, 1)

        self.taperFactorsFlt = QDoubleSpinBox(self.formLayoutWidget)
        self.taperFactorsFlt.setObjectName(u"taperFactorsFlt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.taperFactorsFlt.sizePolicy().hasHeightForWidth())
        self.taperFactorsFlt.setSizePolicy(sizePolicy3)
        self.taperFactorsFlt.setMaximum(1.000000000000000)
        self.taperFactorsFlt.setSingleStep(0.010000000000000)
        self.taperFactorsFlt.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.taperFactorsFlt.setValue(0.250000000000000)

        self.gridLayout_3.addWidget(self.taperFactorsFlt, 0, 1, 1, 1)

        self.lengthAxisCmb = QComboBox(self.formLayoutWidget)
        self.lengthAxisCmb.addItem("")
        self.lengthAxisCmb.addItem("")
        self.lengthAxisCmb.setObjectName(u"lengthAxisCmb")

        self.gridLayout_3.addWidget(self.lengthAxisCmb, 4, 1, 1, 1)

        self.attemptRepairChk = QCheckBox(self.formLayoutWidget)
        self.attemptRepairChk.setObjectName(u"attemptRepairChk")

        self.gridLayout_3.addWidget(self.attemptRepairChk, 5, 0, 1, 1)

        self.transferSkinGroup = QGroupBox(self.mainTab)
        self.transferSkinGroup.setObjectName(u"transferSkinGroup")
        self.transferSkinGroup.setGeometry(QRect(30, 280, 291, 111))
        self.gridLayoutWidget = QWidget(self.transferSkinGroup)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 276, 80))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.thresholdLabel = QLabel(self.gridLayoutWidget)
        self.thresholdLabel.setObjectName(u"thresholdLabel")
        sizePolicy2.setHeightForWidth(self.thresholdLabel.sizePolicy().hasHeightForWidth())
        self.thresholdLabel.setSizePolicy(sizePolicy2)
        self.thresholdLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.thresholdLabel, 0, 0, 1, 1)

        self.skinTransferThresholdflt = QDoubleSpinBox(self.gridLayoutWidget)
        self.skinTransferThresholdflt.setObjectName(u"skinTransferThresholdflt")

        self.gridLayout_4.addWidget(self.skinTransferThresholdflt, 0, 1, 1, 1)

        self.skinTransferMatchByName = QCheckBox(self.gridLayoutWidget)
        self.skinTransferMatchByName.setObjectName(u"skinTransferMatchByName")

        self.gridLayout_4.addWidget(self.skinTransferMatchByName, 1, 0, 1, 1)

        self.moveSkinsToCATChk = QCheckBox(self.mainTab)
        self.moveSkinsToCATChk.setObjectName(u"moveSkinsToCATChk")
        self.moveSkinsToCATChk.setGeometry(QRect(20, 260, 134, 20))
        self.tabWidget.addTab(self.mainTab, "")
        self.boneLabelsTab = QWidget()
        self.boneLabelsTab.setObjectName(u"boneLabelsTab")
        sizePolicy1.setHeightForWidth(self.boneLabelsTab.sizePolicy().hasHeightForWidth())
        self.boneLabelsTab.setSizePolicy(sizePolicy1)
        self.boneLabelsTab.setMinimumSize(QSize(967, 555))
        self.horizontalLayout_3 = QHBoxLayout(self.boneLabelsTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.boneLabelTable = QTableWidget(self.boneLabelsTab)
        if (self.boneLabelTable.columnCount() < 14):
            self.boneLabelTable.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.boneLabelTable.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        if (self.boneLabelTable.rowCount() < 50):
            self.boneLabelTable.setRowCount(50)
        self.boneLabelTable.setObjectName(u"boneLabelTable")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.boneLabelTable.sizePolicy().hasHeightForWidth())
        self.boneLabelTable.setSizePolicy(sizePolicy4)
        self.boneLabelTable.setAlternatingRowColors(True)
        self.boneLabelTable.setSortingEnabled(True)
        self.boneLabelTable.setRowCount(50)
        self.boneLabelTable.setColumnCount(14)

        self.verticalLayout_3.addWidget(self.boneLabelTable)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.boneLabelsTab, "")
        self.boneSizeTab = QWidget()
        self.boneSizeTab.setObjectName(u"boneSizeTab")
        self.verticalLayout_5 = QVBoxLayout(self.boneSizeTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sizeTable = QTableWidget(self.boneSizeTab)
        if (self.sizeTable.columnCount() < 3):
            self.sizeTable.setColumnCount(3)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.sizeTable.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.sizeTable.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.sizeTable.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        if (self.sizeTable.rowCount() < 8):
            self.sizeTable.setRowCount(8)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.sizeTable.setVerticalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.sizeTable.setVerticalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.sizeTable.setVerticalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.sizeTable.setVerticalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.sizeTable.setVerticalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.sizeTable.setVerticalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.sizeTable.setVerticalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.sizeTable.setVerticalHeaderItem(7, __qtablewidgetitem24)
        self.sizeTable.setObjectName(u"sizeTable")
        self.sizeTable.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)
        self.sizeTable.setAlternatingRowColors(True)
        self.sizeTable.setRowCount(8)
        self.sizeTable.setColumnCount(3)

        self.verticalLayout_5.addWidget(self.sizeTable)

        self.tabWidget.addTab(self.boneSizeTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.widget = QWidget(skeleton2CatDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.applyBtn = QPushButton(self.widget)
        self.applyBtn.setObjectName(u"applyBtn")

        self.horizontalLayout_4.addWidget(self.applyBtn)

        self.cancelBtn = QPushButton(self.widget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_4.addWidget(self.cancelBtn)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(skeleton2CatDialog)

        self.tabWidget.setCurrentIndex(0)
        self.applyBtn.setDefault(True)


        QMetaObject.connectSlotsByName(skeleton2CatDialog)
    # setupUi

    def retranslateUi(self, skeleton2CatDialog):
        skeleton2CatDialog.setWindowTitle(QCoreApplication.translate("skeleton2CatDialog", u"Skeleton to CATrig", None))
        self.saveSettingsBtn.setText(QCoreApplication.translate("skeleton2CatDialog", u"Save Settings", None))
        self.loadSettingsBtn.setText(QCoreApplication.translate("skeleton2CatDialog", u"Load Settings", None))
        self.resetSettingsBtn.setText(QCoreApplication.translate("skeleton2CatDialog", u"Reset", None))
        self.CATBoxModeDisplayChk.setText(QCoreApplication.translate("skeleton2CatDialog", u"CAT Box Display Mode", None))
        self.lengthAxisLabel.setText(QCoreApplication.translate("skeleton2CatDialog", u"Length Axis", None))
        self.taperfactorLabel.setText(QCoreApplication.translate("skeleton2CatDialog", u"Taper Factor", None))
#if QT_CONFIG(tooltip)
        self.moveBaseToCharacterChk.setToolTip(QCoreApplication.translate("skeleton2CatDialog", u"If the selected joint is not near origin this will move the Character base below the selected bone", None))
#endif // QT_CONFIG(tooltip)
        self.moveBaseToCharacterChk.setText(QCoreApplication.translate("skeleton2CatDialog", u"Move CAT Base", None))
#if QT_CONFIG(tooltip)
        self.deleteOldBonesChk.setToolTip(QCoreApplication.translate("skeleton2CatDialog", u"After the operation delete the old bones. This is not recommended if you are not transfering the Skins to the CAT as it would break any skinned meshes associated with the old bones", None))
#endif // QT_CONFIG(tooltip)
        self.deleteOldBonesChk.setText(QCoreApplication.translate("skeleton2CatDialog", u"Delete Skeleton After", None))
#if QT_CONFIG(tooltip)
        self.taperFactorsFlt.setToolTip(QCoreApplication.translate("skeleton2CatDialog", u"A Multipilier, How much smaller sub bones get as they get nested deeper into the bone chian ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.taperFactorsFlt.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lengthAxisCmb.setItemText(0, QCoreApplication.translate("skeleton2CatDialog", u"X", None))
        self.lengthAxisCmb.setItemText(1, QCoreApplication.translate("skeleton2CatDialog", u"Z", None))

#if QT_CONFIG(tooltip)
        self.attemptRepairChk.setToolTip(QCoreApplication.translate("skeleton2CatDialog", u"If your Forearm has the same name as your UpperArms", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.attemptRepairChk.setWhatsThis(QCoreApplication.translate("skeleton2CatDialog", u"If your Forearm has the same name as your UpperArms", None))
#endif // QT_CONFIG(whatsthis)
        self.attemptRepairChk.setText(QCoreApplication.translate("skeleton2CatDialog", u"Attempt fixing misnamed Limbs", None))
        self.transferSkinGroup.setTitle(QCoreApplication.translate("skeleton2CatDialog", u"Transfer Skins Settings", None))
        self.thresholdLabel.setText(QCoreApplication.translate("skeleton2CatDialog", u"Threshold", None))
#if QT_CONFIG(tooltip)
        self.skinTransferThresholdflt.setToolTip(QCoreApplication.translate("skeleton2CatDialog", u"The sensitivity of bone matching", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.skinTransferMatchByName.setToolTip(QCoreApplication.translate("skeleton2CatDialog", u"By Default this matches bones based on matching positions in case your bones have bad names", None))
#endif // QT_CONFIG(tooltip)
        self.skinTransferMatchByName.setText(QCoreApplication.translate("skeleton2CatDialog", u"Match By Name", None))
#if QT_CONFIG(tooltip)
        self.moveSkinsToCATChk.setToolTip(QCoreApplication.translate("skeleton2CatDialog", u"Any Skinned mesh associated with the bones will have their bones association moved to the CAT bones", None))
#endif // QT_CONFIG(tooltip)
        self.moveSkinsToCATChk.setText(QCoreApplication.translate("skeleton2CatDialog", u"Transfer Skins to CAT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("skeleton2CatDialog", u"Main", None))
        ___qtablewidgetitem = self.boneLabelTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("skeleton2CatDialog", u"Head", None));
        ___qtablewidgetitem1 = self.boneLabelTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("skeleton2CatDialog", u"Chest", None));
        ___qtablewidgetitem2 = self.boneLabelTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("skeleton2CatDialog", u"Neck", None));
        ___qtablewidgetitem3 = self.boneLabelTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("skeleton2CatDialog", u"Collar", None));
        ___qtablewidgetitem4 = self.boneLabelTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("skeleton2CatDialog", u"Upper Arm", None));
        ___qtablewidgetitem5 = self.boneLabelTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("skeleton2CatDialog", u"Fore Arm", None));
        ___qtablewidgetitem6 = self.boneLabelTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("skeleton2CatDialog", u"Thigh", None));
        ___qtablewidgetitem7 = self.boneLabelTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("skeleton2CatDialog", u"Calf", None));
        ___qtablewidgetitem8 = self.boneLabelTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("skeleton2CatDialog", u"Hand", None));
        ___qtablewidgetitem9 = self.boneLabelTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("skeleton2CatDialog", u"Finger", None));
        ___qtablewidgetitem10 = self.boneLabelTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("skeleton2CatDialog", u"Ankle", None));
        ___qtablewidgetitem11 = self.boneLabelTable.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("skeleton2CatDialog", u"Spine", None));
        ___qtablewidgetitem12 = self.boneLabelTable.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("skeleton2CatDialog", u"Tail", None));
        ___qtablewidgetitem13 = self.boneLabelTable.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("skeleton2CatDialog", u"Digi", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.boneLabelsTab), QCoreApplication.translate("skeleton2CatDialog", u"Bone Labels", None))
        ___qtablewidgetitem14 = self.sizeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("skeleton2CatDialog", u"Length", None));
        ___qtablewidgetitem15 = self.sizeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("skeleton2CatDialog", u"Width", None));
        ___qtablewidgetitem16 = self.sizeTable.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("skeleton2CatDialog", u"Height", None));
        ___qtablewidgetitem17 = self.sizeTable.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("skeleton2CatDialog", u"Head", None));
        ___qtablewidgetitem18 = self.sizeTable.verticalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("skeleton2CatDialog", u"Chest", None));
        ___qtablewidgetitem19 = self.sizeTable.verticalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("skeleton2CatDialog", u"Hip", None));
        ___qtablewidgetitem20 = self.sizeTable.verticalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("skeleton2CatDialog", u"Foot", None));
        ___qtablewidgetitem21 = self.sizeTable.verticalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("skeleton2CatDialog", u"Spine", None));
        ___qtablewidgetitem22 = self.sizeTable.verticalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("skeleton2CatDialog", u"Leg", None));
        ___qtablewidgetitem23 = self.sizeTable.verticalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("skeleton2CatDialog", u"Arm", None));
        ___qtablewidgetitem24 = self.sizeTable.verticalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("skeleton2CatDialog", u"Tail", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.boneSizeTab), QCoreApplication.translate("skeleton2CatDialog", u"Bone Sizes", None))
        self.applyBtn.setText(QCoreApplication.translate("skeleton2CatDialog", u"Apply", None))
        self.cancelBtn.setText(QCoreApplication.translate("skeleton2CatDialog", u"Cancel", None))
    # retranslateUi

