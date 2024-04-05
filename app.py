
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, request, Response
from g4f.client import Client
from flask_cors import CORS
import re

client = Client()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_HEADERS'] = 'X-Unit'
app.config['CORS_HEADERS'] = 'X-Question'


@app.route('/')
def home():
    resp = Response("Error", 200)
    
    equation = request.headers.get('X-Question')
    unit = request.headers.get('X-Unit')
        
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content":
            "I am currentlly working on " + unit + ". Can you please solve " + equation + ". Remember to put the answer in quotation marks."
        }]
    )

    resp.set_data(re.findall('"([^"]*)"', response.choices[0].message.content)[0])
    
    return resp

if __name__ == "__main__":
    app.run()
