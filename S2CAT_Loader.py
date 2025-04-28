import sys
import os

script_dir = os.path.dirname(__file__)


sys.path.append(r'{}'.format(script_dir))
try:
    del sys.modules['Skeleton2CAT']    
except:
	pass

pysideVersion = 6
try:
	from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QDoubleSpinBox
except:
	try:
		pysideVersion = 2
		from PySide2.QtWidgets import QApplication,QDoubleSpinBox,QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
	except:
		pysideVersion = 1
		from PySide.QtGui import QApplication, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QDoubleSpinBox



if pysideVersion == 1:
	print("Loading Pyside 1\n")
	from Skeleton2CAT_maxplus import Skeleton2CAT
	from ui_Skeleton2CAT_Pyside1 import Ui_skeleton2CatDialog
else:
	from Skeleton2CAT import Skeleton2CAT
	print("Loading Pyside 4-6\n")
	from ui_Skeleton2CAT import Ui_skeleton2CatDialog



import pickle



class Skeleton2CATDialog(QWidget):   
	sk2cat = None 
	sizeSet = {}
	boneLabelSet = ()
	settingsfile = "sk2cat_pref.pickle"
	
	def __init__(self):	
		if pysideVersion != 1:		
			super().__init__()
		else:
			 super(Skeleton2CATDialog, self).__init__()  # Adjusted super() call for PySide1 compatibility
		
		
		self.ui = Ui_skeleton2CatDialog()
		self.ui.setupUi(self)

		settings_path = os.path.join(script_dir,self.settingsfile)
		
		self.sk2cat = Skeleton2CAT()
		
		if os.path.exists( settings_path ):
			print(" Skeleton to CAT: loading presets {}\n".format(settings_path))
			try:
				with open(settings_path, "rb") as file:
					self.sk2cat = pickle.load(file)
			except:
				print("Invalid Settings File. please overwrite by saving presets or resetting\n")


		#takes values from sk2cat and applies it to the UI
		self.applyValuesToUI()					

		self.ui.applyBtn.clicked.connect(self.apply)
		self.ui.saveSettingsBtn.clicked.connect(self._savePreset)
		self.ui.loadSettingsBtn.clicked.connect(self._loadPresets)
		self.ui.cancelBtn.clicked.connect(self.closeWindow)
		self.ui.resetSettingsBtn.clicked.connect(self._reset)

	
	def _savePreset(self):
		self.applyValues()		
		settings_path = os.path.join(script_dir,self.settingsfile)
		with open(settings_path, 'wb') as f:
			pickle.dump(self.sk2cat,f)	
		print("Saving Presets to {}\n".format(settings_path))
		
	def _loadPresets(self):					
		settings_path = os.path.join(script_dir,self.settingsfile)	
		if os.path.exists(settings_path):
			try:
				with open(settings_path, "rb") as file:
					self.sk2cat = pickle.load(file)
					self.applyValuesToUI()
			except:
				print("Invalid Settings File. please overwrite by saving presets or resetting\n")
			
			
			print("Loading Presets to {}\n".format(settings_path))
	
	def _reset(self):
		print("Resetting Skeleton2Cat \n")		
		#erase preset		
		settings_path = os.path.join(script_dir,self.settingsfile)	
		if os.path.exists(settings_path):
			os.remove(settings_path)
		
		othersk = Skeleton2CAT()	
		self.sk2cat = Skeleton2CAT()				
		
		self.applyValuesToUI()
		
	

	def applyValuesToUI(self):
		self.ui.taperFactorsFlt.setValue(self.sk2cat.taperFactors)
		self.ui.moveBaseToCharacterChk.setChecked( self.sk2cat.moveBaseToCharacter )
		self.ui.deleteOldBonesChk.setChecked( self.sk2cat.deleteOldBones )
		self.ui.CATBoxModeDisplayChk.setChecked( self.sk2cat.CATBoxModeDisplay )
		self.ui.moveSkinsToCATChk.setChecked( self.sk2cat.moveSkinsToCAT)
		self.ui.skinTransferMatchByName.setChecked( self.sk2cat.skinTransferMatchByName)
		self.ui.attemptRepairChk.setChecked( self.sk2cat.attemptFixMisnamedBones)
		self.ui.skinTransferThresholdflt.setValue( self.sk2cat.skinTransferThreshold )

		if pysideVersion == 1:
			index = self.ui.lengthAxisCmb.findText(self.sk2cat.lengthAxis)
			if index != -1:
				self.ui.lengthAxisCmb.setCurrentIndex(index)
		else:
			self.ui.lengthAxisCmb.setCurrentText( self.sk2cat.lengthAxis )
		

		self.ui.sizeTable.clearContents()
		for row in range(self.ui.sizeTable.rowCount()):
			for col in range(self.ui.sizeTable.columnCount()):
				spinbox = QDoubleSpinBox()
				spinbox.setDecimals(2) # Set decimal places
				spinbox.setMinimum(0.1) # Set min value
				spinbox.setMaximum(1000) # Set max value
				self.ui.sizeTable.setCellWidget(row, col, spinbox)
				
		self.sizeSet = {}
		self.sizeSet["Head"] = self.sk2cat.headSizes
		self.sizeSet["Chest"] = self.sk2cat.chestSizes
		self.sizeSet["Hip"] = self.sk2cat.hipSizes
		self.sizeSet["Foot"] = self.sk2cat.footSizes
		self.sizeSet["Spine"] = self.sk2cat.spineSizes
		self.sizeSet["Leg"] = self.sk2cat.legSizes
		self.sizeSet["Arm"] = self.sk2cat.armSizes
		self.sizeSet["Tail"] = self.sk2cat.tailSizes

		self.ui.boneLabelTable.clearContents()
		for row in range(len(self.sizeSet)):
			headername = self.ui.sizeTable.verticalHeaderItem(row).text()			
			for col in range(3):				
				values = self.sizeSet[headername]				
				self.ui.sizeTable.cellWidget(row,col).setValue( values[col])

		for col in range(self.ui.boneLabelTable.columnCount()):
			columnName = self.ui.boneLabelTable.horizontalHeaderItem(col).text()			
			if columnName == "Head":				
				for i in range(len(self.sk2cat.headNames)):
					item = QTableWidgetItem( self.sk2cat.headNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)
			if columnName == "Chest":				
				for i in range(len(self.sk2cat.chestNames)):
					item = QTableWidgetItem( self.sk2cat.chestNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)
			if columnName == "Collar":				
				for i in range(len(self.sk2cat.collarNames)):
					item = QTableWidgetItem( self.sk2cat.collarNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)
			if columnName == "Upper Arm":				
				for i in range(len(self.sk2cat.upperarmNames)):
					item = QTableWidgetItem( self.sk2cat.upperarmNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)
			if columnName == "Fore Arm":				
				for i in range(len(self.sk2cat.forearmNames)):
					item = QTableWidgetItem( self.sk2cat.forearmNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)
			if columnName == "Thigh":				
				for i in range(len(self.sk2cat.thighNames)):
					item = QTableWidgetItem( self.sk2cat.thighNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)	
			if columnName == "Calf":				
				for i in range(len(self.sk2cat.calfNames)):
					item = QTableWidgetItem( self.sk2cat.calfNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)	
			if columnName == "Hand":				
				for i in range(len(self.sk2cat.handNames)):
					item = QTableWidgetItem( self.sk2cat.handNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)						
			if columnName == "Finger":				
				for i in range(len(self.sk2cat.fingerNames)):
					item = QTableWidgetItem( self.sk2cat.fingerNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)						
			if columnName == "Ankle":				
				for i in range(len(self.sk2cat.ankleNames)):
					item = QTableWidgetItem( self.sk2cat.ankleNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)						
			if columnName == "Spine":				
				for i in range(len(self.sk2cat.spineNames)):
					item = QTableWidgetItem( self.sk2cat.spineNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)	
			if columnName == "Tail":
				for i in range(len(self.sk2cat.tailNames)):
					item = QTableWidgetItem( self.sk2cat.tailNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)					
			if columnName == "Neck":
				for i in range(len(self.sk2cat.neckNames)):
					item = QTableWidgetItem( self.sk2cat.neckNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)		
			if columnName == "Digi":
				for i in range(len(self.sk2cat.digiLegNames)):
					item = QTableWidgetItem( self.sk2cat.digiLegNames[i] )
					self.ui.boneLabelTable.setItem(i,col,item)		
				

	def getTableRow(self, qtTable, headerName):
		values = []
		for col in range(qtTable.columnCount()):
			columnName = qtTable.horizontalHeaderItem(col).text()			
			if columnName == headerName:
				maxrows = qtTable.rowCount()
				for r in range(maxrows):
					item = qtTable.item(r,col)
					if item:
						text = item.text().strip()
						if text != "":
							values.append(text)
		return values

	def closeWindow(self, *args):
		print("Good Bye")
		self.close()

	
	def applyValues(self):
		self.sk2cat.taperFactors = 	self.ui.taperFactorsFlt.value()		
		self.sk2cat.moveBaseToCharacter = self.ui.moveBaseToCharacterChk.isChecked()
		self.sk2cat.deleteOldBones = self.ui.deleteOldBonesChk.isChecked()
		self.sk2cat.CATBoxModeDisplay = self.ui.CATBoxModeDisplayChk.isChecked()
		self.sk2cat.moveSkinsToCAT = self.ui.moveSkinsToCATChk.isChecked()
		self.sk2cat.attemptFixMisnamedBones = self.ui.attemptRepairChk.isChecked()
		self.sk2cat.skinTransferThreshold = self.ui.skinTransferThresholdflt.value()		
		self.sk2cat.lengthAxis = self.ui.lengthAxisCmb.currentText()

		for row in range(len(self.sizeSet)):
			headername = self.ui.sizeTable.verticalHeaderItem(row).text()	
			for col in range(3):
				if headername == "Head": #head
					self.sk2cat.headSizes[col] = self.ui.sizeTable.cellWidget(row,col).value()					
				if headername == "Chest":
					self.sk2cat.chestSizes[col] = self.ui.sizeTable.cellWidget(row,col).value()
				if headername == "Hip":
					self.sk2cat.hipSizes[col] = self.ui.sizeTable.cellWidget(row,col).value()
				if headername == "Foot":
					self.sk2cat.footSizes[col] = self.ui.sizeTable.cellWidget(row,col).value()	
				if headername == "Spine":
					self.sk2cat.spineSizes[col] = self.ui.sizeTable.cellWidget(row,col).value()	
				if headername == "Leg":
					self.sk2cat.legSizes[col] = self.ui.sizeTable.cellWidget(row,col).value()	
				if headername == "Arm":
					self.sk2cat.armSizes[col] = self.ui.sizeTable.cellWidget(row,col).value()	
				if headername == "Tail":	
					self.sk2cat.tailSizes[col] = self.ui.sizeTable.cellWidget(row,col).value()	
			
		for col in range(self.ui.boneLabelTable.columnCount()):
			columnName = self.ui.boneLabelTable.horizontalHeaderItem(col).text()			
			if columnName == "Head":					
				self.sk2cat.headNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Chest":				
				self.sk2cat.chestNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Collar":				
				self.sk2cat.collarNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Upper Arm":				
				self.sk2cat.upperarmNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Fore Arm":				
				self.sk2cat.forearmNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Thigh":				
				self.sk2cat.thighNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Calf":				
				self.sk2cat.calfNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Hand":				
				self.sk2cat.handNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Finger":				
				self.sk2cat.fingerNames = self.getTableRow(self.ui.boneLabelTable,columnName)					
			if columnName == "Ankle":				
				self.sk2cat.ankleNames = self.getTableRow(self.ui.boneLabelTable,columnName)							
			if columnName == "Spine":				
				self.sk2cat.spineNames = self.getTableRow(self.ui.boneLabelTable,columnName)
			if columnName == "Tail":
				self.sk2cat.tailNames =  self.getTableRow(self.ui.boneLabelTable,columnName)
			if columnName == "Neck":
				self.sk2cat.neckNames =  self.getTableRow(self.ui.boneLabelTable,columnName)
			if columnName == "Digi":
				self.sk2cat.digiLegNames =  self.getTableRow(self.ui.boneLabelTable,columnName)

	def apply(self,*args):							
		self.applyValues()
		self.sk2cat.create_CAT_from_Bones()
		
      
my_dialog = Skeleton2CATDialog()
my_dialog.show()