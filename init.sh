#!/bin/bash
soffice --calc --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager" & # & leaves the process running in the background
echo "Please wait before calc finishes loading"
sleep 5     # If the script is run before LibreOffice is fully loaded, we run into error AttributeError: 'NoneType' object has no attribute 'CurrentController'
echo "Copy and Paste the script to be read"
ls Scripts/
#read script_name
#python3.7 Scripts/${script_name}
python3.7 Scripts/game_of_life.py