from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    csv_path = os.path.join('admet', 'admet_results.csv')
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
