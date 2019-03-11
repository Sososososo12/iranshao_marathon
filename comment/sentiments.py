from snownlp import SnowNLP
from comment import cut_sentence
import pandas as pd
import xlrd

data = xlrd.open_workbook(filename=r'./cut_duplicates.xlsx')
sheet1 = data.sheet_by_index(0)
comment_input = sheet1.col_values(2)
# people_id = sheet1.col_values(1)
print(comment_input)


output_sentence=[]
input_sentence=[]


for line in comment_input:
    a=SnowNLP(line)
    output_sentence.append(a.sentiments)
# print(output_sentence)
data1 = pd.DataFrame({'sentiments':output_sentence,

                      })
data1.to_excel(u'comment_sentiment.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')

