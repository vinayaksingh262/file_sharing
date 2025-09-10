import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

PORT = 8010
#use userprofile on windows, home on linux/mac
user_home = os.environ.get("USERPROFILE") or os.environ.get("HOME")
onedrive_path = os.path.join(user_home, "OneDrive")
desktop = onedrive_path if os.path.exists(onedrive_path) else user_home
os.chdir(desktop)

Handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8)
webbrowser.open("myqr.svg")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
    httpd.serve_forever()
