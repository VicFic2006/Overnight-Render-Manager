import os
from time import sleep

print("Executing the Overnight Render script...")
sleep(0.5)
print("©2020 Varghese K. James.")
print(" ")

print('Enter the path to the folder in which your file is located')
loc = input('/home/user/Desktop/Blender Stuff/')
os.chdir('/home/user/Desktop/Blender Stuff/'+loc)
print(" ")

print('Which file do you want to render?')
os.system('ls *.blend')
render = input('Enter the name')

renderType = input("Animation(a) or Single Frame(sf)?")
while True:
    if renderType == 'sf':
        print("Rendering frame 1 of "+render)
        print(" ")
        os.system('blender -b '+render+' -f 1')
        break

    elif renderType == 'a':
        print("Rendering animation of "+render)
        print(" ")
        os.system('blender -b '+render+' -a')
        break

    else:
        print('ERROR: Choose either sf or a')

print('Rendering Complete')
os.system('notify-send "Rendering '+render+' Complete" "Shutting Down in 30 sec"')
sleep(30)
print("SHUTTING DOWN")
#os.system(poweroff)
