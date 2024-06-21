import os

"""
run as sudo

you can use this script on unix base os


before run this script , update whatismyip directory
"""

os.system("rm /bin/whatismyip")

current_dir = input("Enter current directory :")
script = ("cp whatismyip /bin")
os.system(script)

print("The whatismyip script was update in bin dir")