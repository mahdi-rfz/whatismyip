import os

"""
run as sudo

you can use this script on unix base os
"""
os.system("pip install pyinstaller")

os.system("pip install requests")

os.system("pip install colorama")

os.system("pyinstaller --onefile whatismyip.py")


script = ("cp dist/whatismyip /bin")
os.system(script)

print("The whatismyip script was copied in bin dir")