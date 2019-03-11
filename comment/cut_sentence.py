from comment import striptxt
import xlrd
import pandas as pd

def cutSentence():
    data = xlrd.open_workbook(filename=r'./hangzhou_comment_sen.xls')
    sheet1 = data.sheet_by_index(0)
    comment_input = sheet1.col_values(0)
    people_id = sheet1.col_values(1)

    comment_output = []
    for line in comment_input:
        line_seg = striptxt.seg_sentence(line)  # 这里的返回值是字符串
        comment_output.append(line_seg)

    data1 = pd.DataFrame({'cut_sentence': comment_output

                          })
    data1.to_excel(u'comment_sentiment2.xls', index=False, encoding='"utf_8_sig')
    print('信息写入完成！')
    return  comment_output


cutSentence()

