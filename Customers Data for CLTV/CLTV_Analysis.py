## Customer life time value analysis

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df= pd.read_csv(r'C:\Users\Anjli Rathi\Downloads\Projects\Git Projects\Python\CLTV Analysis\Customers Data for CLTV.csv',index_col='channel' )
df

df.shape()