from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model from the file
with open('spam_classification_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the index route
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the message from the form
    message = request.form['message']

    # Make prediction
    prediction = model.predict([message])[0]
    if prediction == 1:
        result = 'Spam'
    else:
        result = 'Not Spam'

    # Render the result page with the prediction
    return render_template('result.html', message=message, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
