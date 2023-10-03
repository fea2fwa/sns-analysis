from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
from janome.tokenizer import Tokenizer

# JanomeのTokenizerをインスタンス化
t = Tokenizer()

words = ""

#　ワードクラウドに含めない単語を指定
notincluded = set(['こと', 'これ', 'それ','され','させ','お願い','よろしく','お願いいたし','お願いし','致し','しい','いる','発生し',
                   'しい','され','させ','さ','れい','しおり','し','おり','様','承知し','承知', 'れい','担当者','れい','せいただき',
                   'ご対応','お世話','なっ','ご担当','担当者','ご連絡','連絡先','れい','れ','い','れ　い','ご','連絡','担当',
                   '者','せ','いただき','お待ちください','お知らせください','確認いたし','いたし','お手数おかけ','お名前','会社名','お時間',
                   "今回お","今回","お","BF","BF","BA","BA","com","E","BC","EBC","大変","大変お","なり","回答なり","EBB","BB","確認うえ",
                   "うえ","ため今回","ため","くださいはい","ください","はい","A","A","お","必要なり","なり","上記","同じ","上記同じ",
                   "するため","する","ため","C","c","B","B","ja","jp"])

# 日本語テキストを行ごとに読み込む
with open('chatmessages-outbound.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # 各行を形態素解析し、単語に分割する
        tokens = t.tokenize(line)
        # 品詞を確認して、特定の品詞を除外する
        words += " ".join([token.surface for token in tokens if "助詞" not in token.part_of_speech and "接続詞" not in token.part_of_speech and "助動詞" not in token.part_of_speech])

# ワードクラウドの設定
wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/msgothic.ttc',  # フォントへのパスを指定
    background_color='white',  # 背景色を白に設定
    width=800,  # 幅を設定
    height=600,  # 高さを設定
    colormap='tab10',  # カラーパレットを設定
    stopwords=notincluded,  # ストップワードを設定
).generate(words)

# ワードクラウドを表示
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
wordcloud.to_file("wordcloud_line-outbound.png")