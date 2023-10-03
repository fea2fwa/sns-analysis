import matplotlib.pyplot as plt
from wordcloud import WordCloud

notincluded = set(['i', 'ok', 'com', 'no', 'ye', 'need', 'name', 'sure', 'yes', 'good',
                   'are', 'u', 's', 'please', 'same', 'thank','is', 'sir', 'send',
                   'o', 'done', 'okay', 'have', 'take', 'time', 'other', 'fine', 'thanks',
                   'm', 'hi', 'email', 'dell', 'part', 'correct', 'be','my', 'part', 'know',
                   'contact', 'number', 'case', 'able', 'help', 'do', 'get', 'give'])

def generate_wordcloud(input_text_file, output_image):
    # テキストファイルを1行ずつ読み込んで単語を集計する
    words = []
    with open(input_text_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            words.append(word)

    # 単語の集計結果からWordcloudを生成する
    wordcloud = WordCloud(
        font_path='C:/Windows/Fonts/msgothic.ttc',  # フォントへのパスを指定
        background_color='white',  # 背景色を白に設定
        width=800,  # 幅を設定
        height=600,  # 高さを設定
        colormap='tab10',  # カラーパレットを設定
        stopwords=notincluded,  # ストップワードを設定
    ).generate(' '.join(words))

    # Wordcloudを表示する
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_image)
    plt.show()

# プログラムの実行例
input_text_file = 'dedup-chatmessages-inbound_sgmy.txt'  # 入力テキストファイル名
output_image = 'wordcloud_line-dedup-inbound_sgmy.png'  # 出力Wordcloud画像名

generate_wordcloud(input_text_file, output_image)


