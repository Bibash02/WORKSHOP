# Create the app
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return "Welcome to the Student Performance App!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)