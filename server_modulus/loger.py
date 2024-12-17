import datetime


def loger(ip , userAgent):
    try : 
        with open("whatismyip-logfile.txt" , "a") as file :
            file.write(f"\nIP : {ip} , TIME : {datetime.datetime.now()} , User_Agent : {userAgent}")
            file.close
            return True
    except Exception : 
        return False