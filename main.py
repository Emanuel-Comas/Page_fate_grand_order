from flask import Flask, render_template

# http://127.0.0.1:5000/
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
