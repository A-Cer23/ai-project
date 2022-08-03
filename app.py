from flask import Flask, render_template
from forms import AccidentForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def index():
    form = AccidentForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)




# todo: index page displays form / get which model and the data to predict with
# todo: prediction route to display the model's prediction