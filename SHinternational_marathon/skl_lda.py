# -*- coding: utf-8 -*-
import numpy as np
import numpy
from sklearn.feature_extraction.text import CountVectorizer
import lda
import lda.datasets
from SHinternational_marathon import getpersonid
import xlwt
import xlrd
import pandas as pd

# 存储读取语料 一行预料为一个文档
corpus = []



for item_id in getpersonid.getIds():
    path_file_name = './person_out_txt/{}_out_article.txt'.format(item_id)
    with open(path_file_name, "r", encoding='utf-8') as f:  # 打开文件
        data = f.read()  # 读取文件
    corpus.append(data.replace('\u3000', ''))
# print(corpus)
# for line in open('./outputs_2.txt', 'r',encoding='utf-8').readlines():
#     #print line
#     corpus.append(line.strip())
# #print corpus


# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(corpus)
# print(x)
analyze = vectorizer.build_analyzer()
weight = x.toarray()

model = lda.LDA(n_topics=10, n_iter=2000, random_state=1)
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
n = 20
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(word)[np.argsort(topic_dist)][:-(n + 1):-1]
    print(u'*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

# print(type(doc_topic))
# print(type(topic_word))
numpy.savetxt('./result/doc_topic.csv', doc_topic, delimiter=',')  # 将得到的文档-主题分布保存
numpy.savetxt('./result/topic_word.csv', topic_word, delimiter=',',encoding='utf-8')

# 输出前10篇文章最可能的Topic
label = []
for n in range(len(corpus)):
    topic_most_pr = doc_topic[n].argmax()
    label.append(topic_most_pr)
    print("doc: {} topic: {}".format(n, topic_most_pr))

data1 = pd.DataFrame({'person_id':getpersonid.getIds(),
                      'topic label':label,
                      })
data1.to_excel(u'topic_base.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')

