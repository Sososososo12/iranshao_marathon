from SHinternational_marathon import striptxt
from SHinternational_marathon import getpersonid
import time



num=0
for item_id in getpersonid.getIds():
    num=num+1
    inputs = open('./person_txt/{}_articles.txt'.format(item_id), 'r', encoding='utf-8')
    outputs = open('./person_out_txt/{}_out_article.txt'.format(item_id), 'w', encoding='utf-8')
    for line in inputs:
        line_seg = striptxt.seg_sentence(line)  # 这里的返回值是字符串
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()
    # time.sleep(2)
    print(str(num)+'   '+'编号'+item_id+'文章已分词！')
print('project finish')

# inputs = open('./p12.txt', 'r',encoding='utf-8')
# outputs = open('./articlete2.txt', 'w', encoding='utf-8')
# for line in inputs:
#     line_seg = seg_sentence(line)  # 这里的返回值是字符串
#     outputs.write(line_seg + '\n')
# outputs.close()
# inputs.close()