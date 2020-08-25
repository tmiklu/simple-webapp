import os
from flash import Flask
app = Flask(__name__)

@app.route("/")
def main():
	return "Welcome!"

@app.route('/how are you')
def hello():
	return 'I'm good, how about you?'

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
