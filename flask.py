#Required modules
from flask import Flask

#Creating Instance for App
app = Flask(__name__)

#Route
@app.route('/')
def hello_world():
    return 'Hello, World!'
    #will display in browser

#For Running App for standalone
if __name__ == "__main__":
    app.run()

#it runs in localhost as "http://127.0.0.1:5000/" or "http://localhost:5000/"
