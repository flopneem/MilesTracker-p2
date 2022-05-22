# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from flask import Flask

app = Flask(__name__)

#Hello path
@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/my')
def my():
    return "Hello again."

@app.route('/myPath')
def myPath():
    return "Hello Path."

if __name__ == '__main__':
   app.run()

