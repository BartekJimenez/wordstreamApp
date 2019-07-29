from flask import Flask, render_template, request
from flask_assets import Bundle, Environment
from data import DataHarvester
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
import requests

response = requests.get("https://app.wordstream.com/services/v1/wordstream/interview_data")
dataObject = DataHarvester(response)

js = Bundle('homeHandler.js', output='get/main.js')

app = Flask(__name__)

assets = Environment(app)
assets.register('main_js', js)


# name = TextField('Name:', validators=[validators.required()])
usableDataSets = dataObject.createMeasurementList()
usableDataSets = dataObject.sort(usableDataSets)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/datasets')
def datasets():
    return render_template('datasets.html', returnData = usableDataSets)

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

        tempHold = dataObject.createMeasurementList(tempResult['datasetInput_id'],tempResult['specParmInput_key'],tempResult['specParmInput_value'])        
        print(type(int(tempResult['comparer_id'])))
        if int(tempResult['comparer_id']) == 2:
            tempHold2 = dataObject.createMeasurementList(tempResult['datasetInput_id2'],tempResult['specParmInput_key2'],tempResult['specParmInput_value2'])
            addLists = tempHold + tempHold2
            print("@@@@@@@@@@@@@@@@@@@@")
            print(len(tempHold))
            print(len(tempHold2))
            gotValues = dataObject.returnTopMetric(addLists)
        else:
            gotValues = dataObject.returnTopMetric(tempHold)

        return render_template("result.html",result = gotValues)



if __name__== '__main__':
    app.run(debug=True)