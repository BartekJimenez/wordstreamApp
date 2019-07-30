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
    try:
        if request.method == 'POST':
            tempResult = request.form
            amountOfDatasets = int(tempResult['comparer_id'])
            tempHold = dataObject.createMeasurementList(tempResult['datasetInput_id1'],tempResult['specParmInput_key1'],tempResult['specParmInput_value1'])        
            if amountOfDatasets == 1:
                gotValues = dataObject.returnTopMetric(tempHold,int(tempResult['amountOfResults']))

            elif amountOfDatasets == 2:
                tempHold2 = dataObject.createMeasurementList(tempResult['datasetInput_id2'],tempResult['specParmInput_key2'],tempResult['specParmInput_value2'])
                addLists = tempHold + tempHold2
                gotValues = dataObject.returnTopMetric(addLists,int(tempResult['amountOfResults']))
            elif amountOfDatasets == 3:
                tempHold2 = dataObject.createMeasurementList(tempResult['datasetInput_id2'],tempResult['specParmInput_key2'],tempResult['specParmInput_value2'])
                tempHold3 = dataObject.createMeasurementList(tempResult['datasetInput_id3'],tempResult['specParmInput_key3'],tempResult['specParmInput_value3'])
                addLists = tempHold + tempHold2 + tempHold3
                gotValues = dataObject.returnTopMetric(addLists,int(tempResult['amountOfResults']))
            return render_template("result.html",result = gotValues)
    except:
        return "request failed. Please try again and double check your input variables."



if __name__== '__main__':
    app.run(debug=True)