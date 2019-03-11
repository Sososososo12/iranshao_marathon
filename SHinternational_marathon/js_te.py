import numpy as np
import scipy.stats
import xlrd
import pandas as pd

p=np.array([0.65,0.25,0.07,0.03])
q=np.array([0.6,0.25,0.1,0.05])
q2=np.array([0.1,0.2,0.3,0.4])
def JS_divergence(p,q):
    M=(p+q)/2
    return 0.5*scipy.stats.entropy(p, M)+0.5*scipy.stats.entropy(q, M)
print(JS_divergence(p,q)) # 0.003093977084273652 print(JS_divergence(p,q2)) # 0.24719159952098618 print(JS_divergence(p,p)) # 0.0


# workbook = xlrd.open_workbook(r'./finfish2.csv',sheetname="Sheet1")
df=pd.read_csv(r'./result/doc_topic.csv',header=None)
col1=df.loc[0].values
col2=df.loc[1].values
col3=df.loc[2].values
col4=df.loc[3].values
col5=df.loc[4].values
# print(col1)
# print(type(col1))



print(JS_divergence(col1,col2))
print(JS_divergence(col2,col3))
print(JS_divergence(col1,col3))
print(JS_divergence(col3,col4))
print