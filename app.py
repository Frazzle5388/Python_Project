from flask import Flask, render_template

from controllers.cities_controller import cities_blueprint
from controllers.pubs_controller import pubs_blueprint

app = Flask(__name__)

app.register_blueprint(cities_blueprint)
app.register_blueprint(pubs_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
