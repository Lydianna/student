#!/usr/bin python3
from flask import Flask

app = Flask(__name__)

def haha():
    return 'Xixi'

if __name__ == '__main__':
    app.debug = True
    print('hello')
    app.run()
