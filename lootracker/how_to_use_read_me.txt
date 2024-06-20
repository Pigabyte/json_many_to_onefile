1) Make sure you have a 3.2+ Version of Python (Latest if Possible)
https://www.python.org/downloads/
2) Press: Windows Key + R 
3) Type: .runelite (Press Enter)
4) Open the Folder 'loots'npc', select your profile '
5) Copy all the files in the folder 'npc' to the folder 'lootracker'
6) Run the File 'Convert.bat' in 'lootracker' folder
(it's in the middle of all the other files). 
7) Press: Windows Key + R 
8) Type: HDOS (Press Enter)
9) Open the Folder 'Profiles' and then open the file 'loot_tracker.json'
10) Open the file 'FileGenerated.json' in the folder 'lootracker'
(it's in the middle of all the other files).
11) Right Click -> Select All -> Copy
12) Delete the contents in the file 'loot_tracker.json'
13) Paste the content from file 'FileGenerated.json'in to file 'loot_tracker.json' and save.
14) Go back to HDOS Client
15) Press: Shift Twice Quickly
16) Type: Loot Tracker 
17) Deactivate and Activate the plugin
18) At this point you should have all your Loot from Runelite in HDOS.
19) Tip: Scroll the Tracker Up and Down using the scroll bar in the right of the Tracker.
(HDOS tracker is very buggy at the moment)


P.S: The plugin itself has insane memory leaks, so my recommendation would be to go through the list
and reseting all the trash monsters/using this only for certain bosses, otherwise your FPS will go dramatically down).

WARNING: The reset functions are insanely buggy, if you can't reset the plugin,
just delete the file 'loot_tracker.json' and deactivate/active the plugin.
Seems to be the best way to go back to a clean state.


----------------------------------------------
If I have time, I will make a v2 for this script where you can choose between all the bosses 
which ones you want to import
to HDOS, so you aren't forced to get a full log.

7/2/2022 - Pigabyte