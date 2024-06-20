import requests
import colorama
import os 

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
    

print(ip_receive())