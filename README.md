
![Skeleton2CAT-Title](https://github.com/user-attachments/assets/a97af5af-7818-45e9-a8c2-3569a0201061)

# Skeleton2CAT for 3DSMAX 2024-2026
Converts basic skeleton heirarchy to 3dsmax CAT Rig
Supports 3dsmax 2024 to Later

# What is this used for?
  This is for imported 3D models from FBX or existing skeletal skinned models that are not CAT rigged.

# Functions and Features include:

+ Go to bind pose (skeleton or CATrig)
+ Move Weights from Skeleton to newly Generated CATrig (Any mesh skinned to the bone will be transitioned)
+ Convert Skeleton Structure to CAT Rig
+ Some support for fixing incorrect names like having the same names for UpperArm/Forearms and Thigh/Calfs
+ Any non CATbone rig bones are converted to AARP CATbones.

 
# Installation:
   Unzip to any folder or check out the repository. find the file **Installer_DragNDrop.ms**
   Drag and Drop the **Installer_DragNDrop.ms** to 3dsmax viewport
   
   To create Shortcut Right click the Tool bar and Click Customize,
   Go to "Tool Bars" Under Category Search for __Shinobubu__
   now drag and drop each icon to your desired tool bar location.

# Toolbar Icons:
![Icon_SK2CAT](https://github.com/user-attachments/assets/fffe25a4-9fce-44d9-87e3-3d9f0952664f)![Icon_SK2CAT_gotobindpose](https://github.com/user-attachments/assets/8ac8119f-f29b-40be-9723-4d358c4cc903)



# Instructions:
For Skeleton Conversion:
  Press 'X' and search for "Skeleton 2 CATrig" or use icon shortcut
  Select the root bone to convert (Not Parent or Group) and click Apply.
  
For Returning to Bind Pose
  Select the Mesh , Press 'X' and search for "Go To Bind Pose' or use the Icon

# Conversion Guidelines
For best results make sure the skeleton is using names commonly used by CATrig
+ Spine chains need to end with a HUB bone (Chest)
+ Neck chains need to end with a Head bone
+ For legs that are digitigrade make sure the 3rd limb has the correct name

Use the preset of bone names associated with limbs

![3dsmax_sUMEs7nmw5](https://github.com/user-attachments/assets/0dd107eb-c8b0-49db-b0ce-ac97ab42fad6)

# Trouble Shooting
Go to Bind Pose

CAT Rig's have very sticky IK/FK (Even with the FK value set to 1) algorithms and it may look broken on the first attempt at returning to Bind Pose. 

__Solution:__
      
      Repeatedly using the function will eventually bring the bones back to its bind pose. 
