import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from janome.tokenizer import Tokenizer

notincluded = set(['可能', 'よう','承知','お願い','場合','確認','の','対応','担当','連絡',
                   '起動','こと','こちら','様','申し訳','ところ','何','方','番号','了解',
                   '先','認識','表示','時','方法','問題','画面','大丈夫','作業','日','ため',
                   '中','お手数','０','0','O',"前","I","P","P","A","A","r","まま","ん"
                   ,"者","jp","これ","後"])

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
input_text_file = 'dedup-chatmessages-inboundt.txt'  # 入力テキストファイル名
output_image = 'wordcloud_line-dedup-inbound.png'  # 出力Wordcloud画像名

generate_wordcloud(input_text_file, output_image)


