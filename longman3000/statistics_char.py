import re
from collections import defaultdict

def count_words_starting_with_each_letter(markdown_text):
    # 使用正则表达式找到所有以大写字母开头的单词
    pattern = r'\b[A-Z]\w*\b'
    matches = re.findall(pattern, markdown_text)
    
    # 创建一个字典来存储每个字母开头的单词数量
    word_counts = defaultdict(int)
    
    # 统计每个字母开头的单词数量
    for word in matches:
        first_letter = word[0]
        word_counts[first_letter] += 1
    
    return dict(word_counts)

# 读取Markdown文档内容
with open('D:/code/automic-habit/longman3000/Longman_unknowned.md', 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# 统计以大写字母开头的单词数量
word_counts = count_words_starting_with_each_letter(markdown_text)

# 输出每个字母开头的单词数量
for letter, count in sorted(word_counts.items()):
    print(f"以'{letter}'开头的单词个数为: {count}")

