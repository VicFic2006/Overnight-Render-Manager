#!/bin/sh

# THIS SCRIPT NEEDS MODIFICATION.

echo "Executing the Overnight Render script..."
sleep 0.5
echo "©2020 Varghese K. James." && echo " "
cd Desktop/ && cd Blender\ Stuff/

echo "Make sure you have set the output path and other render settings before continuing"
echo " " && ls
echo "Which file do you want to render? (Only .blend files are compatible)"
read RENDER

echo "Animation(a) or Single frame?(sf)"

while :
do
  read INPUT_STRING
  case $INPUT_STRING in
	sf)
		echo "Rendering frame 1 of $RENDER" && echo " "
		blender -b $RENDER -f 1
		break
		;;
	a)
		echo "Rendering animation of $RENDER" && echo " "
		blender -b $RENDER -a
		break
		;;
	*)
		echo "ERROR: Choose either sf or a"
		;;
  esac
done

echo "Rendering Complete"
notify-send "Rendering $RENDER Complete" "Shutting Down in 30 sec"
echo "Initiating shutdown sequence in 30 sec (Click Ctrl + C to Abort)"
sleep 30
echo " "
echo "SHUTTING DOWN"
poweroff
