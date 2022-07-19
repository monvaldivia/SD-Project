import string
from tokenize import String
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_text = request.form.get('search')
        filter = request.form.get('filter')
        df = pd.read_csv('rankingExample.csv')
        search_results = df.loc[df["query"].str.contains(search_text)]
        data = {
            'df': search_results,
        }
        return render_template('search.html', search_results=data)
    return render_template('search.html')


if __name__ == '__main__':
    app.run()
