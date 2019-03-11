import xlrd


article_nums=[]

def getIds():
    ids = []
    data = xlrd.open_workbook(filename='./num_new.xlsx')
    sheet1 = data.sheet_by_index(0)
    # 读取excel中sheet1里第一列的数据
    article_person_id = sheet1.col_values(1)
    for i in range(1, len(article_person_id)):
        ids.append(article_person_id[i])
    # print(ids)
    return ids


getIds()