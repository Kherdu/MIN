  # coding=<utf-8>
from flask import Flask
from flask import request
from pandas import DataFrame
from sklearn.externals import joblib
import numpy
app = Flask(__name__)




  # Cargo el modelo que he entrenado previamente.
regr = joblib.load('operations.pkl')


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/predict", methods=['GET'])
def predict():
  arr_pene  = DataFrame([[request.args.get('op1'), request.args.get('op'), request.args.get('op2')]])
  # Aqui va la magia de Machine Learning
  print arr_pene
  arr_pene2 = numpy.reshape(arr_pene, (2, 1))
  print arr_pene2
  result = regr.predict(arr_pene2)
  print ("chupame un pier:" + result[0])
  print ("pene")
  return str(regr.predict(arr_pene))

if __name__ == "__main__":

    app.run()

# Desde Rails podeis llamarlo asi

# def estimate
#   self.estimation = HTTP.get("http://localhost:5000/predict/#{op1.to_f}/").to_s
# end
