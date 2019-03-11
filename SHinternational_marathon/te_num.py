from SHinternational_marathon.scrpyArticle import getPersonArticle

import xlrd

ids=[]
article_nums=[]

data = xlrd.open_workbook(filename='./num_new.xlsx')
sheet1 = data.sheet_by_index(0)
# 读取excel中sheet1里第一列的数据
article_person_id=sheet1.col_values(1)
for i in range(1,len(article_person_id)):
    print('now loading data of '+article_person_id[i])
    getarticle = getPersonArticle()
    allnum = getarticle.getDairies_sites(article_person_id[i])
    article = getarticle.getArticle(allnum)
    getarticle.downloadingTxt(article,article_person_id[i])
    print('success save txt of '+article_person_id[i]+' !')


