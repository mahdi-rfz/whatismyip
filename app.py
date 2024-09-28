from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route("/whatismyip" , methods = ["GET" , "POST"])
def whatIsMyIp():
    return jsonify({"ip":request.remote_addr})

if (__name__) == ("__main__"):
    app.run(debug=True , host="localhost" , port=6263)