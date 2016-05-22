from flask import Flask
app = Flask(__name__)
from sklearn.externals import joblib

# load the chosen and trained model
clf = joblib.load('operations.pkl')


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/predict/<float:v>/")
def predict(v):
    '''
    regr.predict(array) returns a list, [0] gets the only value in the list.
    :param v: numpy.ndarray, format of v train_data[0::, [0, 1, 2, 4]]
    :return: str, Time prediction in seconds
    '''
    v = v.reshape(1, -1)  # no warnings
    return str(clf.predict([v])[0])

if __name__ == "__main__":
    # 3 examples
    print clf.predict([36., 4., 50., 344.])
    print clf.predict([94., 4., 37., 524.])
    print clf.predict([9., 1., 36., 45.])
    #app.run()

# example: call from from rails
# def estimate
#   self.estimation = HTTP.get("http://localhost:5000/predict/#{op1.to_f}/").to_s
# end