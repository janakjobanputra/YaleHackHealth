from flask import Flask, render_template, send_from_directory
# from scripts import annotations


app = Flask(__name__, static_url_path='/static')


# Home page
@app.route('/')
def home():
    message = 'Welcome to Jar-Gone'
    return render_template('/index.html', message=message)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)