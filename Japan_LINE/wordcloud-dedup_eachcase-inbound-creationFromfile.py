import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

notincluded = set(['可能', 'よう','承知','お願い','場合','確認','の','対応','担当','連絡',
                   '起動','こと','こちら','様','申し訳','ところ','何','方','番号','了解',
                   '先','認識','表示','時','方法','問題','画面','大丈夫','作業','日','ため',
                   '中','お手数','０','0','O',"前","I","P","P","A","A","r","まま","ん"
                   ,"者","jp","これ","後",".","1","-","2","/","@","(",")","名","3","4",
                   "5","6","7","8","9","10","以下","2019"])

def generate_wordcloud_fromfile(input_text_file, output_image):
    # テキストファイルから単語と出現頻度を読み込み集計
    word_freq_from_file = {}
    with open(input_text_file, 'r', encoding='utf-8') as fdi2:
        lines = fdi2.readlines()
        for line in lines:
            word, freq = line.strip().split(',')
            if word not in notincluded:
                word_freq_from_file[word] = int(freq)

    # 単語の集計結果からWordcloudを生成する
    wordcloud = WordCloud(
        font_path='C:/Windows/Fonts/msgothic.ttc',  # フォントへのパスを指定
        background_color='white',  # 背景色を白に設定
        width=800,  # 幅を設定
        height=600,  # 高さを設定
        colormap='tab10',  # カラーパレットを設定
        stopwords=notincluded,  # ストップワードを設定
    ).generate_from_frequencies(word_freq_from_file)

    # Wordcloudを表示する
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_image)
    plt.show()

# プログラムの実行
input_text_file = 'word_freq_dedup_inbound-En.txt'  # 入力テキストファイル名
output_image = 'wordcloud_line-dedup-inbound-fileInput.png'  # 出力Wordcloud画像名

generate_wordcloud_fromfile(input_text_file, output_image)


