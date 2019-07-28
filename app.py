from flask import Flask, render_template, request
from data import DataHarvester
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
import requests

response = requests.get("https://app.wordstream.com/services/v1/wordstream/interview_data")
dataObject = DataHarvester(response)


app = Flask(__name__)
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

    @app.route("/", methods=['GET', 'POST'])
    def index():
        return render_template('home.html')
    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/datasets')
    def datasets():
        return render_template('datasets.html', returnData = dataObject.createMeasurementList())

    @app.route('/dataset/<string:id>/')
    def dataset(id):
        try:
            results = dataObject.sort(dataObject.createMeasurementList(id),'name')
        except:
            results = dataObject.sort(dataObject.createMeasurementList(id))
        return render_template('dataset.html', selectedData = results, id=id)

    @app.route('/result',methods = ['POST'])
    def result():
        if request.method == 'POST':
            tempResult = request.form
            gotValues = dataObject.returnTopMetric(tempResult['datasetType'],tempResult['specParm'])
            
            return render_template("result.html",result = gotValues)



if __name__== '__main__':
    app.run(debug=True)