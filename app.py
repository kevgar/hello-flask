from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
from plotly.utils import PlotlyJSONEncoder
import json
import numpy as np

# instantiate the application object
app = Flask(__name__)

# # create an endpoint with a decorator
# @app.route('/')
# def hello():
#     return 'Hello World'

faithful = pd.read_csv('./data/faithful.csv')

@app.route('/graph', methods=['GET'])
def hist():
    # calculate the bins
    x = faithful['waiting']
    counts, bins = np.histogram(x, bins=np.linspace(np.min(x), np.max(x), int(request.args['bins'])+1))
    bins = 0.5* (bins[:-1] + bins[1:])
    p = px.bar(
        x=bins, y=counts,
        title='Histogram of waiting times',
        labels={
            'x': 'Waiting time to next eruption (in mins)',
            'y': 'Frequency'
        },
    template='simple_white'
    )
    return json.dumps(p, cls=PlotlyJSONEncoder)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()