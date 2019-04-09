from snownlp import SnowNLP
import pandas as pd
import xlrd
from comment import striptxt


data = xlrd.open_workbook(filename=r'./2018QingHai0319.xls')
sheet1 = data.sheet_by_index(0)
comment_input = sheet1.col_values(0)
# numid=sheet1.col_values(1)
# print(cut_comment_input)

cut_comment=[]
for line in comment_input:
    line_seg = striptxt.seg_sentence(line)  # 这里的返回值是字符串
    if line_seg=='':
        cut_comment.append('a')
    else:
        cut_comment.append(line_seg)

# print(comment_output)

output_sentence=[]
# input_sentence=[]
#
#
for line in cut_comment:
    a=SnowNLP(line)
    output_sentence.append(a.sentiments)
# print(output_sentence)
data1 = pd.DataFrame({'sentiments':output_sentence,
                      'cut_comment':cut_comment,
                      'sentiments_raw':comment_input

                      })
data1.to_excel(u'qinghai_sentiment.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')

