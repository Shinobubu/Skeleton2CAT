# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Skeleton2CATcXTPvb.ui'
##
## Created by: Qt User Interface Compiler (adapted for PySide 1)
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide.QtCore import (QMetaObject, QRect, QSize, Qt)
from PySide.QtGui import (QApplication, QCheckBox, QComboBox, QDialog,
						  QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout,
						  QLabel, QLayout, QPushButton, QSizePolicy, QSpacerItem,
						  QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
						  QVBoxLayout, QWidget)

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
		self.taperfactorLabel = QLabel(self.formLayoutWidget)
		self.taperfactorLabel.setObjectName(u"taperfactorLabel")
		sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.taperfactorLabel.sizePolicy().hasHeightForWidth())
		self.taperfactorLabel.setSizePolicy(sizePolicy2)
		self.taperfactorLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

		self.gridLayout_3.addWidget(self.taperfactorLabel, 0, 0, 1, 1)

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
		self.taperFactorsFlt.setMaximum(1.0)
		self.taperFactorsFlt.setSingleStep(0.01)
		self.taperFactorsFlt.setValue(0.25)

		self.gridLayout_3.addWidget(self.taperFactorsFlt, 0, 1, 1, 1)

		self.moveBaseToCharacterChk = QCheckBox(self.formLayoutWidget)
		self.moveBaseToCharacterChk.setObjectName(u"moveBaseToCharacterChk")

		self.gridLayout_3.addWidget(self.moveBaseToCharacterChk, 1, 0, 1, 1)

		self.CATBoxModeDisplayChk = QCheckBox(self.formLayoutWidget)
		self.CATBoxModeDisplayChk.setObjectName(u"CATBoxModeDisplayChk")

		self.gridLayout_3.addWidget(self.CATBoxModeDisplayChk, 3, 0, 1, 1)

		self.lengthAxisLabel = QLabel(self.formLayoutWidget)
		self.lengthAxisLabel.setObjectName(u"lengthAxisLabel")
		sizePolicy2.setHeightForWidth(self.lengthAxisLabel.sizePolicy().hasHeightForWidth())
		self.lengthAxisLabel.setSizePolicy(sizePolicy2)
		self.lengthAxisLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

		self.gridLayout_3.addWidget(self.lengthAxisLabel, 4, 0, 1, 1)

		self.lengthAxisCmb = QComboBox(self.formLayoutWidget)
		self.lengthAxisCmb.addItem("")
		self.lengthAxisCmb.addItem("")
		self.lengthAxisCmb.setObjectName(u"lengthAxisCmb")

		self.gridLayout_3.addWidget(self.lengthAxisCmb, 4, 1, 1, 1)

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
		self.thresholdLabel.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

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
		self.boneLabelTable.setColumnCount(13)
		self.boneLabelTable.setHorizontalHeaderItem(0, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(1, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(2, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(3, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(4, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(5, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(6, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(7, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(8, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(9, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(10, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(11, QTableWidgetItem())
		self.boneLabelTable.setHorizontalHeaderItem(12, QTableWidgetItem())
		self.boneLabelTable.setRowCount(50)
		self.boneLabelTable.setObjectName(u"boneLabelTable")
		sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
		sizePolicy4.setHorizontalStretch(1)
		sizePolicy4.setVerticalStretch(1)
		sizePolicy4.setHeightForWidth(self.boneLabelTable.sizePolicy().hasHeightForWidth())
		self.boneLabelTable.setSizePolicy(sizePolicy4)
		self.boneLabelTable.setAlternatingRowColors(True)
		self.boneLabelTable.setSortingEnabled(True)

		self.verticalLayout_3.addWidget(self.boneLabelTable)

		self.horizontalLayout_3.addLayout(self.verticalLayout_3)

		self.tabWidget.addTab(self.boneLabelsTab, "")
		self.boneSizeTab = QWidget()
		self.boneSizeTab.setObjectName(u"boneSizeTab")
		self.verticalLayout_5 = QVBoxLayout(self.boneSizeTab)
		self.verticalLayout_5.setObjectName(u"verticalLayout_5")
		self.sizeTable = QTableWidget(self.boneSizeTab)
		self.sizeTable.setColumnCount(3)
		self.sizeTable.setHorizontalHeaderItem(0, QTableWidgetItem())
		self.sizeTable.setHorizontalHeaderItem(1, QTableWidgetItem())
		self.sizeTable.setHorizontalHeaderItem(2, QTableWidgetItem())
		self.sizeTable.setRowCount(8)
		self.sizeTable.setVerticalHeaderItem(0, QTableWidgetItem())
		self.sizeTable.setVerticalHeaderItem(1, QTableWidgetItem())
		self.sizeTable.setVerticalHeaderItem(2, QTableWidgetItem())
		self.sizeTable.setVerticalHeaderItem(3, QTableWidgetItem())
		self.sizeTable.setVerticalHeaderItem(4, QTableWidgetItem())
		self.sizeTable.setVerticalHeaderItem(5, QTableWidgetItem())
		self.sizeTable.setVerticalHeaderItem(6, QTableWidgetItem())
		self.sizeTable.setVerticalHeaderItem(7, QTableWidgetItem())
		self.sizeTable.setObjectName(u"sizeTable")
		self.sizeTable.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
		self.sizeTable.setAlternatingRowColors(True)

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

		self.englishUi(skeleton2CatDialog)

		self.tabWidget.setCurrentIndex(0)
		self.applyBtn.setDefault(True)

		QMetaObject.connectSlotsByName(skeleton2CatDialog)
	
	# setupUi
	def englishUi(self, skeleton2CatDialog):
		#force english mode		
		skeleton2CatDialog.setWindowTitle(u"Skeleton to CATrig")
		self.saveSettingsBtn.setText(u"Save Settings")
		self.loadSettingsBtn.setText(u"Load Settings")
		self.resetSettingsBtn.setText(u"Reset")
		self.taperfactorLabel.setText(u"Taper Factor")
		self.deleteOldBonesChk.setText(u"Delete Skeleton After")
		self.moveBaseToCharacterChk.setText(u"Move CAT Base")
		self.CATBoxModeDisplayChk.setText(u"CAT Box Display Mode")
		self.lengthAxisLabel.setText(u"Length Axis")
		self.lengthAxisCmb.setItemText(0, u"X")
		self.lengthAxisCmb.setItemText(1, u"Z")
		self.transferSkinGroup.setTitle(u"Transfer Skins Settings")
		self.thresholdLabel.setText(u"Threshold")
		self.skinTransferMatchByName.setText(u"Match By Name")
		self.moveSkinsToCATChk.setText(u"Transfer Skins to CAT")
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), u"Main")
		self.boneLabelTable.horizontalHeaderItem(0).setText(u"Head")
		self.boneLabelTable.horizontalHeaderItem(1).setText(u"Chest")
		self.boneLabelTable.horizontalHeaderItem(2).setText(u"Neck")
		self.boneLabelTable.horizontalHeaderItem(3).setText(u"Collar")
		self.boneLabelTable.horizontalHeaderItem(4).setText(u"Upper Arm")
		self.boneLabelTable.horizontalHeaderItem(5).setText(u"Fore Arm")
		self.boneLabelTable.horizontalHeaderItem(6).setText(u"Thigh")
		self.boneLabelTable.horizontalHeaderItem(7).setText(u"Calf")
		self.boneLabelTable.horizontalHeaderItem(8).setText(u"Hand")
		self.boneLabelTable.horizontalHeaderItem(9).setText(u"Finger")
		self.boneLabelTable.horizontalHeaderItem(10).setText(u"Ankle")
		self.boneLabelTable.horizontalHeaderItem(11).setText(u"Spine")
		self.boneLabelTable.horizontalHeaderItem(12).setText(u"Tail")
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.boneLabelsTab), u"Bone Labels")
		self.sizeTable.horizontalHeaderItem(0).setText(u"Length")
		self.sizeTable.horizontalHeaderItem(1).setText(u"Width")
		self.sizeTable.horizontalHeaderItem(2).setText(u"Height")
		self.sizeTable.verticalHeaderItem(0).setText(u"Head")
		self.sizeTable.verticalHeaderItem(1).setText(u"Chest")
		self.sizeTable.verticalHeaderItem(2).setText(u"Hip")
		self.sizeTable.verticalHeaderItem(3).setText(u"Foot")
		self.sizeTable.verticalHeaderItem(4).setText(u"Spine")
		self.sizeTable.verticalHeaderItem(5).setText(u"Leg")
		self.sizeTable.verticalHeaderItem(6).setText(u"Arm")
		self.sizeTable.verticalHeaderItem(7).setText(u"Tail")
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.boneSizeTab), u"Bone Sizes")
		self.applyBtn.setText(u"Apply")
		self.cancelBtn.setText(u"Cancel")
	
	def retranslateUi(self, skeleton2CatDialog):
		skeleton2CatDialog.setWindowTitle(QApplication.translate("skeleton2CatDialog", u"Skeleton to CATrig", None))
		self.saveSettingsBtn.setText(QApplication.translate("skeleton2CatDialog", u"Save Settings", None))
		self.loadSettingsBtn.setText(QApplication.translate("skeleton2CatDialog", u"Load Settings", None))
		self.resetSettingsBtn.setText(QApplication.translate("skeleton2CatDialog", u"Reset", None))
		self.taperfactorLabel.setText(QApplication.translate("skeleton2CatDialog", u"Taper Factor", None))
		self.deleteOldBonesChk.setText(QApplication.translate("skeleton2CatDialog", u"Delete Skeleton After", None))
		self.moveBaseToCharacterChk.setText(QApplication.translate("skeleton2CatDialog", u"Move CAT Base", None))
		self.CATBoxModeDisplayChk.setText(QApplication.translate("skeleton2CatDialog", u"CAT Box Display Mode", None))
		self.lengthAxisLabel.setText(QApplication.translate("skeleton2CatDialog", u"Length Axis", None))
		self.lengthAxisCmb.setItemText(0, QApplication.translate("skeleton2CatDialog", u"X", None))
		self.lengthAxisCmb.setItemText(1, QApplication.translate("skeleton2CatDialog", u"Z", None))

		self.transferSkinGroup.setTitle(QApplication.translate("skeleton2CatDialog", u"Transfer Skins Settings", None))
		self.thresholdLabel.setText(QApplication.translate("skeleton2CatDialog", u"Threshold", None))
		self.skinTransferMatchByName.setText(QApplication.translate("skeleton2CatDialog", u"Match By Name", None))
		self.moveSkinsToCATChk.setText(QApplication.translate("skeleton2CatDialog", u"Transfer Skins to CAT", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QApplication.translate("skeleton2CatDialog", u"Main", None))
		self.boneLabelTable.horizontalHeaderItem(0).setText(QApplication.translate("skeleton2CatDialog", u"Head", None))
		self.boneLabelTable.horizontalHeaderItem(1).setText(QApplication.translate("skeleton2CatDialog", u"Chest", None))
		self.boneLabelTable.horizontalHeaderItem(2).setText(QApplication.translate("skeleton2CatDialog", u"Neck", None))
		self.boneLabelTable.horizontalHeaderItem(3).setText(QApplication.translate("skeleton2CatDialog", u"Collar", None))
		self.boneLabelTable.horizontalHeaderItem(4).setText(QApplication.translate("skeleton2CatDialog", u"Upper Arm", None))
		self.boneLabelTable.horizontalHeaderItem(5).setText(QApplication.translate("skeleton2CatDialog", u"Fore Arm", None))
		self.boneLabelTable.horizontalHeaderItem(6).setText(QApplication.translate("skeleton2CatDialog", u"Thigh", None))
		self.boneLabelTable.horizontalHeaderItem(7).setText(QApplication.translate("skeleton2CatDialog", u"Calf", None))
		self.boneLabelTable.horizontalHeaderItem(8).setText(QApplication.translate("skeleton2CatDialog", u"Hand", None))
		self.boneLabelTable.horizontalHeaderItem(9).setText(QApplication.translate("skeleton2CatDialog", u"Finger", None))
		self.boneLabelTable.horizontalHeaderItem(10).setText(QApplication.translate("skeleton2CatDialog", u"Ankle", None))
		self.boneLabelTable.horizontalHeaderItem(11).setText(QApplication.translate("skeleton2CatDialog", u"Spine", None))
		self.boneLabelTable.horizontalHeaderItem(12).setText(QApplication.translate("skeleton2CatDialog", u"Tail", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.boneLabelsTab), QApplication.translate("skeleton2CatDialog", u"Bone Labels", None))
		self.sizeTable.horizontalHeaderItem(0).setText(QApplication.translate("skeleton2CatDialog", u"Length", None))
		self.sizeTable.horizontalHeaderItem(1).setText(QApplication.translate("skeleton2CatDialog", u"Width", None))
		self.sizeTable.horizontalHeaderItem(2).setText(QApplication.translate("skeleton2CatDialog", u"Height", None))
		self.sizeTable.verticalHeaderItem(0).setText(QApplication.translate("skeleton2CatDialog", u"Head", None))
		self.sizeTable.verticalHeaderItem(1).setText(QApplication.translate("skeleton2CatDialog", u"Chest", None))
		self.sizeTable.verticalHeaderItem(2).setText(QApplication.translate("skeleton2CatDialog", u"Hip", None))
		self.sizeTable.verticalHeaderItem(3).setText(QApplication.translate("skeleton2CatDialog", u"Foot", None))
		self.sizeTable.verticalHeaderItem(4).setText(QApplication.translate("skeleton2CatDialog", u"Spine", None))
		self.sizeTable.verticalHeaderItem(5).setText(QApplication.translate("skeleton2CatDialog", u"Leg", None))
		self.sizeTable.verticalHeaderItem(6).setText(QApplication.translate("skeleton2CatDialog", u"Arm", None))
		self.sizeTable.verticalHeaderItem(7).setText(QApplication.translate("skeleton2CatDialog", u"Tail", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.boneSizeTab), QApplication.translate("skeleton2CatDialog", u"Bone Sizes", None))
		self.applyBtn.setText(QApplication.translate("skeleton2CatDialog", u"Apply", None))
		self.cancelBtn.setText(QApplication.translate("skeleton2CatDialog", u"Cancel", None))
	# retranslateUi