from flask import Flask
from flask import request
import numpy
app = Flask(__name__)
from sklearn.externals import joblib

# load the chosen and trained model
clf = joblib.load('operations.pkl')


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/predict", methods=['GET'])
def predict():
    '''
    regr.predict(array) returns a list, [0] gets the only value in the list.
    :param v: numpy.ndarray, format of v train_data[0::, [0, 1, 2, 4]]
    :return: str, Time prediction in seconds
    '''
    op1 = float(request.args.get('op1'))
    op = str(request.args.get('op'))
    #op = op.map({'+': 1, '-': 1, '/': 1, '*': 4}).astype(int)
    operacion = 1.
    if op == '+' or op == '-' or op=='/':
        operacion =1.
    else:
        operacion = 4.

    op2 = float(request.args.get('op2'))
    complexity = (op1+op2)*operacion
    v = [op1, operacion, op2, complexity]
    prediction = str(clf.predict([v])[0])
    print prediction
    return prediction

if __name__ == "__main__":
    # 3 examples
    #print clf.predict([36., 4., 50., 344.])
    #print clf.predict([94., 4., 37., 524.])
    #print clf.predict([9., 1., 36., 45.])

    app.run()

# example: call from from rails
# def estimate
#   self.estimation = HTTP.get("http://localhost:5000/predict/#{op1.to_f}/").to_s
# end