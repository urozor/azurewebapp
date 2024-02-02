from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Working!!!! :)\n Test 2 to check automatism'

if __name__ == '__main__':
    app.run(debug=True)
    