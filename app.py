from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Run the app on 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
