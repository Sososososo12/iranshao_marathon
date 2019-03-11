from snownlp import SnowNLP
from comment import cut_sentence

output_sentence=[]
input_sentence=[]
inputs=cut_sentence.cutSentence()
for i in inputs:
    i.replace(' ','')
    if i!='':
        input_sentence.append(i)

for line in inputs:
    a=SnowNLP(line)
    output_sentence.append(a.sentiments)
print(output_sentence)
