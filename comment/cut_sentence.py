from comment import striptxt
import xlrd

def cutSentence():
    data = xlrd.open_workbook(filename=r'./hangzhou_comment.xls')
    sheet1 = data.sheet_by_index(1)
    comment_input = sheet1.col_values(0)
    people_id = sheet1.col_values(1)

    comment_output = []
    for line in comment_input:
        line_seg = striptxt.seg_sentence(line)  # 这里的返回值是字符串
        comment_output.append(line_seg)
    return  comment_output
