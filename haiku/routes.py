from haiku import app, writer
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
def home():
    haiku = writer.gen_haiku(5, 7, 5)
    return render_template('home.html', haiku=haiku)