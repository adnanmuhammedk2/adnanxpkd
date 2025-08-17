from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Tech VJ'

@app.route('/redirect')
def redirect_page():
    return render_template('blogspot.html')

@app.route('/countdown')
def countdown_page():
    return render_template('countdownblog.html')

@app.route('/player')
def player_page():
    return render_template('videoplayer.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
