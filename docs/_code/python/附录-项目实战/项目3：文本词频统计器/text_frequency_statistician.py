import sys
import string

from collections import Counter

def parse_args():
    # 解析命令行参数
    if len(sys.argv) != 2:
        print("使用方法：python text_frequency_statistician.py <文件路径名称> ")
        sys.exit(1)
    filename = sys.argv[1]
    
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    return filename, top_n

def read_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # 移除标点符号, 并转换为小写
            line = line.translate(str.maketrans('', '', string.punctuation))
            for word in line.lower().split():
                yield word

def count_words(filename):             
    word_counts = Counter()
    for word in read_words(filename):
        word_counts[word] += 1
    return word_counts

def main():
    filename, top_n = parse_args()
    try:
        counter = count_words(filename)
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在。")
        sys.exit(1)
    for word, count in counter.most_common(top_n):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()