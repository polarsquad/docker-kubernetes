from flask import Flask
app = Flask(__name__)

@app.route('/')
# Serving Flask
def hello():
    return "Hello World!\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)