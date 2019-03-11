import jieba
# import loading_article_num
import time


# jieba.load_userdict('userdict.txt')
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('./based/stopwords5.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# for item_num in loading_article_num.article_nums:
#     inputs = open('./txtres/{}.txt'.format(item_num), 'r', encoding='utf-8')
#     outputs = open('./newtxtres/{}out.txt'.format(item_num), 'w', encoding='utf-8')
#     for line in inputs:
#         line_seg = seg_sentence(line)  # 这里的返回值是字符串
#         outputs.write(line_seg + '\n')
#     outputs.close()
#     inputs.close()
#     # time.sleep(2)
