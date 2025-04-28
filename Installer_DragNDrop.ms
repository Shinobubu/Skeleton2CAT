/*
==========================================================================
Folder Structure
==========================================================================
+ /<Main Script Folder>/

	+ /<Main Script Folder>/icons
		- /<Main Script Folder>/icons/skeleton2Cat_16a.bmp
		...
	+ /<Main Script Folder>/scripts
		- /<Main Script Folder>/SCAT2_Loader.py
		...
	- Installer_DragNDrop.mse
	
==========================================================================
*/


--Adjust this part
script_name = "Skeleton 2 CAT"
script_folder_name = "\\Skeleton2CAT\\"

--End of adjust

script_path = getThisScriptFilename()
this_script_path = getfilenamepath script_path
icons_folder = "\\icons\\"

--format "Script DIR : %\n" this_script_path

--macroscript
fn create_macro_script=
(	
	macroScript SK2CAT
	Category:"Shinobubu" 
	toolTip:"Skeleton To CAT"
	icon: #("Icon_SK2CAT",1)

	(
		python.ExecuteFile ((GetDir #userScripts) + "\\Shinobubu\\" + "\\Skeleton2CAT\\" +  "S2CAT_Loader.py")
	)					
	macroScript G2BindPose
	Category:"Shinobubu" 
	toolTip:"Go To Bind Pose"
	icon: #("Icon_SK2CAT_gotobindpose",1)

	(
		python.ExecuteFile ((GetDir #userScripts) + "\\Shinobubu\\" + "\\Skeleton2CAT\\" +  "gotoBindPose.py")
	)
)

--Copy icons
icon_file_list = getfiles (this_script_path + icons_folder + "\\*.bmp")

for o in icon_file_list do
(
	copyFile (o) ((GetDir #userIcons) + "\\" + (filenameFromPath o))
	
)


--Create Shinobubu directory
makeDir ((GetDir #userScripts) + "\\Shinobubu\\" + script_folder_name)

--Remove the previous files of this script
destination_path = getFiles ((GetDir #userScripts) + "\\Shinobubu\\" + script_folder_name + "\\*.*" )

for item in destination_path do
(
	try(deleteFile item) catch()
)


--Get all scripts in 'scripts' folder + Copy them
all_scripts = getFiles (this_script_path  + "\\*.py" )

for item in all_scripts do
(
	copyFile item ((GetDir #userScripts) + "\\Shinobubu\\" + script_folder_name + filenameFromPath item)
)


create_macro_script()
colorMan.reInitIcons()
messageBox ("Install success!\n\nTo use: \nRight click on the tool bar > Customize...\nChoose category \"Shinobubu\"\nDrag \" " + script_name + " \" to the toolbar where you want.\n\nTo use Command press X and search 'Skeleton 2 CAT' or 'Go to Bind Pose'")

