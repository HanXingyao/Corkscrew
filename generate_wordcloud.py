import re
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter


# 下载NLTK的词性标注数据
nltk.download('averaged_perceptron_tagger')

# 读取文件内容到字符串
with open('demo.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 使用正则表达式将文本拆分为长度为2到5的短语
phrases = re.findall(r'\b[\w\s]{10,25}\b', text)
phrases = [phrase.lower() for phrase in phrases]
print('Phrase Num:', len(phrases))

# 标记词性
tagged_phrases = nltk.pos_tag(phrases)
# print(tagged_phrases)

# 过滤非名词的短语
noun_phrases = [phrase for phrase, tag in tagged_phrases if tag.startswith('N')]
print('Noun Phrase Num:', len(noun_phrases))

# 手动过滤一些常见的非名词短语
non_noun_words = ['the', 'a', 'an', 'and', 'or', 'but', 'with', 'in', 'on', 'for', 'of', 'to', 'by', 'as', 'at']
# 过滤非名词短语
filtered_phrases = []
for phrase in noun_phrases:
    if len(phrase.split()) < 2:
        continue
    if not any(word.lower() in non_noun_words for word in phrase.split()):
        filtered_phrases.append(phrase)

print('Noun Phrase Num:', len(filtered_phrases))

# 计算短语频率
phrase_counts = Counter(filtered_phrases)

# 去掉前五大的短语
# for phrase, count in phrase_counts.most_common(0):
#     del phrase_counts[phrase]

# 生成词云
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(phrase_counts)

# 显示词云
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig('wordcloud.png')
plt.show()
