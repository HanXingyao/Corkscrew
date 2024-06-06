import pandas as pd

# 使用pandas的read_excel函数
data = pd.read_excel('TPC-TITS-Review.xlsx')

# 提取'摘要'列
abstract = data['摘要']
# print(abstract)

# 将所有的摘要连接成一个长字符串
text = ' '.join(abstract)

with open('demo.txt', 'w', encoding='utf-8') as f:
    # 将文本写入文件
    f.write(text)
