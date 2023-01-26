from flask import Flask

app = Flask(__name__)


@app.route('/')
def page_index():
    return 'main page'


app.run()
