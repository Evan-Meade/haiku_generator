from flask import Flask
from haiku.write import Writer


app = Flask(__name__)

writer = Writer()

from haiku import routes