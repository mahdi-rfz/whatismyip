#use requests for http request for receive ip and ip info function
import requests
#use socket for check internet connection and check server status
import socket
#use json for parse in parameters in ip receive function
import json
#use argparse for parse in inputs
import argparse
#use sys only for sys.exit()
import sys
#use sqlite for save host url on client
import sqlite3
#use getpass for find client username for save on system
import getpass
#use os to diagnose os 
import os


class dbController:
    """
    class dbController id define for controll all 
    parameter on data base ex.username and password 
    """
    def __init__(self , url = "http://127.0.0.1:6263"):
        self.url = url


    def checkSaver():
        if os.name == "nt":
            #if os.name == "nt" the client os is windows

            try : 
                os.mkdir(f"C:/Users/{getpass.getuser()}/whatismyip")
            except : 
                pass
            finally : 
                os.chdir(f"C:/Users/{getpass.getuser()}/whatismyip")
        else : 
            try : 
                os.mkdir(f"/home/{getpass.getuser()}/.whatismyip")
            except : 
                pass
            finally : 
                os.chdir(f"/home/{getpass.getuser()}/.whatismyip")




    def setUrl(self):
        dbController.checkSaver()
        def _createTable():
            """
            for create table on url.db file with one column (url)
            """
            conn = sqlite3.connect("url.db")
            cursor = conn.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS url(url)")
            conn.commit()
            conn.close()
        _createTable()
        try : 
            conn = sqlite3.connect("url.db")
            cursor = conn.cursor()

            cursor.execute("INSERT INTO url VALUES(?)" ,(self.url,))
            conn.commit()
            conn.close()
            
            return True
        except Exception : 
            return False
        


    def readUrl(self):
        dbController.checkSaver()
        def _createTable():
            conn = sqlite3.connect("url.db")
            cursor = conn.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS url(url)")
            conn.commit()
            conn.close()
        _createTable()
        try : 
            conn = sqlite3.connect("url.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM url")
            
            data = cursor.fetchall()

            if len(data) == 0:
                return False
            else : 
                return (data[-1])
        except Exception as e: 
            return False








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
            socket.create_connection((serverIp , int(serverPort)))
            return True
        except Exception as e : 
            return False
        

    def receiveClientIp(serverIp , serverPort):
        ip = requests.get(f"http://{serverIp}:{serverPort}/whatismyip")
        return json.loads((ip.text))["ip"]
        
    
    def checkIpInfo(clientIp):
        info = requests.get(f"http://ip-api.com/json/{clientIp}")
        return json.loads((info.text))
    



    def splitUrlAndPort(url):
        """
        function work flow : 
            input -> http://127.0.0.1:6263
            output -> [127.0.0.1 , 6263]
        """
        url = list(url)
        counter = 0 
        while True :
            if url[counter] == ":":
                url[counter] = "&"
                break
            counter = counter + 1

        allch = ""

        for ch in url : 
            allch = allch + ch
        allch = allch.replace("//" , "*")
        
        url = allch[allch.index("*") + 1:allch.index(":")]
        port = allch[allch.index(":") + 1:]
        return [url , port]
        











parser = argparse.ArgumentParser(description='whatIsMyIp')

parser.add_argument("-i" , type = str , help = "input ip")
parser.add_argument('-v', action='store_true', help='verbose')
parser.add_argument("--set_url" , type = str , help = "set url")

args = parser.parse_args()




if dbController().readUrl() == False : 
    SERVER_IP = None
    SERVER_PORT = None
else : 
    SERVER_IP = Tool.splitUrlAndPort(dbController().readUrl()[0])[0]
    SERVER_PORT = Tool.splitUrlAndPort(dbController().readUrl()[0])[1]





if args.set_url != None:
    dbController(args.set_url).setUrl() 
    print("your url set on data base")
    sys.exit()

if Tool.checkInternetConnection() == False :
    print(Tool.artText())
    print("Check your internet connection")
    sys.exit()






if args.i != None : 
    print(Tool.artText())
    info = Tool.checkIpInfo((args.i).strip())
    for i in info:
        print(f"{i} : {info[i]}")

elif args.v == True : 
    print(Tool.artText())
    info = Tool.checkIpInfo(Tool.receiveClientIp(SERVER_IP , SERVER_PORT))
    for i in info:
        print(f"{i} : {info[i]}")


else : 
    if Tool.checkServerStatus(SERVER_IP , SERVER_PORT) == False:
        print(Tool.artText())
        print(f"HOST with ip : {SERVER_IP} & port : {SERVER_PORT} is down")
        sys.exit()

    print(Tool.artText())
    ip = (Tool.receiveClientIp(SERVER_IP , SERVER_PORT))
    print(f"IP : {ip}")
    info = (Tool.checkIpInfo(ip))
    print(f"Country : {info["country"]}")
    print(f"City : {info["city"]}")
    print(f"ISP : {info["isp"]}")
