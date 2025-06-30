# Dummy file for main.py
from flask import Flask, render_template, request
from utils.model_utils import load_model_and_predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        image = request.files['image']
        prediction = load_model_and_predict(image)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
