import os

"""
run as sudo

you can use this script on unix base os
"""

current_dir = input("Enter current directory :")
script = ("cp whatismyip /bin")
os.system(script)