from flask import Flask
app = Flask(__name__)


from sklearn.externals import joblib

  # Cargo el modelo que he entrenado previamente.
regr = joblib.load('operations.pkl')


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/predict/<float:v>/")
def predict(v):

  return str(regr.predict([v])[0])

if __name__ == "__main__":

    app.run()


# def estimate
#   self.estimation = HTTP.get("http://localhost:5000/predict/#{op1.to_f}/").to_s
# end