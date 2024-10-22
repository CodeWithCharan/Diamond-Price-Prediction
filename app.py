import os
import numpy as np
import pandas as pd

from flask import Flask, render_template, request
from mlProject.pipeline.prediction_pipeline import PredictionPipeline

# initialize the flask app
app = Flask(__name__)

# Route for homepage
@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")

# Route for training pipeline
@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful!"

# Route for prediction
@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # Reading the inputs given by the user for diamond prediction
            carat = float(request.form['carat'])
            cut = request.form['cut']
            color = request.form['color']
            clarity = request.form['clarity']
            depth = float(request.form['depth'])
            table = float(request.form['table'])
            x = float(request.form['x'])
            y = float(request.form['y'])
            z = float(request.form['z'])
        
            # Create a DataFrame or numpy array with user input
            data = pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]],
                                columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z'])

            # Initialize the pipeline
            obj = PredictionPipeline()

            # transform the input data
            data_transformed = obj.data_transform(data)

            # predict the input data
            predict = obj.predict(data_transformed)

            # Convert prediction to a float and format it as price
            formatted_pred = "{:,.2f}".format(float(predict[0]))

            return render_template('results.html', prediction=formatted_pred)
            
        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong. Please try again.'
    
    else:
        return render_template('index.html')



if __name__ == "__main__":
    # run the app locally
    # app.run(host="0.0.0.0", port=8080, debug=True)
    # run the app in cloud
    app.run(host="0.0.0.0", port=8080)