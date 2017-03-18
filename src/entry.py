'''
Created on 2017. 3. 18.

@author: Byungchul
'''

from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'


if(__name__ == '__main__'):
    app.run()