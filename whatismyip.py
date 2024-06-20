import requests
from colorama import Fore


def ip_receive():
    try :
        request_url = 'https://geolocation-db.com/jsonp/' 
        response = requests.get(request_url)
        response = response.text
        response = response.replace("callback(" , "")
        response = response.replace(")" , "")
        response = response.replace("null" , "False")
        
        return eval(response)
    
    except OSError :
        return " Not found"
    
    
data = ip_receive()
    
print(""" █   █ █▄█ ▄▀▄ ▀█▀ █ ▄▀▀ █▄ ▄█ ▀▄▀ █ █▀▄
 ▀▄▀▄▀ █ █ █▀█  █  █ ▄██ █ ▀ █  █  █ █▀ 
""")

print(Fore.LIGHTBLACK_EX + """    Ip :""" , Fore.WHITE + data["IPv4"])
print(Fore.LIGHTBLACK_EX + """    Country code :""" , Fore.WHITE + data["country_name"])
print(Fore.LIGHTBLACK_EX + """    Latitude :""" , Fore.WHITE + str(data["latitude"]))
print(Fore.LIGHTBLACK_EX + """    Longitude :""" , Fore.WHITE + str(data["longitude"]))
