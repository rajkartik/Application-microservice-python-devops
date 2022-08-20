from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import socket
app=Flask(__name__)
# function fetch ip address and name of the machine python
@app.route('/') 
def index():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return render_template('index.html', hostname=hostname, ip=ip)



# @app.route('/')
# def hello_world():
#     return render_template('index.html')

@app.route('/health')
def health():
    return jsonify(
        status="OK"
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)