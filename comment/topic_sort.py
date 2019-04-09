import xlrd
import xlwt
import pandas as pd
import csv
import numpy as np

numid=[]
maxtopic1=[]
maxtopic2=[]
maxtopic3=[]
maxtopic1_pro=[]
maxtopic2_pro=[]
maxtopic3_pro=[]

# 读取文件并建为DataFrame格式
data=pd.DataFrame(pd.read_csv('./art1topic8.csv'))
# 将num设置为索引index
topic_data=data.set_index('comment_num')
for i in range(1,topic_data.shape[0]+1):
    # 获取第一行的切片数，并且排序提取前3的值
    num = topic_data.loc[i]
    num_sort = num.sort_values(ascending=False)[:3]
    # numid.append(loading_article_num.article_nums[i-1])
    maxtopic1.append(num_sort.index[0])
    maxtopic2.append(num_sort.index[1])
    maxtopic3.append(num_sort.index[2])
    maxtopic1_pro.append(num_sort[0])
    maxtopic2_pro.append(num_sort[1])
    maxtopic3_pro.append(num_sort[2])
    print('已提取num '+str(i)+' 的前三个主题')
print(len(maxtopic1))
print(len(maxtopic1_pro))
print(len(maxtopic2))
print(len(maxtopic2_pro))
print(len(maxtopic3))
print(len(maxtopic3_pro))

data1 = pd.DataFrame({
                      'max topic1': maxtopic1,
                      'max topic2': maxtopic2,
                      'max topic3': maxtopic3,
                      'max topic1 pro': maxtopic1_pro,
                      'max topic2 pro': maxtopic2_pro,
                      'max topic3 pro': maxtopic3_pro,
                      })
data1.to_excel(u'topic8_propotion.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')

