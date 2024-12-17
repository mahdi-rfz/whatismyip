import requests
import socket
import json
import argparse
import sys



SERVER_IP = "46.100.60.199"
SERVER_PORT = 6263


class Tool:

    def artText():
        return(""" █   █ █ █▄ ▄█ █ █▀▄
 ▀▄▀▄▀ █ █ ▀ █ █ █▀ 
""")


    def checkInternetConnection():
        """
        Check internet connection with www.google.com:80
        if internet connection is ok : return true
        else : return false
        """
        try : 
            socket.create_connection(("www.google.com" , 80))
            return True
        except Exception : 
            return False
        

    def checkServerStatus(serverIp , serverPort):
        """
        check server status with socket connection

        if server is up : return true
        else : return false
        """
        try : 
            socket.create_connection((serverPort , int(serverPort)))
            return True
        except Exception : 
            return False
        

    def receiveClientIp(serverIp , serverPort):
        ip = requests.get(f"http://{serverIp}:{serverPort}/whatismyip")
        return json.loads((ip.text))["ip"]
        
    
    def checkIpInfo(clientIp):
        info = requests.get(f"http://ip-api.com/json/{clientIp}")
        return json.loads((info.text))
        




parser = argparse.ArgumentParser(description='whatIsMyIp')

parser.add_argument("-i" , type = str , help = "input ip")
parser.add_argument("-n" , type = str , help = "client ip")

args = parser.parse_args()





if Tool.checkInternetConnection() == False :
    print(Tool.artText())
    print("Check your internet connection")
    sys.exit()
elif Tool.checkServerStatus(SERVER_IP , SERVER_PORT):
    print(Tool.artText())
    print(f"HOST with ip : {SERVER_IP} & port : {SERVER_PORT} is down")
    sys.exit()






if args.i != None : 
    print(Tool.artText())
    info = Tool.checkIpInfo(args.i)
    for i in info:
        print(f"{i} : {info[i]}")
else : 
    print(Tool.artText())
    ip = (Tool.receiveClientIp(SERVER_IP , SERVER_PORT))
    print(f"IP : {ip}")
    info = (Tool.checkIpInfo(ip))
    print(f"Country : {info["country"]}")
    print(f"City : {info["city"]}")
    print(f"ISP : {info["isp"]}")
