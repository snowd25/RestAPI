from flask import Flask

#create object of Flask with unique name
app = Flask(__name__)

#create route with just '/' to access homepage
@app.route('/')
def home():
	return "Hello World"

app.run(port = 4000)

#Now type this in browser http://127.0.0.1:4000/
