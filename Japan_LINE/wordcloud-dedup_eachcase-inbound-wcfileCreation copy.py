import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

def generate_wordcloud_basefile(input_text_file):
    # テキストファイルを1行ずつ読み込んで単語を集計する
    words = []
    with open(input_text_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            words.append(word)
        word_freq = Counter(words)

        # 集計した単語の出現数Top300を昇順で並び変えてテキストファイルに出力
        with open('word_freq_dedup_inbound.txt', 'w', encoding='utf-8') as fdi:
            for word, freq in word_freq.most_common(300):
                fdi.write(f"{word},{freq}\n")

# プログラムの実行
input_text_file = 'dedup-chatmessages-inboundt.txt'  # 入力テキストファイル名

generate_wordcloud_basefile(input_text_file)


