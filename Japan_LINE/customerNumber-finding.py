import pandas as pd
import re
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む
df_sfdc = pd.read_excel('sfdc_raw_concatinated.xlsx') 

# 必要な列だけ抜き出して、TypeをObjectに合わせる
df_sfdc = df_sfdc[['Customer #', 'SR Title']].astype(object)

# 特定の列から8桁の数字を抽出する関数を定義する
def extract_8digit_num(row):
    # 'SR Title'列を対象とする
    matches = re.findall(r'\b\d{8}\b', str(row['SR Title']))
    return ', '.join(matches)

# 新しい列'Associated Cases'を作成し、8桁の数字をその列に追加する
df_sfdc['Associated Cases'] = df_sfdc.apply(extract_8digit_num, axis=1)


# NaNがあったらその行を削除
df_sfdc = df_sfdc.dropna()

# 'Associated Cases'列に対して重複排除を行う
df_sfdc = df_sfdc.drop_duplicates(subset=['Associated Cases'])



# Excelファイルからデータを読み込む
df_sla = pd.read_excel('sla_raw_concatinated.xlsx') 

# 必要な列だけ抜き出して、TypeをObjectに合わせる
df_sla = df_sla[['Associated Cases', 'Sender Screen Name (EXTERNAL_VALUE)']].astype(object)

# 'Associated Cases'列をStr型にする
df_sla['Associated Cases'] = df_sla['Associated Cases'].astype(str)

# NaNがあったらその行を削除
df_sla = df_sla.dropna()

# 'Associated Cases'列に対して重複排除を行う
df_sla = df_sla.drop_duplicates(subset=['Associated Cases'])

# 'Associated Cases'をキーとして、df_sfdcを基準にdf_slaをレフトジョインする
merged_df = pd.merge(df_sfdc, df_sla, how='left', on='Associated Cases') 

print(merged_df.head())
print(merged_df.shape)

# 'Customer #'列の値を集計
value_counts = merged_df['Customer #'].value_counts()

# 上位20個の値を取得
top_20 = value_counts.sort_values(ascending=False).head(20)

print(top_20)

# データを棒グラフで表示
plt.figure(figsize=(10,5))
top_20.plot(kind='bar')
# plt.title('Top 20 Customer #')
plt.xlabel('Customer #')
plt.xticks(rotation=55)
plt.ylabel('Frequency')
# グラフの下が切れるのでレイアウトを自動調整
plt.tight_layout()
# グラフをファイル出力
plt.savefig("top-20-customer#.png", format='png')
plt.show()


# 結果を新しいExcelファイルに出力する
merged_df.to_excel('merged.xlsx', index=False)


with open('top-20-customer#.txt', 'w', encoding='UTF-8') as wf:
    # それぞれのCustomer #に何人のどのユーザが属しているかをコンソールに表示
    for k,v in top_20.items():

        # 特定の列の特定の値を持つ行を抽出
        df_filtered = merged_df[merged_df['Customer #'] == k]

        # その行から別の列の値を抽出し、重複を排除
        unique_values = df_filtered['Sender Screen Name (EXTERNAL_VALUE)'].unique()

        # 個数と個別の値を表示
        print(f"{k}, Unique User #: {len(unique_values)}, User Name(s): {unique_values}")

        # 個数と個別の値をファイルに書き出し
        wf.write(f"{k}, Unique User #: {len(unique_values)}, User Name(s): {unique_values}\n")






