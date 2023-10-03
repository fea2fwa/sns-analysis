import pandas as pd

# 結果をExcelファイルからインポート
merged_df = pd.read_excel('merged.xlsx') 
top_20 = pd.read_excel('top_20.xlsx') 


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