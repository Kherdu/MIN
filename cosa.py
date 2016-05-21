
import numpy
from pandas import DataFrame

from sklearn.externals import joblib


regr = joblib.load('operations.pkl')
arr_pene  = DataFrame([['3', '*', '4'],['3','+','3']])
res= regr.predict(arr_pene[0])
print res
arr_pene2 = numpy.reshape(arr_pene, (3, 2))
print arr_pene
print arr_pene2