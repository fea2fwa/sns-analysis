import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# nltkのリソースをダウンロード
nltk.download('punkt')  # word_tokenizeメソッドを利用するために必要
nltk.download('averaged_perceptron_tagger')  # tokenizeした単語に品詞タグをつけるために必要

def extract_unique_words(input_file, output_file, target_column, other_column):
    # Excelファイルを読み込む
    df = pd.read_excel(input_file)

    # 列ごとにテキストを収集し、単語を重複を除いてファイルに追記出力する
    for target_value, other_values in df.groupby(target_column)[other_column]:
        text = ' '.join(other_values.dropna().astype(str).values)
        words = word_tokenize(text) # 単語分割
        tagged_words = pos_tag(words)  # 単語に品詞タグ付け
        # 単語の重複排除用に名詞, 動詞, 形容詞のセットを定義
        nouns = set()
        verbs = set()
        adjectives = set()
        # 品詞によって単語を分類
        for word, tag in tagged_words:
            if tag.startswith('NN'):
                nouns.add(word.lower())  # 名詞
            elif tag.startswith('VB'):
                verbs.add(word.lower())  # 動詞
            elif tag.startswith('JJ'):
                adjectives.add(word.lower())  # 形容詞

        print(f"Nouns: {nouns}")
        print(f"Verbs: {verbs}")
        print(f"Adjs: {adjectives}")

        with open(output_file, 'a', encoding='utf-8') as file:
            for word in nouns:
                file.write(word + '\n')
            for word in verbs:
                file.write(word + '\n')
            for word in adjectives:
                file.write(word + '\n')

# プログラムの実行例
input_file = 'sla_raw_concatinated_sgmy.xlsx'  # 入力ファイル名
output_file = 'dedup-chatmessages-inbound_sgmy.txt'  # 出力ファイル名
target_column = 'Associated Cases'  # 対象の列名
other_column = 'Inbound Message'  # 他の列名

extract_unique_words(input_file, output_file, target_column, other_column)
