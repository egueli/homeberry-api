#!/home/pi/homeberryApi/bin/python
from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

@app.route("/")
def helloWorld():
	return "Hello World\n"

@app.route("/nordvpn")
def switchNordVpnCountry():
	country = request.args.get('country')
	subprocess.run(["sudo", "/home/pi/switch.sh", country], check=True)
	return f"Switching to NordVPN server with country '{country}'"

@app.route("/shutdown")
def shutdown():
	subprocess.run("sudo shutdown -h now".split())
	return "Shutting down Raspberry"

@app.route("/reboot")
def reboot():
	subprocess.run("sudo shutdown -r now".split())
	return "Restarting Raspberry"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

