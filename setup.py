import os

"""
run as sudo

you can use this script on unix base os
"""
##add pip installer
current_dir = input("Enter current directory :")
script = ("cp whatismyip /bin")
os.system(script)

print("The whatismyip script was copied in bin dir")