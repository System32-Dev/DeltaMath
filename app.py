
from http.server import BaseHTTPRequestHandler, HTTPServer
from g4f.client import Client
import re

client = Client()

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Headers", "X-Question")
        self.send_header("Access-Control-Allow-Headers", "X-Unit")
        self.end_headers()
        # self.processRequest()
            
    def do_GET(self):
        print("hi")
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        equation = self.headers.get('X-Question')
        unit = self.headers.get('X-Unit')
        
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content":
                "I am currentlly working on " + unit + ". Can you please solve " + equation + ". Remember to put the answer in quotation marks."
            }]
        )

        self.wfile.write(bytes(re.findall('"([^"]*)"', response.choices[0].message.content)[0], encoding='utf8'))

class app:
    def __init__(w, x, r):
        print("app")
    
    def run():
        webServer = HTTPServer((hostName, serverPort), MyServer)
        print("Server started http://%s:%s" % (hostName, serverPort))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")
        
if __name__ == "__main__":        
    app.run()
