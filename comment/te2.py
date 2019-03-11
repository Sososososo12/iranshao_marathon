import xlwt
import pandas as pd
import os
import re

dictlist=[]
filepath='./based/good_estiment_dict.txt'
itemname=re.findall('based/(.*?).txt',filepath)[0]
for line in open(filepath, 'r', encoding='utf-8').readlines():
    dictlist.append(line)

data1 = pd.DataFrame({'dict':dictlist
                      })
data1.to_excel(u'{}_dict.xls'.format(itemname), index=False, encoding='"utf_8_sig')
print('信息写入完成！')