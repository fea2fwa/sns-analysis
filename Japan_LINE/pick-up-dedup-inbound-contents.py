import pandas as pd
from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def extract_unique_words(input_file, output_file, target_column, other_column):
    # Excelファイルを読み込む
    df = pd.read_excel(input_file)

    # 列ごとにテキストを収集し、単語を重複を除いてファイルに追記出力する
    tokenizer = Tokenizer()
    for target_value, other_values in df.groupby(target_column)[other_column]:
        text = ' '.join(other_values.dropna().astype(str).values)
        tokens = tokenizer.tokenize(text)
        words = {token.surface for token in tokens if token.part_of_speech.split(',')[0] in ["名詞", "動詞", "形容詞"] }  # 名詞、動詞、形容詞のみを抽出

        print(words)

        with open(output_file, 'a', encoding='utf-8') as file:
            for word in words:
                file.write(word + '\n')

# プログラムの実行例
input_file = 'sla_raw_concatinated.xlsx'  # 入力ファイル名
output_file = 'dedup-chatmessages-inboundt.txt'  # 出力ファイル名
target_column = 'Associated Cases'  # 対象の列名
other_column = 'Inbound Message'  # 他の列名

extract_unique_words(input_file, output_file, target_column, other_column)
