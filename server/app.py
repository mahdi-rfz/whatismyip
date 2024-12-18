from flask import Flask , request , jsonify
import socket
import server_modulus.loger as loger

app = Flask(__name__)

@app.route("/whatismyip" , methods = ["GET" , "POST"])
def whatIsMyIp():
    loger.loger(request.remote_addr , request.user_agent)
    return jsonify({"ip":request.remote_addr})



if (__name__) == ("__main__"):
    app.run(host = socket.gethostbyname(socket.gethostname()) , port = 6263)