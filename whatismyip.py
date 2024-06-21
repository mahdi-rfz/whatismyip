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

def streetmap_link(latitude , longitude , zoom  = 15):
        base_url = "https://www.openstreetmap.org/"
        link = f"{base_url}?mlat={latitude}&mlon={longitude}&zoom={zoom}"
        return link

data = ip_receive()
    
print(""" █   █ █▄█ ▄▀▄ ▀█▀ █ ▄▀▀ █▄ ▄█ ▀▄▀ █ █▀▄
 ▀▄▀▄▀ █ █ █▀█  █  █ ▄██ █ ▀ █  █  █ █▀ 
""")

print(Fore.LIGHTBLACK_EX + """    Ip :""" , Fore.WHITE + data["IPv4"])
print(Fore.LIGHTBLACK_EX + """    Country code :""" , Fore.WHITE + data["country_name"])
print(Fore.LIGHTBLACK_EX + """    Latitude :""" , Fore.WHITE + str(data["latitude"]))
print(Fore.LIGHTBLACK_EX + """    Longitude :""" , Fore.WHITE + str(data["longitude"]))
print(Fore.LIGHTBLACK_EX + """    OpenStreetMap Link :""" , Fore.WHITE + streetmap_link(data["latitude"] ,data["longitude"]))
print()