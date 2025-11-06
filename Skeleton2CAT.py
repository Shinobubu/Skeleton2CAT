"""
Shinobu's Skeleton to CAT Script for Onirism
v1.0
Tested on 3dsmax 2026
"""

import pymxs
import math

from pymxs import runtime as rt

class Skeleton2CAT:
				
	def __init__(self):		
		# Names have to be LOWER CASE
		self.headNames = ["head","hub"]
		self.chestNames = ["ribcage","chest","hub","pelvis","root"]
		self.collarNames = ["scapula","collar"]
		self.upperarmNames = ["upperarm","bicep","arm"]
		self.forearmNames = ["forearm",]
		self.thighNames = ["thigh","femur","humerus"]
		self.calfNames = ["calf","tibia","radius"]
		self.digiLegNames = ["cannon","metacarpus"]
		self.handNames = ["palm","hand"]
		self.fingerNames = ["digit","hoof","finger","thumb","index","middle","ring","hallux"]
		self.ankleNames = ["ankle","feet","foot","manus","prima"]
		self.spineNames = ["spine"]
		self.tailNames = ["tail","tentacle","tendril","ribbon","bun"]
		self.neckNames = ["neck"]
		self.taperFactors = 0.25
		self.hipSizes = [3,10,5]
		self.legSizes = [5,5,5]
		self.footSizes = [10,5,2]
		self.chestSizes = [5,20,5]
		self.headSizes = [10,10,12]
		self.spineSizes = [5,5,5]
		self.armSizes = [3,3,3]
		self.tailSizes = [3,3,3]
		self.skinnedObjects = []
		self.moveBaseToCharacter = True
		self.moveSkinsToCAT = True
		self.deleteOldBones = True
		self.CATBoxModeDisplay = True
		self.lengthAxis = "X" # "X" "Z"
		self.delayedRename = []
		self.CATName = "" # leave blank to preserve tail names
	
		self.flatBoneList = []
		self.flatCATBones = []
		self.flatPlatformsIKs = []
		self.positionDistanceMatch = 0.0001	
		self.skinTransferThreshold = 1
		self.skinTransferMatchByName = False
		self.platformRotation = None
		self.attemptFixMisnamedBones = True

	def createTempTransform(self,sourceBone,targetBone):		
		# There is no way EASY WAY to just move a position that is connected to a controller
		targetBone.transform = sourceBone.transform	
	
		return True
		

	def maxHierarchyDepth(self,parentObject,depth=0):
		result = depth				
		for c in parentObject.Children:	
			childrenLen = len(c.Children) 					
			if childrenLen > 0:
				rs = self.maxHierarchyDepth(c,depth+1) 
				if rs > result:
					result = rs
		return result

	def inArrayStrings(self,listhaystack,needleString):
		for i in listhaystack:
			if i.lower() in needleString.lower():
				return True
		return False
	# Use this to find Digits and segments
	def getSegmentJoints(self,parentObject,segmentNames,endTipNames):
		result = []		
		if self.inArrayStrings(segmentNames, parentObject.name) or len(segmentNames) == 0:
			# is a spine
			result.append(parentObject)
			childrenLen = len(parentObject.Children) 
			if childrenLen > 0 :
				for c in parentObject.Children:					
					if self.inArrayStrings(segmentNames,c.name):
						result += self.getSegmentJoints(c,segmentNames,endTipNames) 
					elif (len(endTipNames) == 0 and len(segmentNames) == 0):						
						#result.append( c )
						result += self.getSegmentJoints(c,segmentNames,endTipNames) 
					elif (self.inArrayStrings(endTipNames,c.name) and len(endTipNames) > 0):
						# if end joint is a ribcage or a head.						
						result.append( c )
						# end point	
		return result
	
	def createPoint(self,p1,p2,p3):
		rt.point3(p1,p2,p3)

	
		
	def boneDistanceFromBone(self,boneA,boneB):
		startPos = boneA.position
		endPos = boneB.position
		p1 = rt.point3(startPos[0],startPos[1],startPos[2])	
		p2 = rt.point3(endPos[0],endPos[1],endPos[2])
		return rt.distance(p1,p2)

	def boneLength(self,bone,defaultlength=5):
		if len(bone.Children) == 0: 
			return defaultlength
		boneB = bone.Children[0]
		try:
			startPos = bone.position
			endPos = boneB.position
		except:
			startPos = bone.transform.position
			endPos = boneB.transform.position
		p1 = rt.point3(startPos[0],startPos[1],startPos[2])	
		p2 = rt.point3(endPos[0],endPos[1],endPos[2])
		result = rt.distance(p1,p2)
		if result <= 0.01:
			result = defaultlength

		return result
	
	def boneLengthFromMatrix(self,bone,boneDictionary):
		''' Uses a set to find the child'''		
		if len(bone.Children) == 0: 					
			return -1		
		try:
			#idname = id(bone.Children[0].transform)			
			boneB = boneDictionary[ bone.Children[0].name ] 
			boneA = boneDictionary[ bone.name ] 									
		except:
			return -1
			
		try:
			startPos = boneA.position
			endPos = boneB.position
		except:
			startPos = boneA.transform.position
			endPos = boneB.transform.position

		p1 = rt.point3(startPos[0],startPos[1],startPos[2])	
		p2 = rt.point3(endPos[0],endPos[1],endPos[2])
		result = rt.distance(p1,p2)
		if result <= 0.01:
			result = -1 # has no parent or too small

		return result

	def findKeyword(self,needle,haystacksArray):
		for h in haystacksArray:
			if h.lower() in needle.lower():			
				return h
		return ""
	
	# this may be redundant to the LegJoints parser but just making sure
	def getArmJoints(self,parentObject):
		collarbones = None
		upperarms = []
		forearms = []
		hand = None
		handDigits = []
		flathierarchy = self.getSegmentJoints(parentObject,[],[])
		flatDigits = []
		flathierarchyFiltered = []
		for l in range(len(flathierarchy)):
			c = flathierarchy[l]
			cname = c.name.lower()
			collarbonesName = self.findKeyword(c.name.lower(),self.collarNames)
			upperarmsName = self.findKeyword(c.name.lower(),self.upperarmNames)
			forarmName =  self.findKeyword(c.name.lower(),self.forearmNames)			
			handName = self.findKeyword(c.name.lower(), self.handNames)
			digitName = self.findKeyword(c.name.lower(),self.fingerNames)						
			if l == 0:
				
				if upperarmsName == "" or collarbonesName != "":
					# Collar
					collarbones = c
					flathierarchyFiltered.append(c)
				elif upperarmsName != "":
					upperarms.append(c)	
					flathierarchyFiltered.append(c)
			else:
				#prioritize hand detection incase someone used armHand as a name
				if handName != "" and hand == None:
					hand = c
					flathierarchyFiltered.append(c)				
				elif digitName != "":					
					flatDigits.append(c)
					flathierarchyFiltered.append(c)
				elif upperarmsName != "":
					upperarms.append(c)
					flathierarchyFiltered.append(c)
				elif forarmName != "":
					forearms.append(c)
					flathierarchyFiltered.append(c)				
				
		
		if hand != None:
			numDigits = len(hand.Children)
			if numDigits > 0:
				for f in hand.Children:
					digitName = self.findKeyword(f.name.lower(),self.fingerNames)	
					if digitName != "":			
						digitArray = self.getSegmentJoints(f,[digitName],[])
						handDigits.append(digitArray)
						flathierarchyFiltered += digitArray
						
		return collarbones,upperarms,forearms,hand,handDigits,flathierarchyFiltered
	
	# Reconstructs leg joints and its members
	def getLegJoints(self,parentObject):
		collarbones = None
		thighs = []
		calfs = []
		foot = None
		footDigits = []
		digiLegs = []
		flathierarchy = self.getSegmentJoints(parentObject,[],[])
		flatDigits = []
		flathierarchyFiltered = []
		for l in range(len(flathierarchy)):
			c = flathierarchy[l]
			collarbonesName = self.findKeyword(c.name.lower(),self.collarNames)
			thighName = self.findKeyword(c.name.lower(),self.thighNames)
			calfName =  self.findKeyword(c.name.lower(),self.calfNames)
			ankleName = self.findKeyword(c.name.lower(), self.ankleNames)
			digitName = self.findKeyword(c.name.lower(),self.fingerNames)
			digilegName = self.findKeyword(c.name.lower(),self.digiLegNames) 
			if l == 0:
				
				if thighName == "" or collarbonesName != "":
					# Collar
					collarbones = c
					flathierarchyFiltered.append(c)
				elif thighName != "":
					thighs.append(c)	
					flathierarchyFiltered.append(c)
			else:
				if ankleName != "" and foot == None:
					foot = c
					flathierarchyFiltered.append(c)
				elif digitName != "":					
					flatDigits.append(c)
					flathierarchyFiltered.append(c)
				elif digilegName != "":
					digiLegs.append(c)
					flathierarchyFiltered.append(c)
				elif thighName != "":
					thighs.append(c)
					flathierarchyFiltered.append(c)
				elif calfName != "":
					calfs.append(c)
					flathierarchyFiltered.append(c)
																					
		if foot != None:
			numDigits = len(foot.Children)
			if numDigits > 0:
				for f in foot.Children:
					digitName = self.findKeyword(f.name.lower(),self.fingerNames)	
					if digitName != "":			
						digitArray = self.getSegmentJoints(f,[digitName],[])
						footDigits.append(digitArray)
						flathierarchyFiltered += digitArray
						
		return collarbones,thighs,calfs,digiLegs,foot,footDigits,flathierarchyFiltered

	def childHasLegs(self,parentObject):
		for c in parentObject.Children:
			thighName = self.findKeyword(c.name.lower(),self.thighNames)
			if thighName != "":
				return thighName
		return ""
	
	def childHasArms(self,parentObject):
		for c in parentObject.Children:
			thighName = self.findKeyword(c.name.lower(),self.upperarmNames)
			if thighName != "":
				return thighName
		return ""

	def quaternion_equal(self,q1, q2, tolerance=1e-6):
		for id,val in enumerate(q1):
			if not math.isclose(q1[id], q2[id], abs_tol=tolerance):
				return False
		return True
	
	def isTransformTheSame(self,A,B):
		posDistance = rt.distance(A.position,B.position)
		scaleDistance = rt.distance(A.scale,B.scale)		
		quatTolerance = self.quaternion_equal( A.rotation , B.rotation )				
		return (posDistance < self.positionDistanceMatch) and (scaleDistance < self.positionDistanceMatch) and quatTolerance
	
	def isBoneTheSame(self,nodeA,nodeB):
		return self.isTransformTheSame(nodeA.transform,nodeB.transform)		
		

	def parseLegJoints(self,legCAT,parentCAT,c,exclude,maxDepth,depth):
		collarbones,thighs,calfs,digis,foot,footDigits,bones = self.getLegJoints(c)				
		numThighSegments = len(thighs)
		numCalfSegments = len(calfs)
		numDigiSegments = len(digis)
		numDigits = len(footDigits)
		hasDigis = False
		hasAnkles = False
		hasCollar = False
		hasKnees = False
		digiCAT = None
		collarCAT = None 
		footCAT = None
		
		selfbones = [collarbones]+thighs+calfs+digis+[foot]

		for fd in footDigits:
			selfbones += fd

		# Check for DigiLegs incase its animal

		if foot != None:
			hasAnkles = True
		if collarbones != None:
			hasCollar = True
		
		if numDigiSegments > 0:
			hasDigis = True
		
		if numCalfSegments > 0:
			hasKnees = True
		else:
			hasKnees = False
			if numThighSegments > 1 and self.attemptFixMisnamedBones:
				#possible misnamed leg joints
				calfs.append( thighs.pop() )
				numThighSegments = len(thighs)
				numCalfSegments = len(calfs)
				hasKnees = True

		#parentCAT.AddLeg(AddCollarbone=hasCollar,AddAnkle=hasAnkles)					
		#legCAT = parentCAT.limbs[-1]

		if hasAnkles == True:
			legCAT.CreatePalmAnkle()
		if hasAnkles == False:
			legCAT.RemovePalmAnkle()

		if hasCollar == True:
			legCAT.CreateCollarbone()
		if hasCollar == False:
			legCAT.RemoveCollarbone()
		if hasDigis == True:
			legCAT.NumBones = 3
			
		

		# disable IK/FK to allow leg to reposition
		#legCAT.removeIKTarget()
		legCAT.layerIKFKRatio = 1.0	
		RepeatPosition=[]
		
		
		
		if hasAnkles:			
			footCAT = legCAT.Palm
			footCAT.node.controller.numDigits = numDigits			

		thighCAT = legCAT.bones[0]
		thighCAT.numSegs = numThighSegments

		if hasKnees:
			calfCAT = legCAT.bones[1]
			calfCAT.numSegs = numCalfSegments
			calfCAT.width = self.legSizes[1]
			calfCAT.depth = self.legSizes[2]			

		if hasDigis:
			digiCAT = legCAT.bones[2]
			digiCAT.numSegs = numDigiSegments
			digiCAT.width = self.legSizes[1]
			digiCAT.depth = self.legSizes[2]
			
		
		if hasCollar:
			collarCAT = legCAT.collarbone
			collarCAT.node.length = self.boneLength(collarbones)
			RepeatPosition.append([collarbones,collarCAT.node])
			self.addFlatBones(collarbones,collarCAT)
			self.createTempTransform(collarbones,collarCAT.node)						
			collarnodesthesame = collarCAT.node.Controller == collarCAT			
			self.parseHierarchy(collarbones,parentCAT,exclude+selfbones,maxDepth,depth+1)


		legCAT.name = "" # Blank out to preserve names
		
		
		
		if numCalfSegments > 0:
			if hasKnees:
				thighCAT.length = self.boneDistanceFromBone(thighs[0],calfs[0])
			elif hasAnkles:
				thighCAT.length = self.boneDistanceFromBone(thighs[0],foot)
			else:
				thighCAT.length = self.legSizes[0]

			if numDigiSegments > 0:
				if hasKnees:
					calfCAT.length = self.boneDistanceFromBone(calfs[0],digis[0])
				if hasAnkles:
					digiCAT.length = self.boneDistanceFromBone(digis[0],foot)
			elif hasAnkles:
				if hasKnees:
					calfCAT.length = self.boneDistanceFromBone(calfs[0],foot)

		for se in range(numThighSegments):						
			thighCAT.boneSegs[se].node.name = thighs[se].name						
			self.addFlatBones(thighs[se],thighCAT.boneSegs[se])			
			self.createTempTransform(thighs[se],thighCAT.boneSegs[se].node )
			RepeatPosition.append([thighs[se],thighCAT.boneSegs[se].node ])
			self.parseHierarchy(thighs[se],thighCAT.boneSegs[se],exclude+selfbones,maxDepth,depth+1)			
			
									
		for se in range(numCalfSegments):						
			calfCAT.boneSegs[se].node.name = calfs[se].name
			self.addFlatBones(calfs[se],calfCAT.boneSegs[se])			
			self.createTempTransform(calfs[se],calfCAT.boneSegs[se].node )
			RepeatPosition.append([calfs[se],calfCAT.boneSegs[se].node])
			self.parseHierarchy(calfs[se],calfCAT.boneSegs[se],exclude+selfbones,maxDepth,depth+1)

		for se in range(numDigiSegments):
			digiCAT.boneSegs[se].node.name = digis[se].name
			self.addFlatBones(digis[se],digiCAT.boneSegs[se])
			self.createTempTransform(digis[se],digiCAT.boneSegs[se].node )
			RepeatPosition.append([digis[se],digiCAT.boneSegs[se].node])
			self.parseHierarchy(digis[se],digiCAT.boneSegs[se],exclude+selfbones,maxDepth,depth+1)

		#do this last while the joints articulate into final position
		

		thighCAT.width = self.legSizes[1]
		thighCAT.depth = self.legSizes[2]

		#self.addFlatBones(thighs[0],thighCAT)
		#RepeatPosition.append([digis[se],digiCAT.boneSegs[se].node])		
		self.createTempTransform(thighs[0],thighCAT.node)

		if hasAnkles:		
			footCAT.name = ""	
			footCAT.node.name = foot.name				
			footCAT.node.width = self.footSizes[1]
			footCAT.node.height = self.footSizes[2]
			footCAT.node.length = self.boneLength(foot,self.footSizes[0])
			
			RepeatPosition.append([foot,footCAT.node])				
			self.addFlatBones(foot,footCAT)
			self.createTempTransform(foot,footCAT.node)
			#parse toes
			if numDigits > 0:
				for fi in range(numDigits):
					footCAT.node.Children[fi].controller.NumBones = len(footDigits[fi])								

			if numDigits > 0:
				# futile to try to get the fingers the normal way
				
				for fi in range(numDigits):					
					footCAT.node.controller.digits[fi].NumBones = len(footDigits[fi])
					fingerData = footCAT.node.controller.digits[fi]
					fingerData.name = ""  # removes the digit sub text
					#knuckle indexing, this also calls parseHiearchy to create custom user added bones on each knuckle because why not
					for nu in range(len(footDigits[fi])):						
						fingerData.bones[nu].node.transform = footDigits[fi][nu].transform						
						fingerData.bones[nu].name = footDigits[fi][nu].name		
						fingerData.bones[nu].length = self.boneLength(footDigits[fi][nu],5)
						self.addFlatBones(footDigits[fi][nu],fingerData.bones[nu])							
						RepeatPosition.append([footDigits[fi][nu],fingerData.bones[nu].node])		
						self.parseHierarchy(footDigits[fi][nu],fingerData.bones[nu],exclude+selfbones,maxDepth,depth+1)

			
			
			#parse extra attached bones not fingers, exclude leg bones detected			
			self.parseHierarchy(foot,footCAT,exclude+selfbones,maxDepth,depth+1)
		
		
		#fix rotation of IK platform			
		self.correctPlatformPosition(legCAT,False)	
		self.flatPlatformsIKs.append(legCAT.IKtarget)	
		legCAT.layerIKFKRatio = 0.0		
		# repeat positions to bake the IK
		# in reverse forward and backward fix
		for i in reversed(RepeatPosition):
			i[1].transform = i[0].transform
		for i in RepeatPosition:
			i[1].transform = i[0].transform	
			
			
		

	def moveIKTargetToEndOfLimb(self,CatBone,val,boneDictionary=None):
		# Todo
		dummy = rt.Dummy()	
		palmCAT = CatBone.Palm	
		if boneDictionary == None:				
			ikposition = palmCAT.node.transform.position			
			dummy.transform = palmCAT.node.transform		
		else:
			node = boneDictionary[palmCAT.node.name]				
			ikposition = node.position			
					

		dummy.position = ikposition
		CatBone.IKtarget.transform = dummy.transform	
		self.flatPlatformsIKs.append(CatBone.IKtarget)			
		rt.delete(dummy)

		#CatBone.moveIKTargetToEndOfLimb(val) # undocumented feature 0.0 - 1.0 is the range to move				

	def parseArmJoints(self,armCAT,parentCAT,c,exclude,maxDepth,depth):		
		collarbones,upperarms,forearms,hand,handDigits,bones = self.getArmJoints(c)				
		numUpperSegments = len(upperarms)
		numForeArmSegments = len(forearms)		
		numDigits = len(handDigits)
		hasPalm = False
		hasCollar = False
		hasForearm = False
		collarCAT = None 
		handCAT = None
		
		selfbones = [collarbones]+upperarms+forearms+[hand]
		for fd in handDigits:
			selfbones += fd
		

		if hand != None:
			hasPalm = True
		if collarbones != None:
			hasCollar = True
		if numForeArmSegments > 0:
			hasForearm = True
		else:
			hasForearm = False			
			if numUpperSegments > 1 and self.attemptFixMisnamedBones:
				# possibly misnamed arm joints
				forearms.append( upperarms.pop() )
				numUpperSegments = len(upperarms)
				numForeArmSegments = len(forearms)				
				hasForearm = True
				

		#parentCAT.AddArm(AddCollarbone=hasCollar,AddPalm=hasPalm)		
		#armCAT = parentCAT.limbs[-1]
		armCAT.name = "" #blank out to preserve names		

		if hasPalm == True:
			armCAT.CreatePalmAnkle()
		else:
			armCAT.removePalmAnkle()			
		if hasCollar == True:
			armCAT.CreateCollarbone()
		else:
			armCAT.removeCollarbone()
		
		# disable IK/FK to allow leg to reposition
		#armCAT.layerIKFKRatio = 1.0
		
		
		if hasPalm:				
			handCAT = armCAT.Palm
			handCAT.name = "" # blanks out digits
			handCAT.node.controller.numDigits = numDigits

		upperArmCAT = armCAT.bones[0]
		upperArmCAT.numSegs = numUpperSegments

		if hasForearm:			
			foreArmCAT = armCAT.bones[1]
			foreArmCAT.width = self.armSizes[1]
			foreArmCAT.depth = self.armSizes[2]	
			foreArmCAT.numSegs = numForeArmSegments
		else:
			armCAT.NumBones = 1
		
		if hasCollar:
			collarCAT = armCAT.collarbone
			collarCAT.node.name = collarbones.name
			collarCAT.node.length = self.boneLength(collarbones)
			self.addFlatBones(collarbones,collarCAT)
			self.createTempTransform(collarbones,collarCAT.node)	
			self.parseHierarchy(collarbones,parentCAT,exclude+selfbones,maxDepth,depth+1)
											
		for se in range(numUpperSegments):			
			upperArmCAT.boneSegs[se].node.name = upperarms[se].name	
			self.addFlatBones(upperarms[se],upperArmCAT.boneSegs[se])		
			self.createTempTransform(upperarms[se],upperArmCAT.boneSegs[se].node )									
			self.parseHierarchy(upperarms[se],upperArmCAT.boneSegs[se],exclude+selfbones,maxDepth,depth+1)
			
			
		for se in range(numForeArmSegments):			
			foreArmCAT.boneSegs[se].node.name = forearms[se].name			
			self.addFlatBones(forearms[se],foreArmCAT.boneSegs[se])
			self.createTempTransform(forearms[se],foreArmCAT.boneSegs[se].node )
			self.parseHierarchy(forearms[se],foreArmCAT.boneSegs[se],exclude+selfbones,maxDepth,depth+1)
			

		#do this last while the joints articulate into final position
		
		for se in range(numUpperSegments):						
			self.parseHierarchy(upperarms[se],upperArmCAT.boneSegs[se],exclude+selfbones,maxDepth,depth+1)
			
		for se in range(numForeArmSegments):						
			self.parseHierarchy(forearms[se],foreArmCAT.boneSegs[se],exclude+selfbones,maxDepth,depth+1)
		

		upperArmCAT.length = self.armSizes[1]

		if hasForearm:
			
			upperArmCAT.length = self.boneDistanceFromBone(upperarms[0],forearms[0])	
		elif hasPalm:
			upperArmCAT.length = self.boneDistanceFromBone(upperarms[0],hand)
		else:
			upperArmCAT.length = self.armSizes[0]

		upperArmCAT.width = self.armSizes[1] 
		upperArmCAT.depth = self.armSizes[2] 
		
		

		self.addFlatBones(upperarms[0],upperArmCAT)
		self.createTempTransform(upperarms[0],upperArmCAT.node)

		if hasForearm:
			self.addFlatBones(forearms[0],foreArmCAT)
			self.createTempTransform(forearms[0],foreArmCAT.node)

		if hasPalm:			
			handCAT.node.name = hand.name				
			handCAT.node.width = self.footSizes[1]
			handCAT.node.height = self.footSizes[2]			
			handCAT.node.length = self.boneLength(hand,self.footSizes[0])
			if hasForearm:
				foreArmCAT.length = self.boneDistanceFromBone(forearms[0],hand)
			self.addFlatBones(hand,handCAT)			
			self.createTempTransform(hand,handCAT.node)
			#parse toes
			if numDigits > 0:
				for fi in range(numDigits):
					handCAT.node.Children[fi].controller.NumBones = len(handDigits[fi])								
			
			if numDigits > 0:
				# futile to try to get the fingers the normal way
				for fi in range(numDigits):					
					handCAT.node.controller.digits[fi].NumBones = len(handDigits[fi])
					fingerData = handCAT.node.controller.digits[fi]
					#knuckle indexing, this also calls parseHiearchy to create custom user added bones on each knuckle because why not
					fingerData.name = "" # erase prefix to preserve name
					for nu in range(len(handDigits[fi])):						
						fingerData.bones[nu].node.transform = handDigits[fi][nu].transform									
						fingerData.bones[nu].name = handDigits[fi][nu].name								
						fingerData.bones[nu].length = self.boneLength(handDigits[fi][nu],5)						
						self.addFlatBones(handDigits[fi][nu],fingerData.bones[nu])				
						self.parseHierarchy(handDigits[fi][nu],fingerData.bones[nu],exclude+selfbones,maxDepth,depth+1)						

			
			self.parseHierarchy(hand,handCAT,exclude+selfbones,maxDepth,depth+1)
			
		
	def parseTail(self,parentCAT,c,exclude,maxDepth,depth):
		# Spine parsing				
		tails = self.getSegmentJoints(c,self.tailNames,[])				
		tailboneLen = len(tails)
		if tailboneLen == 0:
			return False
		depth += tailboneLen	
		try:
			parentCAT.AddTail(NumBones=tailboneLen)																						
		except:
			print(f"{tails[0].name} TAIL ERROR probably misnamed. Make sure Tail segments have the same names!\n")
			return False
			# some CAT rigs do not have tails enabled
		CATTail = parentCAT.tails[-1]	
		CATTail.name = "" # blank out to preserve tail names								
		CATTail.width = self.tailSizes[1]	
		CATTail.depth = self.tailSizes[2]
		for b in range(CATTail.numBones):
			CATTail.bones[b].name = tails[b].name
			CATTail.bones[b].node.name = tails[b].name					
			segmentLength = self.boneLength(tails[b])
			#Get bone lengths
			CATTail.bones[b].node.length = segmentLength	
			self.addFlatBones(tails[b],CATTail.bones[b])																							
			self.createTempTransform(tails[b],CATTail.bones[b].node)
			if len(tails[b].Children) > 0:
				self.parseHierarchy(tails[b],CATTail.bones[b],exclude+tails,maxDepth,depth+1)
		return True

	def parseNeck(self,parentCAT,c,exclude,maxDepth,depth):
		# Neck parsing
		
		spines = self.getSegmentJoints(c,self.neckNames,self.headNames)
		spineboneLen = len(spines)		
		if spineboneLen == 0:
			return False
		depth += spineboneLen
		
		parentCAT.AddSpine(NumBones=spineboneLen-1)		
		CATSpine = parentCAT.spines[-1]		

		# Tip
		CATSpine.tipHub.name = spines[-1].name
		CATSpine.tipHub.node.name = spines[-1].name
		
		CATSpine.tipHub.node.length = self.headSizes[0]
		CATSpine.tipHub.node.width = self.headSizes[1]
		CATSpine.tipHub.node.height = self.headSizes[2]

		self.addFlatBones(spines[-1],CATSpine.tipHub)
		self.createTempTransform(spines[-1],CATSpine.tipHub.node)		
		self.disableSpineIK(CATSpine,True)	

		for b in range(CATSpine.numBones):
			CATSpine.bones[b].node.name = spines[b].name
			segmentLength = self.boneLength(spines[b])
			#Get bone lengths
			CATSpine.bones[b].node.length = segmentLength
			CATSpine.bones[b].node.width = self.spineSizes[1]
			CATSpine.bones[b].node.depth = self.spineSizes[2]
			self.addFlatBones(spines[b],CATSpine.bones[b])
			self.createTempTransform(spines[b],CATSpine.bones[b].node)
			self.createTempTransform(spines[-1],CATSpine.tipHub.node) # Continously update 
			
			if len(spines[b].Children) > 0:
				self.parseHierarchy(spines[b],CATSpine.bones[b],exclude+spines,maxDepth,depth+1)
		
		if len(spines[-1].Children) > 0:
			self.parseHierarchy(spines[-1],CATSpine.tipHub,exclude+spines,maxDepth,depth+1)
		return True
		
	def stopAtArray(self,array,needle):
		for i in array:
			if i.name == needle:
				print(array)
				raise Exception(f" NOT SUPPOSE TO HAPPEN {needle} detected in array")

	def parseSpine(self,parentCAT,c,exclude,maxDepth,depth):
		# Spine parsing				
		spines = self.getSegmentJoints(c,self.spineNames,self.chestNames)					
		spineboneLen = len(spines)
		if spineboneLen == 0:
			print(f"{parentCAT.name} SPINES NOT FOUND....\n")
			return False
		parentCAT.AddSpine(NumBones=spineboneLen-1)		
		depth += spineboneLen
		CATSpine = parentCAT.spines[-1]				
		
		# Tip
		CATSpine.tipHub.name = spines[-1].name
		CATSpine.tipHub.node.name = spines[-1].name
		CATSpine.tipHub.node.length = self.chestSizes[0] # 5
		CATSpine.tipHub.node.width = self.chestSizes[1] #20
		CATSpine.tipHub.node.height = self.chestSizes[2] #5		
		
		self.addFlatBones(spines[-1],CATSpine.tiphub)
		self.createTempTransform(spines[-1],CATSpine.tipHub.node)
		self.disableSpineIK(CATSpine,True)	
		

		for b in range(CATSpine.numBones):
			
			CATSpine.bones[b].node.name = spines[b].name
			segmentLength = self.boneLength(spines[b])
			#Get bone lengths
			CATSpine.bones[b].node.length = segmentLength
			CATSpine.bones[b].node.width = self.spineSizes[1]
			CATSpine.bones[b].node.depth = self.spineSizes[2]
			
			self.createTempTransform(spines[b],CATSpine.bones[b].node)			
			self.addFlatBones(spines[b],CATSpine.bones[b])			
			self.createTempTransform(spines[-1],CATSpine.tipHub.node) # continously update since spine is weird
			
			if len(spines[b].Children) > 0:
				self.parseHierarchy(spines[b],CATSpine.bones[b],spines,maxDepth,depth+1)
		
		# Parse the Heads
		
		if len(spines[-1].Children) > 0:					
				self.parseHierarchy(spines[-1],CATSpine.tipHub,exclude+spines,maxDepth,depth+1)
		
		return True
		

	def parseBone(self,parentCAT,c,exclude,maxDepth,depth):
		# Basic Bone Extensions				
		parentCAT.AddArbBone()		
		currentARB = parentCAT.NumArbBones
		lastNode = parentCAT.GetArbBone(currentARB)		
		self.delayedRename.append("$'{}'.name = \"{}\"".format(lastNode.node.name,c.name))					
		self.addFlatBones(c,lastNode)
		self.createTempTransform(c,lastNode.node)								
		boneLen = self.boneLength(c,5)
		lastNode.node.length = boneLen		
		
		if maxDepth > 0:
			perc = (float(depth) / float(maxDepth))
			lastNode.node.width -= ((lastNode.node.width*self.taperFactors)* perc)
			lastNode.node.depth -= ((lastNode.node.depth*self.taperFactors)* perc)
		# Parse the Children	
		

		self.parseHierarchy(c,lastNode,exclude,maxDepth,depth+1)							

	def initializeArmLimb(self,parentCAT,c):
		parentCAT.AddArm()		
		armCAT = parentCAT.limbs[-1]
		return (armCAT,c)
	
	def initializeLegLimb(self,parentCAT,c):		
		parentCAT.AddLeg()
		legCAT = parentCAT.limbs[-1]
		
		return (legCAT,c)

	def parseHierarchy(self,parentObject,parentCAT,exclude=[],maxDepth=0,depth=0):	
		# Clavicle,Collar,etc	
		armlimbs = []  # process limbs only after they are generated to avoid mirroring	
		legLimbs = []
		for c in parentObject.Children:		
			if c in exclude:	
				#print(f"{parentObject.name} Excluding {c.name}")			
				continue
			if pymxs.runtime.classof(parentCAT) != pymxs.runtime.HubTrans:
				print(f"ERROR PARENT CAT is invalid something bad happened  {c.name} type {pymxs.runtime.classof(parentCAT)}\n")
				break
			isLeg = False
			isArm = False			
			# find leg conditions and rare conditions of collarbones with legs
			#If Child is Leg or Arm CollarBone			
			thighName = self.findKeyword(c.name.lower(),self.thighNames)
			armName = self.findKeyword(c.name.lower(),self.upperarmNames)
			childhasThighs = self.childHasLegs(c)
			childhasArms = self.childHasArms(c)
			
			if childhasThighs != "":
				isLeg = True				
			if thighName != "":
				isLeg = True
			
			if childhasArms != "":
				isArm = True
			if armName != "":
				isArm = True
			isTail = self.inArrayStrings( self.tailNames , c.name )			
			isNeck = self.inArrayStrings( self.neckNames , c.name )			
			isSpine = self.inArrayStrings( self.spineNames, c.name)							
			
			#print(f"{parentObject.name} Child has thighs childhasArms {childhasArms} childhasThighs {childhasThighs} isSpine {isSpine} isNeck {isNeck}\n")
			
				
			if isArm:			
				armlimbs.append( self.initializeArmLimb(parentCAT,c) )								
			elif isLeg:
				legLimbs.append( self.initializeLegLimb(parentCAT,c) )				
			elif isTail:
				self.parseTail(parentCAT,c,exclude,maxDepth,depth)								
			elif isNeck:				
				self.parseNeck(parentCAT,c,exclude,maxDepth,depth)												
			elif isSpine:
				self.parseSpine(parentCAT,c,exclude,maxDepth,depth)	
			else :
				# this part is recursive too				
				self.parseBone(parentCAT,c,exclude,maxDepth,depth)	

		# Process Limbs separately so they dont mirror		
		for a in armlimbs:			
			self.parseArmJoints(a[0],parentCAT,a[1],exclude,maxDepth,depth)
		for l in legLimbs:
			self.parseLegJoints(l[0],parentCAT,l[1],exclude,maxDepth,depth)
		
	#https://gist.github.com/tpoveda/eb668ca1bd7504123e37a0d461d3ffd2
		
	def transferBones(self,mesh,sourceBones,targetBones):
		#https://help.autodesk.com/view/MAXDEV/2022/ENU/?guid=GUID-0820AA26-920F-434D-A6BC-E8B6B57F54AC
		
		rt.execute("max modify mode") # a bug in 3dsmax where skin utilities don't work if the modify tab isn't visible
		# because for some reason 3dsmax's skin utilities lives inside the Modify UI.

		currentPose = []
		# storing initial bone pose
		for i in targetBones:
			currentPose.append( i.transform )
		rt.select(sourceBones+mesh)	
		bindpose = self.getBindPose(mesh)
		self.gotoBindPose(mesh,bindpose)						
		
		# pose the CAT bones
		for i in range(len(targetBones)):
			targetBones[i].transform = sourceBones[i].transform

		for x in mesh.modifiers:
			if str(x) == "Skin:Skin":					
				# duplicate rigging
				isCloned = rt.skinUtils.extractSkinData(mesh)
				cloned = rt.getNodeByName("SkinData_"+mesh.name)
				if isCloned:
					
					skinObject = x							
					bones = rt.skinOps.GetBoneNodes(skinObject)					
					boneorder = []
					b1 = len(bones)
					for s in range(b1):							
						if bones[s] in sourceBones:							
							boneIndex = sourceBones.index(bones[s])								
						else:
							bname = bones[s].name
							raise Exception(f"MISSING BONES IN SOURCE {bname}\n")
							
						boneorder.append(targetBones[boneIndex])						
					
					for s in reversed(range(b1)):
						rt.skinOps.removeBone(skinObject,bones[s])						
					
					bonesBefore = rt.skinOps.GetBoneNodes(skinObject)					

					b3 = len(bonesBefore)
					
					if b3 > 0:
						raise Exception(f"{mesh.name} Unable to remove bones there are {b3} remaining\n")
					for s in boneorder:
						rt.skinOps.addbone(skinObject,s,0)		

					bonesAfter = rt.skinOps.GetBoneNodes(skinObject)					
					b2 = len(bonesAfter)
					
					useMatchingName = self.skinTransferMatchByName
					if b1 != b2:
						print(f"There {mesh.name} a difference in transfered bones from Original bone count of {b1} to {b2} Using Bone names for Transfer")
						useMatchingName = True
					
					#rt.skinUtils.ImportSkinData(mesh,cloned)
					rt.select([mesh,cloned])
					rt.skinUtils.ImportSkinDataNoDialog(useMatchingName,False,False,False,False,self.skinTransferThreshold,0 )					
					rt.delete(cloned)		
									

		# return original back to normal Pose too
		for i in range(len(sourceBones)):
			sourceBones[i].transform = currentPose[i]
		
		# return catbones back to normal Pose		
		for i in range(len(targetBones)):
			targetBones[i].transform = sourceBones[i].transform


	def inspect_Skin(self):
		
		numselected = len(rt.getCurrentSelection())		
		if numselected > 0:
			selected = rt.getCurrentSelection()[0]
			objectType = rt.classof(selected)
			
			#with pymxs.undo(True):
			for x in selected.modifiers:
				if str(x) == "Skin:Skin":					
					skinObject = x					
					print("{} = {} \n".format(selected,x))
					bones = rt.skinOps.GetBoneNodes(skinObject)					
					for s in range(len(bones)):
						print("{}\t{}\n".format(s,bones[s]))
						try:
							rt.skinOps.removeBone(skinObject,bones[s])
						except:
							print("{} Failed to remove {}\n".format(s,bones[s]))
						
						
	def addFlatBones(self,bone,catbone):
		self.flatBoneList.append(bone)
		self.flatCATBones.append(catbone.node)
	
	def get_skinned_meshes(self,boneNeedles):		
		skinned_meshes = []
		for obj in pymxs.runtime.objects:
			if pymxs.runtime.classof(obj) == pymxs.runtime.Editable_mesh or pymxs.runtime.classof(obj) == pymxs.runtime.Editable_poly or pymxs.runtime.classof(obj) == pymxs.runtime.PolyMeshObject :
				for x in obj.modifiers:
						if str(x) == "Skin:Skin":					
							skin_modifier = x								
							bones = rt.skinOps.GetBoneNodes(skin_modifier)	
							for i in range(len(bones)):								
								bone = bones[i]
								if bone in boneNeedles:
									skinned_meshes.append(obj)
									break  # Move to the next mesh if the bone is found
		return skinned_meshes
	def getBindPose(self,mesh):
		transformmatrixes = []
		for x in mesh.modifiers:
			if str(x) == "Skin:Skin":					
				skin_modifier = x								
				bones = rt.skinOps.GetBoneNodes(skin_modifier)	
				for b in range(len(bones)):					
					matrix = rt.skinUtils.GetBoneBindTM(mesh,bones[b])
					transformmatrixes.append(matrix)
				
		return transformmatrixes
	
	def CATGotoBindPose(self,mesh,skin_modifier,matrixArray):
		ikHandles = [] # array of ik controllers
		ikBlendStates = [] # array of blend states
		ikSpineHandles = [] # array of spine controllers
		ikSpineStates = [] # array of spine spinecontroller booleans
		boneDictionary= dict()
		boneOldNames = []
		bones = list(rt.skinOps.GetBoneNodes(skin_modifier))
		rootbone = None 
		for b in bones:
			if b.parent not in bones:
				rootbone = b		
		sortedlist = self.getSegmentJoints(rootbone,[],[])
		
		cleanedlist = []
		sortedMatrix = []
		for i in sortedlist:
			try:
				index = bones.index(i)
				if index > -1:
					cleanedlist.append(bones[index])
					sortedMatrix.append(matrixArray[index])
			except:
				pass

		bones = cleanedlist
		matrixArray = sortedMatrix		

		CATlengths = [] # sometimes if you can accidentally stretch the bones causing problems
		
		for b in range(len(bones)):
			boneOldNames.append(bones[b].name)
			# solving duplicate names
			bones[b].name = f"{b}_"+rt.uniquename(bones[b].name)					
			#print(f"{b} New name = {bones[b].name}\n")
			boneDictionary[ bones[b].name ] = matrixArray[b]

		
		for b in range(len(bones)):																		
			bonelength = self.boneLengthFromMatrix(bones[b],boneDictionary)											
			CATlengths.append( bonelength ) 

			try:						
				ikTarget = bones[b].Controller.LimbData.IKtarget						
				if ikTarget:													
					ikController =  bones[b].Controller.Limb # bones[b].Controller.LimbData
					
					if ikController not in ikHandles:
						ikHandles.append(ikController)
						ikBlendStates.append(ikController.layerIKFKRatio)
						ikController.layerIKFKRatio = 1.0							
			except:
				pass
			try:												
				ikSpine = bones[b].Controller.CATSpineData2						
				if ikSpine:							
					spineController = bones[b].Controller.CATSpineData2							
					if spineController not in ikSpineHandles:
						ikSpineHandles.append(spineController)
						ikSpineStates.append( self.disableSpineIK(spineController,True) )																
			except:
				pass
		# sort the limbs out
						
		for b in (range(len(bones))):
			bones[b].transform = matrixArray[b]
			if CATlengths[b] > -1:
				bones[b].length = CATlengths[b]						
		

		for i in range(len(ikSpineHandles)):					
			self.disableSpineIK(ikSpineHandles[i],ikSpineStates[i])

		# restore ik's
		for i in range(len(ikHandles)):										
			if ikHandles[i].isLeg:
				self.correctPlatformPosition(ikHandles[i],False,boneDictionary)					
				ikHandles[i].layerIKFKRatio = ikBlendStates[i]		
		
				
			
		
		# Always start in reverse
		for b in reversed(range(len(bones))):			
			if CATlengths[b] > -1:
				bones[b].length = CATlengths[b]			
			bones[b].transform = matrixArray[b]			
		for b in (range(len(bones))):			
			bones[b].transform = matrixArray[b]							
			if CATlengths[b] > -1:
				bones[b].length = CATlengths[b]			

				
		for i in range(len(ikHandles)):										
			if not ikHandles[i].isLeg:				
				self.moveIKTargetToEndOfLimb(ikHandles[i],1,boneDictionary)
				ikHandles[i].layerIKFKRatio = ikBlendStates[i]	
				

		for b in range(len(bones)):
			bones[b].name = boneOldNames[b]
		

		


	def gotoBindPose(self,mesh,matrixArray):
		#need to disable CATrig from twisting my joints
		
		for x in mesh.modifiers:
			if str(x) == "Skin:Skin":									
				hasCAT = False				
				skin_modifier = x								
				bones = rt.skinOps.GetBoneNodes(skin_modifier)									
				#first find bones that are spines
				for b in range(len(bones)):	
					try:
						if bones[b].Controller.CATParent :						
							hasCAT = True							
					except:
						pass
					if hasCAT:
						self.CATGotoBindPose(mesh,skin_modifier,matrixArray)
						break;
					
					
				for b in range(len(bones)):																
					bones[b].transform = matrixArray[b]																		
															
				
	
	def disableSpineIK(self,spineCAT,toggle):
		oldState = spineCAT.SpineFK		
		rt.Execute("SetQuietMode On")
		spineCAT.SpineFK = toggle
		rt.Execute("SetQuietMode Off")		
		return oldState
	
	
	def getCombinedBoundingBox(self,objects):
		"""
		Calculates the combined bounding box of an array of objects.

		Args:
			objects: A list of 3ds Max nodes.

		Returns:
			A pymxs.runtime.Box3 object representing the combined bounding box, or None if the array is empty.
		"""
		if not objects:
			return None

		first_box = rt.nodeGetBoundingBox(objects[0] , objects[0].transform, asBox3=True)
		min_point = first_box.min
		max_point = first_box.max

		for obj in objects[1:]:
			box = pymxs.runtime.nodeGetBoundingBox(obj, obj.transform, asBox3=True)
			min_point.x = min(min_point.x, box.min.x)
			min_point.y = min(min_point.y, box.min.y)
			min_point.z = min(min_point.z, box.min.z)

			max_point.x = max(max_point.x, box.max.x)
			max_point.y = max(max_point.y, box.max.y)
			max_point.z = max(max_point.z, box.max.z)
		return rt.Box3(min_point, max_point)

	def correctPlatformPosition(self,legCAT,offsetToToes=False,boneDictionary=None):		
		footCAT = legCAT.Palm	
		footlen = self.boneLength(footCAT.node,self.footSizes[0])	
		#fix rotation of IK platform and offset to the base of the palm/foot
		offset = 0
		if offsetToToes:
			numDigits = footCAT.node.controller.numDigits
			fingerGroup = [footCAT.node]
			if numDigits > 0:			
				for fi in range(numDigits):
					knuckles = footCAT.node.controller.digits[fi].NumBones
					fingerData = footCAT.node.controller.digits[fi]
					for nu in range(knuckles):
						fingerGroup.append(fingerData.bones[nu].node)									
			bb = self.getCombinedBoundingBox(fingerGroup)
				
			if self.lengthAxis == "X":				
				forwardpoint = rt.point3( footlen , 0 , 0 ) * footCAT.node.transform.rotation
			if self.lengthAxis == "Z":				
				forwardpoint = rt.point3( 0 , footlen , 0 ) * footCAT.node.transform.rotation			
			ikposition = (footCAT.node.transform.position + forwardpoint)
			ikposition.z = bb.min.z
			

		else:
			#project to floor	
			if boneDictionary == None:
				if self.lengthAxis == "X":				
					forwardpoint = rt.point3( footlen, 0 , 0 ) * footCAT.node.transform.rotation
				if self.lengthAxis == "Z":				
					forwardpoint = rt.point3( 0 , footlen , 0 ) * footCAT.node.transform.rotation				
				ikposition = footCAT.node.transform.position + forwardpoint
			else :				
				node = boneDictionary[footCAT.node.name]				
				footlen = self.footSizes[0]
				footlenfound = self.boneLengthFromMatrix(footCAT.node,boneDictionary)	
				if footlenfound > -1:
					footlen = footlenfound

				if self.lengthAxis == "X":				
					forwardpoint = rt.point3( footlen, 0 , 0 ) * node.rotation
				if self.lengthAxis == "Z":				
					forwardpoint = rt.point3( 0 , footlen , 0 ) * node.rotation				
				ikposition = node.position + forwardpoint
			ikposition.z = 0

		
		dummy = rt.Dummy()		
		dummy.transform = footCAT.node.transform
		dummy.rotation = self.platformRotation
		dummy.position = ikposition
		legCAT.IKtarget.transform = dummy.transform				
		rt.delete(dummy)

	def selectReturnToBindPose(self):		
		with pymxs.undo(True):				
			numselected = len(rt.getCurrentSelection())		
			selectedRootBone = None
			self.skinnedObjects = []
			
			if(self.lengthAxis == "X"):
				self.platformRotation = rt.EulerAngles(180,-90,0)				
			if(self.lengthAxis == "Z"):	
				self.platformRotation = rt.EulerAngles(180,0,0)							
			
			for s in range(numselected):
				mesh = rt.getCurrentSelection()[s]
				pose = self.getBindPose(mesh)
				self.gotoBindPose(mesh,pose)

	def validateBonePositions(self,flatSource,flattarget):
		for i in range(len(flatSource)):
			bonename = flatSource[i].name
			closeness = self.isBoneTheSame(flatSource[i],flattarget[i])	

	def create_CAT_from_Bones(self):		

		#with pymxs.undo(True):						
		if True:
			self.flatBoneList = []
			self.flatCATBones = []
			
			numselected = len(rt.getCurrentSelection())		
			selectedRootBone = None
			self.skinnedObjects = []
			for s in range(numselected):
				if rt.classof( rt.getCurrentSelection()[s] ) == pymxs.runtime.Dummy or rt.classof( rt.getCurrentSelection()[s] ) == pymxs.runtime.BoneGeometry :
					selectedRootBone = rt.getCurrentSelection()[s]

			if selectedRootBone != None:
				CATParentObj = rt.CATParent( )	
				# check if the name is a pelvis and prefixxed by a name
				
				rootname = selectedRootBone.name			
				CATParentObj.CATUnits = 1
				CATParentObj.CATName = self.CATName
				CATParentObj.lengthAxis = self.lengthAxis
								
				# grab parent bone and copy position and rotation	

				#TODO: this isn't setup yet for Y up		
				#self.platformRotation = rt.EulerAngles(180,-90,0)
				
				if(self.lengthAxis == "X"):
					self.platformRotation = rt.EulerAngles(180,-90,0)
					CATParentObj.rotation = self.platformRotation
					if self.moveBaseToCharacter:				
						newPos = selectedRootBone.position
						newPos.z = 0
						CATParentObj.position = newPos
					CATParentObj.rotation = self.platformRotation
				
				if(self.lengthAxis == "Z"):	
					self.platformRotation = rt.EulerAngles(180,0,0)							
					CATParentObj.rotation = self.platformRotation
					if self.moveBaseToCharacter:				
						newPos = selectedRootBone.position
						#newPos.x = 0
						newPos.z = 0
						CATParentObj.position = newPos
					
								
				CATParentObj.AddHub()
				pelvisHUB = CATParentObj.RootHub #HubTrans	
				pelvisHUB.node.length = self.hipSizes[0]
				pelvisHUB.node.width = self.hipSizes[1]
				pelvisHUB.node.height = self.hipSizes[2]			
				arraynodes = CATParentObj.CATRigNodes
				rootNode = arraynodes[1]
				rootNode.name = rootname						
				maxDepth = self.maxHierarchyDepth(selectedRootBone,0)	
				print(f"Class of hub is {rt.classof(pelvisHUB)}\n")
				self.addFlatBones(selectedRootBone,pelvisHUB)				
				self.createTempTransform(selectedRootBone,rootNode)				
				self.parseHierarchy(selectedRootBone,pelvisHUB,[],maxDepth)				
				
				


				for d in self.delayedRename:					
					try:
						rt.execute(d)
					except:
						print(f"Unable to Rename [{d}] possible scene naming conflicts\n")

				self.skinnedObjects = self.get_skinned_meshes(self.flatBoneList)				
				

				if self.moveSkinsToCAT:										
					for m in range(len(self.skinnedObjects)):
						print(f" Transfering Skinning to {self.skinnedObjects[m].name}\n")
						self.transferBones(self.skinnedObjects[m],self.flatBoneList,self.flatCATBones)
				
				# copy layers
				print("Assigning Layers to CAT Bones\n")
				for bindex in range(len(self.flatBoneList)):					
					layer = self.flatBoneList[bindex].layer
					layer.addNode(self.flatCATBones[bindex])
					layer.addNode(CATParentObj)
					for ik in self.flatPlatformsIKs:
						layer.addNode(ik)
				# parent CAT root bone to original parent
				originalParent = selectedRootBone.parent
				if originalParent != None:
					self.flatCATBones[0].parent = originalParent				
					CATParentObj.parent = originalParent
					CATParentObj.name = rt.uniquename(originalParent.name)
					for ik in self.flatPlatformsIKs:
						ik.parent = originalParent	

				if self.deleteOldBones: 
					if(len(self.skinnedObjects) > 0 ):
						if(self.moveSkinsToCAT == False):
							print("Cannot Delete Original Skeleton, it is Currently in Use")
						else:
							rt.delete(self.flatBoneList)		
					else:
						rt.delete(self.flatBoneList)	
				if self.CATBoxModeDisplay:
					for b in self.flatCATBones:
						b.boxmode = True

				print("Skeleton 2 CAT Completed\n")		
				return True
			else:
				print("Need A Bone selected!\n")
				return False								
		return False
		
		