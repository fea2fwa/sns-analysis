import pandas as pd

# Excelファイルを読み込む
df = pd.read_excel("sla_raw_concatinated_india.xlsx")

# 特定の列を選択
column_data_inbound = df['Inbound Message'].values
column_data_outbound = df['Replied Post'].values

# テキストファイルに書き出す
with open('chatmessages-inbound_india.txt', 'w', encoding='utf-8') as f:
    for item in column_data_inbound:
        f.write("%s\n" % item)

with open('chatmessages-outbound_india.txt', 'w', encoding='utf-8') as f:
    for item in column_data_outbound:
        f.write("%s\n" % item)
