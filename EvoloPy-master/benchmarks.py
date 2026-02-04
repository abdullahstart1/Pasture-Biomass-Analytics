import numpy as np
import math
import pandas as pd

data = pd.read_csv(r"..\Complete_Dataset_updated.csv")

# define the function blocks
def MSE_ESI(num):
    w1, w2, w3= num
    actual_ESI = data['Environmental Suitability Index']
    predicted_ESI = w1 * data['Rainfall'] + w2 * data['TEMP_MAX'] + w3 * data['NDVI']
    mse =  np.mean((actual_ESI-predicted_ESI)**2)
    return mse

def getFunctionDetails(a):
    # [name, lb, ub, dim]
    param = {
        "MSE_ESI": ["MSE_ESI",0,1,3],
    }
    return param.get(a, "nothing")