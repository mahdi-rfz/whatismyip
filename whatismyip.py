import requests

URL = ("http://localhost:6263/whatismyip")


def checkInternteConnection():
    r = requests.get("https://google.com")
    return r.ok

def receiveIp():
    responce = requests.get(URL)
    return (eval(responce.text)["ip"])
    
def artText():
    return(""" █   █ █ █▄ ▄█ █ █▀▄
 ▀▄▀▄▀ █ █ ▀ █ █ █▀ 
""")



print(artText())
print(f"IP : {receiveIp()}")