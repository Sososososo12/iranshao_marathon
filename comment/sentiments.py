from snownlp import SnowNLP
import pandas as pd
import xlrd


data = xlrd.open_workbook(filename=r'./comment_sentiment2.xls')
sheet1 = data.sheet_by_index(0)
cut_comment_input = sheet1.col_values(0)
# print(cut_comment_input)

output_sentence=[]
# input_sentence=[]
#
#
for line in cut_comment_input:
    a=SnowNLP(line)
    output_sentence.append(a.sentiments)
# print(output_sentence)
data1 = pd.DataFrame({'sentiments':output_sentence

                      })
data1.to_excel(u'comment_sentiment2_finish.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')

