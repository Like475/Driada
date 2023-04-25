""" Required for deployment in repl.it """
from threading import Thread
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return ''


def run():
    app.run(host='0.0.0.0', port=80)


def keep_alive():
    keep_alive_thread = Thread(target=run)
    keep_alive_thread.start()
