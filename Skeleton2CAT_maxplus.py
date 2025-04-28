"""
Shinobu's Skeleton to CAT Script for Onirism
v1.0
Tested on 3dsmax 2016
THIS DOESNT WORK as its hard to figure out how to Get the CAT Object nodes with MaxPlus
"""

import MaxPlus
import math

def isclose(a, b, abs_tol=1e-6):
	return abs(a - b) <= abs_tol

class Skeleton2CAT:
	def __init__(self):
		# Names have to be LOWER CASE
		self.headNames = ["head"]
		self.chestNames = ["ribcage"]
		self.collarNames = ["scapula", "collar"]
		self.upperarmNames = ["upperarm", "bicep"]
		self.forearmNames = ["forearm"]
		self.thighNames = ["thigh"]
		self.calfNames = ["calf"]
		self.handNames = ["palm", "manus", "prima", "hand"]
		self.fingerNames = ["digit", "hoof", "finger", "thumb", "index", "middle", "ring", "hallux"]
		self.ankleNames = ["ankle", "feet", "foot"]
		self.spineNames = ["spine"]
		self.tailNames = ["tail"]
		self.neckNames = ["neck"]
		self.taperFactors = 0.25
		self.hipSizes = [3, 10, 5]
		self.legSizes = [5, 5, 5]
		self.footSizes = [10, 5, 2]
		self.chestSizes = [5, 20, 5]
		self.headSizes = [10, 10, 12]
		self.spineSizes = [5, 5, 5]
		self.armSizes = [3, 3, 3]
		self.tailSizes = [3, 3, 3]
		self.skinnedObjects = []
		self.moveBaseToCharacter = True
		self.moveSkinsToCAT = True
		self.deleteOldBones = True
		self.CATBoxModeDisplay = True
		self.lengthAxis = "X"  # "X" "Z"
		self.delayedRename = []
		self.CATName = ""  # leave blank to preserve tail names
		self.flatBoneList = []
		self.flatCATBones = []
		self.positionDistanceMatch = 0.0001
		self.skinTransferThreshold = 1
		self.skinTransferMatchByName = False

	def createTempTransform(self, sourceBone, targetBone):
		targetBone.Transform = sourceBone.Transform
		return True

	def maxHierarchyDepth(self, parentObject, depth=0):
		result = depth
		for c in parentObject.Children:
			childrenLen = len(c.Children)
			if childrenLen > 0:
				rs = self.maxHierarchyDepth(c, depth + 1)
				if rs > result:
					result = rs
		return result

	def inArrayStrings(self, listhaystack, needleString):
		for i in listhaystack:
			if i.lower() in needleString.lower():
				return True
		return False

	def getSegmentJoints(self, parentObject, segmentNames, endTipNames):
		result = []
		if self.inArrayStrings(segmentNames, parentObject.Name) or len(segmentNames) == 0:
			result.append(parentObject)
			childrenLen = len(parentObject.Children)
			if childrenLen > 0:
				for c in parentObject.Children:
					if self.inArrayStrings(segmentNames, c.Name):
						result += self.getSegmentJoints(c, segmentNames, endTipNames)
					elif (len(endTipNames) == 0 and len(segmentNames) == 0):
						result += self.getSegmentJoints(c, segmentNames, endTipNames)
					elif (self.inArrayStrings(endTipNames, c.Name) and len(endTipNames) > 0):
						result.append(c)
		return result

	def createPoint(self, p1, p2, p3):
		return MaxPlus.Point3(p1, p2, p3)

	def boneDistanceFromBone(self, boneA, boneB):
		startPos = boneA.Position
		endPos = boneB.Position
		p1 = self.createPoint(startPos.X, startPos.Y, startPos.Z)
		p2 = self.createPoint(endPos.X, endPos.Y, endPos.Z)
		return MaxPlus.Core.Distance(p1, p2)

	def boneLength(self, bone, defaultlength=5):
		if len(bone.Children) == 0:
			return defaultlength
		boneB = bone.Children[0]
		startPos = bone.Position
		endPos = boneB.Position
		p1 = self.createPoint(startPos.X, startPos.Y, startPos.Z)
		p2 = self.createPoint(endPos.X, endPos.Y, endPos.Z)
		result = MaxPlus.Core.Distance(p1, p2)
		if result <= 0.01:
			result = defaultlength
		return result

	def findKeyword(self, needle, haystacksArray):
		for h in haystacksArray:
			if h.lower() in needle.lower():
				return h
		return ""

	def getArmJoints(self, parentObject):
		collarbones = None
		upperarms = []
		forearms = []
		hand = None
		handDigits = []
		flathierarchy = self.getSegmentJoints(parentObject, [], [])
		flatDigits = []
		flathierarchyFiltered = []
		for l in range(len(flathierarchy)):
			c = flathierarchy[l]
			cname = c.Name.lower()
			upperarmsName = self.findKeyword(c.Name.lower(), self.upperarmNames)
			forearmName = self.findKeyword(c.Name.lower(), self.forearmNames)
			handName = self.findKeyword(c.Name.lower(), self.handNames)
			digitName = self.findKeyword(c.Name.lower(), self.fingerNames)
			if l == 0:
				if upperarmsName == "":
					collarbones = c
					flathierarchyFiltered.append(c)
				elif upperarmsName != "":
					upperarms.append(c)
					flathierarchyFiltered.append(c)
			else:
				if upperarmsName != "":
					upperarms.append(c)
					flathierarchyFiltered.append(c)
				if forearmName != "":
					forearms.append(c)
					flathierarchyFiltered.append(c)
				if handName != "" and hand is None:
					hand = c
					flathierarchyFiltered.append(c)
				if digitName != "":
					flatDigits.append(c)
					flathierarchyFiltered.append(c)
		if hand is not None:
			numDigits = len(hand.Children)
			if numDigits > 0:
				for f in hand.Children:
					digitName = self.findKeyword(f.Name.lower(), self.fingerNames)
					if digitName != "":
						digitArray = self.getSegmentJoints(f, [digitName], [])
						handDigits.append(digitArray)
						flathierarchyFiltered += digitArray
		return collarbones, upperarms, forearms, hand, handDigits, flathierarchyFiltered

	def getLegJoints(self, parentObject):
		collarbones = None
		thighs = []
		calfs = []
		foot = None
		footDigits = []
		flathierarchy = self.getSegmentJoints(parentObject, [], [])
		flatDigits = []
		flathierarchyFiltered = []
		for l in range(len(flathierarchy)):
			c = flathierarchy[l]
			thighName = self.findKeyword(c.Name.lower(), self.thighNames)
			calfName = self.findKeyword(c.Name.lower(), self.calfNames)
			ankleName = self.findKeyword(c.Name.lower(), self.ankleNames)
			digitName = self.findKeyword(c.Name.lower(), self.fingerNames)
			if l == 0:
				if thighName == "":
					collarbones = c
					flathierarchyFiltered.append(c)
				elif thighName != "":
					thighs.append(c)
					flathierarchyFiltered.append(c)
			else:
				if thighName != "":
					thighs.append(c)
					flathierarchyFiltered.append(c)
				if calfName != "":
					calfs.append(c)
					flathierarchyFiltered.append(c)
				if ankleName != "" and foot is None:
					foot = c
					flathierarchyFiltered.append(c)
				if digitName != "":
					flatDigits.append(c)
					flathierarchyFiltered.append(c)
		if foot is not None:
			numDigits = len(foot.Children)
			if numDigits > 0:
				for f in foot.Children:
					digitName = self.findKeyword(f.Name.lower(), self.fingerNames)
					if digitName != "":
						digitArray = self.getSegmentJoints(f, [digitName], [])
						footDigits.append(digitArray)
						flathierarchyFiltered += digitArray
		return collarbones, thighs, calfs, foot, footDigits, flathierarchyFiltered

	def childHasLegs(self, parentObject):
		for c in parentObject.Children:
			thighName = self.findKeyword(c.Name.lower(), self.thighNames)
			if thighName != "":
				return thighName
		return ""

	def childHasArms(self, parentObject):
		for c in parentObject.Children:
			armName = self.findKeyword(c.Name.lower(), self.upperarmNames)
			if armName != "":
				return armName
		return ""

	def quaternion_equal(self, q1, q2, tolerance=1e-6):
		for id, val in enumerate(q1):
			if not isclose(q1[id], q2[id], abs_tol=tolerance):
				return False
		return True

	def isBoneTheSame(self, nodeA, nodeB):
		posDistance = MaxPlus.Core.Distance(nodeA.Position, nodeB.Position)
		scaleDistance = MaxPlus.Core.Distance(nodeA.Scale, nodeB.Scale)
		quatTolerance = self.quaternion_equal(nodeA.Rotation, nodeB.Rotation, self.positionDistanceMatch)
		return (posDistance < self.positionDistanceMatch) and (scaleDistance < self.positionDistanceMatch) and quatTolerance

	def parseLegJoints(self, legCAT, parentCAT, c, exclude, maxDepth, depth):
		collarbones, thighs, calfs, foot, footDigits, bones = self.getLegJoints(c)
		numThighSegments = len(thighs)
		numCalfSegments = len(calfs)
		numDigits = len(footDigits)
		hasAnkles = foot is not None
		hasCollar = collarbones is not None
		collarCAT = None
		footCAT = None

		if hasAnkles:
			legCAT.CreatePalmAnkle()
		else:
			legCAT.RemovePalmAnkle()
		if hasCollar:
			legCAT.CreateCollarbone()
		else:
			legCAT.RemoveCollarbone()

		legCAT.LayerIKFKRatio = 1.0

		if hasAnkles:
			footCAT = legCAT.Palm
			footCAT.Node.Controller.NumDigits = numDigits

		thighCAT = legCAT.Bones[0]
		calfCAT = legCAT.Bones[1]

		if hasCollar:
			collarCAT = legCAT.Collarbone
			collarCAT.Node.Length = self.boneLength(collarbones)
			self.addFlatBones(collarbones, collarCAT)
			self.createTempTransform(collarbones, collarCAT.Node)
			self.parseHierarchy(collarbones, parentCAT, exclude + bones, maxDepth, depth + 1)

		legCAT.Name = ""
		thighCAT.NumSegs = numThighSegments
		calfCAT.NumSegs = numCalfSegments

		for se in range(numThighSegments):
			thighCAT.BoneSegs[se].Node.Name = thighs[se].Name
			self.addFlatBones(thighs[se], thighCAT.BoneSegs[se])
			self.createTempTransform(thighs[se], thighCAT.BoneSegs[se].Node)

		for se in range(numCalfSegments):
			calfCAT.BoneSegs[se].Node.Name = calfs[se].Name
			self.addFlatBones(calfs[se], calfCAT.BoneSegs[se])
			self.createTempTransform(calfs[se], calfCAT.BoneSegs[se].Node)

		for se in range(numThighSegments):
			self.parseHierarchy(thighs[se], thighCAT.BoneSegs[se], exclude + bones, maxDepth, depth + 1)
		for se in range(numCalfSegments):
			self.parseHierarchy(calfs[se], calfCAT.BoneSegs[se], exclude + bones, maxDepth, depth + 1)

		thighCAT.Length = self.legSizes[0]
		if calfs:
			thighCAT.Length = self.boneDistanceFromBone(thighs[0], calfs[0])
		thighCAT.Width = calfCAT.Width = self.legSizes[1]
		thighCAT.Depth = calfCAT.Depth = self.legSizes[2]

		self.addFlatBones(thighs[0], thighCAT)
		self.createTempTransform(thighs[0], thighCAT.Node)
		self.addFlatBones(calfs[0], calfCAT)
		self.createTempTransform(calfs[0], calfCAT.Node)

		if hasAnkles:
			footCAT.Name = ""
			footCAT.Node.Name = foot.Name
			footCAT.Node.Width = self.footSizes[1]
			footCAT.Node.Height = self.footSizes[2]
			footCAT.Node.Length = self.boneLength(foot, self.footSizes[0])
			calfCAT.Length = self.boneDistanceFromBone(calfs[0], foot)
			self.addFlatBones(foot, footCAT)
			self.createTempTransform(foot, footCAT.Node)
			if numDigits > 0:
				for fi in range(numDigits):
					footCAT.Node.Children[fi].Controller.NumBones = len(footDigits[fi])
				for fi in range(numDigits):
					footCAT.Node.Controller.Digits[fi].NumBones = len(footDigits[fi])
					fingerData = footCAT.Node.Controller.Digits[fi]
					fingerData.Name = ""
					for nu in range(len(footDigits[fi])):
						fingerData.Bones[nu].Node.Transform = footDigits[fi][nu].Transform
						fingerData.Bones[nu].Name = footDigits[fi][nu].Name
						self.addFlatBones(footDigits[fi][nu], fingerData.Bones[nu])
						self.parseHierarchy(footDigits[fi][nu], fingerData.Bones[nu], exclude + bones, maxDepth, depth + 1)
			self.parseHierarchy(foot, footCAT, exclude + bones, maxDepth, depth + 1)

		legCAT.MoveIKTargetToEndOfLimb(1)
		legCAT.LayerIKFKRatio = 0.0

	def parseArmJoints(self, armCAT, parentCAT, c, exclude, maxDepth, depth):
		collarbones, upperarms, forearms, hand, handDigits, bones = self.getArmJoints(c)
		numUpperSegments = len(upperarms)
		numForeArmSegments = len(forearms)
		numDigits = len(handDigits)
		hasPalm = hand is not None
		hasCollar = collarbones is not None
		collarCAT = None
		handCAT = None

		armCAT.Name = ""
		if hasPalm:
			armCAT.CreatePalmAnkle()
		else:
			armCAT.RemovePalmAnkle()
		if hasCollar:
			armCAT.CreateCollarbone()
		else:
			armCAT.RemoveCollarbone()

		if hasPalm:
			handCAT = armCAT.Palm
			handCAT.Name = ""
			handCAT.Node.Controller.NumDigits = numDigits

		upperArmCAT = armCAT.Bones[0]
		foreArmCAT = armCAT.Bones[1]

		if hasCollar:
			collarCAT = armCAT.Collarbone
			collarCAT.Node.Name = collarbones.Name
			collarCAT.Node.Length = self.boneLength(collarbones)
			self.addFlatBones(collarbones, collarCAT)
			self.createTempTransform(collarbones, collarCAT.Node)
			self.parseHierarchy(collarbones, parentCAT, exclude + bones, maxDepth, depth + 1)

		upperArmCAT.NumSegs = numUpperSegments
		foreArmCAT.NumSegs = numForeArmSegments

		for se in range(numUpperSegments):
			upperArmCAT.BoneSegs[se].Node.Name = upperarms[se].Name
			self.addFlatBones(upperarms[se], upperArmCAT)
			self.createTempTransform(upperarms[se], upperArmCAT.BoneSegs[se].Node)

		for se in range(numForeArmSegments):
			foreArmCAT.BoneSegs[se].Node.Name = forearms[se].Name
			self.addFlatBones(forearms[se], foreArmCAT)
			self.createTempTransform(forearms[se], foreArmCAT.BoneSegs[se].Node)

		for se in range(numUpperSegments):
			self.parseHierarchy(upperarms[se], upperArmCAT.BoneSegs[se], exclude + bones, maxDepth, depth + 1)
		for se in range(numForeArmSegments):
			self.parseHierarchy(forearms[se], foreArmCAT.BoneSegs[se], exclude + bones, maxDepth, depth + 1)

		upperArmCAT.Length = self.armSizes[1]
		if forearms:
			upperArmCAT.Length = self.boneDistanceFromBone(upperarms[0], forearms[0])
		upperArmCAT.Width = foreArmCAT.Width = self.armSizes[1]
		upperArmCAT.Depth = foreArmCAT.Depth = self.armSizes[2]

		self.addFlatBones(upperarms[0], upperArmCAT)
		self.createTempTransform(upperarms[0], upperArmCAT.Node)
		self.addFlatBones(forearms[0], foreArmCAT)
		self.createTempTransform(forearms[0], foreArmCAT.Node)

		if hasPalm:
			handCAT.Node.Name = hand.Name
			handCAT.Node.Width = self.footSizes[1]
			handCAT.Node.Height = self.footSizes[2]
			handCAT.Node.Length = self.boneLength(hand, self.footSizes[0])
			foreArmCAT.Length = self.boneDistanceFromBone(forearms[0], hand)
			self.addFlatBones(hand, handCAT)
			self.createTempTransform(hand, handCAT.Node)
			if numDigits > 0:
				for fi in range(numDigits):
					handCAT.Node.Children[fi].Controller.NumBones = len(handDigits[fi])
				for fi in range(numDigits):
					handCAT.Node.Controller.Digits[fi].NumBones = len(handDigits[fi])
					fingerData = handCAT.Node.Controller.Digits[fi]
					fingerData.Name = ""
					for nu in range(len(handDigits[fi])):
						fingerData.Bones[nu].Node.Transform = handDigits[fi][nu].Transform
						fingerData.Bones[nu].Name = handDigits[fi][nu].Name
						self.addFlatBones(handDigits[fi][nu], fingerData.Bones[nu])
						self.parseHierarchy(handDigits[fi][nu], fingerData.Bones[nu], exclude + bones, maxDepth, depth + 1)
			self.parseHierarchy(hand, handCAT, exclude + bones, maxDepth, depth + 1)

	def parseTail(self, parentCAT, c, exclude, maxDepth, depth):
		tails = self.getSegmentJoints(c, self.tailNames, [])
		tailboneLen = len(tails)
		if tailboneLen == 0:
			return False
		depth += tailboneLen
		parentCAT.AddTail(NumBones=tailboneLen)
		CATTail = parentCAT.Tails[-1]
		CATTail.Name = ""
		CATTail.Width = self.tailSizes[1]
		CATTail.Depth = self.tailSizes[2]
		for b in range(CATTail.NumBones):
			CATTail.Bones[b].Name = tails[b].Name
			CATTail.Bones[b].Node.Name = tails[b].Name
			segmentLength = self.boneLength(tails[b])
			CATTail.Bones[b].Node.Length = segmentLength
			self.addFlatBones(tails[b], CATTail.Bones[b])
			self.createTempTransform(tails[b], CATTail.Bones[b].Node)
			if len(tails[b].Children) > 0:
				self.parseHierarchy(tails[b], CATTail.Bones[b], exclude + tails, maxDepth, depth + 1)
		return True

	def parseNeck(self, parentCAT, c, exclude, maxDepth, depth):
		spines = self.getSegmentJoints(c, self.neckNames, self.headNames)
		spineboneLen = len(spines)
		if spineboneLen == 0:
			return False
		depth += spineboneLen
		parentCAT.AddSpine(NumBones=spineboneLen - 1)
		CATSpine = parentCAT.Spines[-1]
		for b in range(CATSpine.NumBones):
			CATSpine.Bones[b].Node.Name = spines[b].Name
			segmentLength = self.boneLength(spines[b])
			CATSpine.Bones[b].Node.Length = segmentLength
			CATSpine.Bones[b].Node.Width = self.spineSizes[1]
			CATSpine.Bones[b].Node.Depth = self.spineSizes[2]
			self.addFlatBones(spines[b], CATSpine.Bones[b])
			self.createTempTransform(spines[b], CATSpine.Bones[b].Node)
			if len(spines[b].Children) > 0:
				self.parseHierarchy(spines[b], CATSpine.Bones[b], exclude + spines, maxDepth, depth + 1)
		CATSpine.TipHub.Name = spines[1].Name
		CATSpine.TipHub.Node.Name = spines[-1].Name
		CATSpine.TipHub.Node.Length = self.headSizes[0]
		CATSpine.TipHub.Node.Width = self.headSizes[1]
		CATSpine.TipHub.Node.Height = self.headSizes[2]
		self.addFlatBones(spines[-1], CATSpine.TipHub)
		self.createTempTransform(spines[-1], CATSpine.TipHub.Node)
		if len(spines[-1].Children) > 0:
			self.parseHierarchy(spines[-1], CATSpine.TipHub, exclude + spines, maxDepth, depth + 1)
		return True

	def parseSpine(self, parentCAT, c, exclude, maxDepth, depth):
		spines = self.getSegmentJoints(c, self.spineNames, self.chestNames)
		spineboneLen = len(spines)
		if spineboneLen == 0:
			print("%s SPINES NOT FOUND....\n" % parentCAT.Name)
			return False
		parentCAT.AddSpine(NumBones=spineboneLen - 1)
		depth += spineboneLen
		CATSpine = parentCAT.Spines[-1]
		for b in range(CATSpine.NumBones):
			CATSpine.Bones[b].Node.Name = spines[b].Name
			segmentLength = self.boneLength(spines[b])
			CATSpine.Bones[b].Node.Length = segmentLength
			CATSpine.Bones[b].Node.Width = self.spineSizes[1]
			CATSpine.Bones[b].Node.Depth = self.spineSizes[2]
			self.addFlatBones(spines[b], CATSpine.Bones[b])
			self.createTempTransform(spines[b], CATSpine.Bones[b].Node)
			if len(spines[b].Children) > 0:
				self.parseHierarchy(spines[b], CATSpine.Bones[b], exclude + spines, maxDepth, depth + 1)
		CATSpine.TipHub.Name = spines[1].Name
		CATSpine.TipHub.Node.Name = spines[-1].Name
		CATSpine.TipHub.Node.Length = self.chestSizes[0]
		CATSpine.TipHub.Node.Width = self.chestSizes[1]
		CATSpine.TipHub.Node.Height = self.chestSizes[2]
		self.addFlatBones(spines[-1], CATSpine.TipHub)
		self.createTempTransform(spines[-1], CATSpine.TipHub.Node)
		if len(spines[-1].Children) > 0:
			self.parseHierarchy(spines[-1], CATSpine.TipHub, exclude + spines, maxDepth, depth + 1)
		return True

	def parseBone(self, parentCAT, c, exclude, maxDepth, depth):
		parentCAT.AddArbBone()
		currentARB = parentCAT.NumArbBones
		lastNode = parentCAT.GetArbBone(currentARB)
		self.delayedRename.append("$'{0}'.name = \"{1}\" \n".format(lastNode.Node.Name, c.Name))
		self.addFlatBones(c, lastNode)
		self.createTempTransform(c, lastNode.Node)
		boneLen = self.boneLength(c, 5)
		lastNode.Node.Length = boneLen
		if maxDepth > 0:
			perc = (float(depth) / float(maxDepth))
			lastNode.Node.Width -= ((lastNode.Node.Width * self.taperFactors) * perc)
			lastNode.Node.Depth -= ((lastNode.Node.Depth * self.taperFactors) * perc)
		self.parseHierarchy(c, lastNode, exclude, maxDepth, depth + 1)

	def initializeArmLimb(self, parentCAT, c):
		parentCAT.AddArm()
		armCAT = parentCAT.Limbs[-1]
		return (armCAT, c)

	def initializeLegLimb(self, parentCAT, c):
		parentCAT.AddLeg()
		legCAT = parentCAT.Limbs[-1]
		return (legCAT, c)

	def parseHierarchy(self, parentObject, parentCAT, exclude=[], maxDepth=0, depth=0):
		armlimbs = []
		legLimbs = []
		for c in parentObject.Children:
			if c in exclude:
				continue
			isLeg = False
			isArm = False
			thighName = self.findKeyword(c.Name.lower(), self.thighNames)
			armName = self.findKeyword(c.Name.lower(), self.upperarmNames)
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
			isTail = self.inArrayStrings(self.tailNames, c.Name)
			isNeck = self.inArrayStrings(self.neckNames, c.Name)
			isSpine = self.inArrayStrings(self.spineNames, c.Name)
			if isArm:
				armlimbs.append(self.initializeArmLimb(parentCAT, c))
			elif isLeg:
				legLimbs.append(self.initializeLegLimb(parentCAT, c))
			elif isTail:
				self.parseTail(parentCAT, c, exclude, maxDepth, depth)
			elif isNeck:
				self.parseNeck(parentCAT, c, exclude, maxDepth, depth)
			elif isSpine:
				self.parseSpine(parentCAT, c, exclude, maxDepth, depth)
			else:
				self.parseBone(parentCAT, c, exclude, maxDepth, depth)
		for a in armlimbs:
			self.parseArmJoints(a[0], parentCAT, a[1], exclude, maxDepth, depth)
		for l in legLimbs:
			self.parseLegJoints(l[0], parentCAT, l[1], exclude, maxDepth, depth)

	def transferBones(self, mesh, sourceBones, targetBones):
		MaxPlus.Core.EvalMAXScript("max modify mode")
		currentPose = [i.Transform for i in targetBones]
		MaxPlus.Core.EvalMAXScript("select (%s)" % "+".join([b.Name for b in sourceBones] + [mesh.Name]))
		bindpose = self.getBindPose(mesh)
		self.gotoBindPose(mesh, bindpose)
		for i in range(len(targetBones)):
			targetBones[i].Transform = sourceBones[i].Transform
		for x in mesh.Modifiers:
			if x.Name == "Skin":
				isCloned = MaxPlus.Core.EvalMAXScript("skinUtils.extractSkinData %s" % mesh.Name).GetBool()
				cloned = MaxPlus.INode.GetINodeByName("SkinData_" + mesh.Name)
				if isCloned:
					skinObject = x
					bones = MaxPlus.Core.EvalMAXScript("skinOps.GetBoneNodes %s" % skinObject.Name).GetINodeArray()
					boneorder = []
					b1 = len(bones)
					for s in range(b1):
						if bones[s] in sourceBones:
							boneIndex = sourceBones.index(bones[s])
						else:
							bname = bones[s].Name
							raise Exception("MISSING BONES IN SOURCE %s\n" % bname)
						boneorder.append(targetBones[boneIndex])
					for s in reversed(range(b1)):
						MaxPlus.Core.EvalMAXScript("skinOps.removeBone %s %s" % (skinObject.Name, bones[s].Name))
					bonesBefore = MaxPlus.Core.EvalMAXScript("skinOps.GetBoneNodes %s" % skinObject.Name).GetINodeArray()
					b3 = len(bonesBefore)
					if b3 > 0:
						raise Exception("%s Unable to remove bones there are %s remaining\n" % (mesh.Name, b3))
					for s in boneorder:
						MaxPlus.Core.EvalMAXScript("skinOps.addbone %s %s 0" % (skinObject.Name, s.Name))
					bonesAfter = MaxPlus.Core.EvalMAXScript("skinOps.GetBoneNodes %s" % skinObject.Name).GetINodeArray()
					b2 = len(bonesAfter)
					useMatchingName = self.skinTransferMatchByName
					if b1 != b2:
						print("There %s a difference in transferred bones from Original bone count of %s to %s Using Bone names for Transfer" % (mesh.Name, b1, b2))
						useMatchingName = True
					MaxPlus.Core.EvalMAXScript("select {%s, %s}" % (mesh.Name, cloned.Name))
					MaxPlus.Core.EvalMAXScript("skinUtils.ImportSkinDataNoDialog %s %s %s %s %s %s 0" % (
						useMatchingName, False, False, False, False, self.skinTransferThreshold))
					MaxPlus.Core.EvalMAXScript("delete %s" % cloned.Name)
		for i in range(len(targetBones)):
			targetBones[i].Transform = currentPose[i]
		for i in range(len(sourceBones)):
			sourceBones[i].Transform = currentPose[i]

	def inspect_Skin(self):
		numselected = len(MaxPlus.SelectionManager.GetNodes())
		if numselected > 0:
			selected = MaxPlus.SelectionManager.GetNode(0)
			objectType = selected.GetObject().GetSuperClassID()
			for x in selected.Modifiers:
				if x.Name == "Skin":
					skinObject = x
					print("%s = %s \n" % (selected.Name, x.Name))
					bones = MaxPlus.Core.EvalMAXScript("skinOps.GetBoneNodes %s" % skinObject.Name).GetINodeArray()
					for s in range(len(bones)):
						print("%s\t%s\n" % (s, bones[s].Name))
						try:
							MaxPlus.Core.EvalMAXScript("skinOps.removeBone %s %s" % (skinObject.Name, bones[s].Name))
						except:
							print("%s Failed to remove %s\n" % (s, bones[s].Name))

	def addFlatBones(self, bone, catbone):
		self.flatBoneList.append(bone)
		self.flatCATBones.append(catbone.Node)

	def get_skinned_meshes(self, boneNeedles):
		skinned_meshes = []
		for obj in MaxPlus.Core.GetRootNode().Children:
			if obj.GetObject().GetSuperClassID() in [MaxPlus.SuperClassID().GeometryClass, MaxPlus.SuperClassID().ShapeClass]:
				for x in obj.Modifiers:
					if x.Name == "Skin":
						skin_modifier = x
						bones = MaxPlus.Core.EvalMAXScript("skinOps.GetBoneNodes %s" % skin_modifier.Name).GetINodeArray()
						for i in range(len(bones)):
							bone = bones[i]
							if bone in boneNeedles:
								skinned_meshes.append(obj)
								break
		return skinned_meshes

	def getBindPose(self, mesh):
		transformmatrixes = []
		for x in mesh.Modifiers:
			if x.Name == "Skin":
				skin_modifier = x
				bones = MaxPlus.Core.EvalMAXScript("skinOps.GetBoneNodes %s" % skin_modifier.Name).GetINodeArray()
				for b in range(len(bones)):
					matrix = MaxPlus.Core.EvalMAXScript("skinUtils.GetBoneBindTM %s %s" % (mesh.Name, bones[b].Name)).GetMatrix()
					transformmatrixes.append(matrix)
		return transformmatrixes

	def gotoBindPose(self, mesh, matrixArray):
		for x in mesh.Modifiers:
			if x.Name == "Skin":
				skin_modifier = x
				bones = MaxPlus.Core.EvalMAXScript("skinOps.GetBoneNodes %s" % skin_modifier.Name).GetINodeArray()
				for b in range(len(bones)):
					bones[b].Transform = matrixArray[b]

	def selectReturnToBindPose(self):
		numselected = len(MaxPlus.SelectionManager.GetNodes())
		selectedRootBone = None
		self.skinnedObjects = []
		for s in range(numselected):
			mesh = MaxPlus.SelectionManager.GetNode(s)
			pose = self.getBindPose(mesh)
			self.gotoBindPose(mesh, pose)

	def create_CAT_from_Bones(self):
		self.flatBoneList = []
		self.flatCATBones = []
		numselected = len(MaxPlus.SelectionManager.GetNodes())
		selectedRootBone = None
		self.skinnedObjects = []
		for s in range(numselected):
			if MaxPlus.SelectionManager.GetNode(s).GetObject().GetClassID() == MaxPlus.Class_ID(8872500, 0):
				selectedRootBone = MaxPlus.SelectionManager.GetNode(s)
		if selectedRootBone is not None:
			# Create CATParent and capture its name
			MaxPlus.Core.EvalMAXScript("global catParentObj = CATParent(); catParentObj.name")
			fp_value = MaxPlus.Core.EvalMAXScript("catParentObj.name")			
			cat_parent_name = fp_value.Get()  # Get the name as a string			
			CATParentObj = MaxPlus.INode.GetINodeByName(cat_parent_name)
			if CATParentObj is None:
				print("Failed to create CATParent!\n")
				return False

			rootname = selectedRootBone.Name
			# Configure CATParent properties
			MaxPlus.Core.EvalMAXScript("catParentObj.CATUnits = 1")
			MaxPlus.Core.EvalMAXScript("catParentObj.CATName = \"{0}\"".format(self.CATName))
			MaxPlus.Core.EvalMAXScript("catParentObj.LengthAxis = \"{0}\"".format(self.lengthAxis))
			
			# Set rotation using MAXScript
			if self.lengthAxis == "X":
				MaxPlus.Core.EvalMAXScript("catParentObj.rotation = (eulerAngles 180 -90 0) as quat")
				if self.moveBaseToCharacter:
					newPos = selectedRootBone.Position
					newPos.Z = 0
					CATParentObj.Position = newPos
			if self.lengthAxis == "Z":
				MaxPlus.Core.EvalMAXScript("catParentObj.rotation = (eulerAngles 180 90 0) as quat")
				if self.moveBaseToCharacter:
					newPos = selectedRootBone.Position
					newPos.X = 0
					CATParentObj.Position = newPos

			# Add a hub
			MaxPlus.Core.EvalMAXScript("catParentObj.AddHub()")
			fp_value = MaxPlus.Core.EvalMAXScript("catParentObj.Node.RootHub")
			pelvisHUB = fp_value.Get()#CATParentObj.RootHub()						
			
			MaxPlus.Core.EvalMAXScript("{}.Node.Length={}".format(pelvisHUB,self.hipSizes[0]))#pelvisHUB.Node.Length = self.hipSizes[0]
			MaxPlus.Core.EvalMAXScript("{}.Node.Width={}".format(pelvisHUB,self.hipSizes[1]))#pelvisHUB.Node.Width = self.hipSizes[1]
			MaxPlus.Core.EvalMAXScript("{}.Node.Height={}".format(pelvisHUB,self.hipSizes[2]))#pelvisHUB.Node.Height = self.hipSizes[2]
			arraynodes = CATParentObj.CATRigNodes
			rootNode = arraynodes[1]
			rootNode.Name = rootname
			maxDepth = self.maxHierarchyDepth(selectedRootBone, 0)
			self.addFlatBones(selectedRootBone, pelvisHUB)
			self.createTempTransform(selectedRootBone, rootNode)
			self.parseHierarchy(selectedRootBone, pelvisHUB, [], maxDepth)
			for d in self.delayedRename:
				try:
					MaxPlus.Core.EvalMAXScript(d)
				except:
					print("Unable to Rename [%s]\n" % d)
			self.skinnedObjects = self.get_skinned_meshes(self.flatBoneList)
			if self.moveSkinsToCAT:
				for m in range(len(self.skinnedObjects)):
					print(" Transfering Skinning to %s\n" % self.skinnedObjects[m].Name)
					self.transferBones(self.skinnedObjects[m], self.flatBoneList, self.flatCATBones)
			if self.deleteOldBones:
				if len(self.skinnedObjects) > 0:
					if not self.moveSkinsToCAT:
						print("Cannot Delete Original Skeleton, it is Currently in Use")
					else:
						for b in self.flatBoneList:
							MaxPlus.Core.EvalMAXScript("delete %s" % b.Name)
				else:
					for b in self.flatBoneList:
						MaxPlus.Core.EvalMAXScript("delete %s" % b.Name)
			if self.CATBoxModeDisplay:
				for b in self.flatCATBones:
					b.BoxMode = True
			print("Skeleton 2 CAT Completed\n")
			return True
		else:
			print("Need A Bone selected!\n")
			return False
		return False