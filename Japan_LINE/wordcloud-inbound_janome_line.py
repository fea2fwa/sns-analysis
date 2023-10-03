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
                   '者','せ','いただき',"すれ良い","やっみ","あるの","できの","A","A","み","み宜しく","I","I","すれ","良い","ある",
                   "の","ありその","あり","その","回答ありがとう","回答","ありがとう","上記同じ","上記","同じ","教えください","教え",
                   "ください","頂きありがとう","頂き"])

# 日本語テキストを行ごとに読み込む
with open('chatmessages-inbound.txt', 'r', encoding='utf-8') as f:
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
wordcloud.to_file("wordcloud_line-inbound.png")