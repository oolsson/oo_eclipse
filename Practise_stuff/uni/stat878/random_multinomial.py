import numpy as np
import pandas as pd
x=np.random.multinomial(197, [0.65670537446775,   0.09329462553225,   0.09329462553225,   0.15670537446775], size=1000)
x2=pd.DataFrame(x)
x2.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\price.csv")