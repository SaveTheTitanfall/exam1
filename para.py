import numpy as np
from math import sqrt
import pandas as pd
data=pd.Series(np.random.randint(10,20,10))
data
print(data)
num=pd.DataFrame(np.random.randint(10,20,size=(9,15)),index=("ww","222","111","ww","222","111","ww","222","111"))