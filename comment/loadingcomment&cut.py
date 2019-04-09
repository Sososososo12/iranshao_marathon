import xlrd
import xlwt
import pandas as pd
from comment import striptxt
# -*- coding: utf-8 -*-
import numpy as np
import numpy
from sklearn.feature_extraction.text import CountVectorizer
import lda
import lda.datasets


data=xlrd.open_workbook(filename=r'./hangzhou_comment_sen2.xls')
sheet1 = data.sheet_by_index(1)
comment_input=sheet1.col_values(0)
people_id=sheet1.col_values(1)

comment_output=[]
for line in comment_input:
    line_seg = striptxt.seg_sentence(line)  # 这里的返回值是字符串
    comment_output.append(line_seg)
# print(comment_output)

# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(comment_output)
# print(x)
analyze = vectorizer.build_analyzer()
weight = x.toarray()

model = lda.LDA(n_topics=8, n_iter=2000, random_state=1)
model.fit(np.asarray(weight))  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
# 文档-主题（Document-Topic）分布
doc_topic = model.doc_topic_

# print("type(doc_topic): {}".format(type(doc_topic)))

# 输出主题中的TopN关键词
word = vectorizer.get_feature_names()
# for w in word:
#     print
#     w
# print
# topic_word[:, :3]
# print
# print(word)
n = 30
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(word)[np.argsort(topic_dist)][:-(n + 1):-1]
    print(u'*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

# print(type(doc_topic))
# print(type(topic_word))
numpy.savetxt('./art1topic8.csv', doc_topic, delimiter=',')  # 将得到的文档-主题分布保存
numpy.savetxt('./art2topic8.csv', topic_word, delimiter=',',encoding='utf-8')

# 输出前20篇文章最可能的Topic
label = []
for n in range(len(doc_topic)):
    topic_most_pr = doc_topic[n].argmax()
    label.append(topic_most_pr)
    print("doc: {} topic: {}".format(n, topic_most_pr))

data1 = pd.DataFrame({'comment_txt':comment_output,
                      'number id':people_id,
                      'topic label':label,
                      })
data1.to_excel(u'topic8_base.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')