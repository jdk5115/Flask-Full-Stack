from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return ('Hello World!!!'), 200

if __name__ == '__main__':
    app.run(port= 8000, debug= True)