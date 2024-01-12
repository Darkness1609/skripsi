from flask import Flask, request, render_template
from datetime import datetime
import json
from model import  predict_diseases

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def fitur():
    if request.method == 'POST':
        print(request.form.getlist('mycheckbox'))
        hasil = predict_diseases(request.form.getlist('mycheckbox'))
        return render_template('result.html', penyakit=hasil)



@app.route("/about/")
def about():
    return render_template("about.html",)

@app.route("/turtle")
def turtle():
    data = []
    with open('static\data.json') as file:
        data = json.load(file)
        print(data)
        return render_template(    
            "penyu.html",
            penyu = data
    )


    
if __name__ == "__main__":
    app.run(debug=True)