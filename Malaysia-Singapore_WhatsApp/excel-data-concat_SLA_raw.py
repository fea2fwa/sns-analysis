import os
import pandas as pd

# Excelファイルがあるディレクトリを指定します
directory = './data'

# 結合したいシートの名前をリストで指定します
# sheet_names_to_concat = ['SFDC_raw', 'Survey_raw', 'SLA_raw']
sheet_names_to_concat = ['SLA_raw']

# すべてのデータを格納するための空のDataFrameを作成します
all_data = pd.DataFrame()

# 指定したディレクトリ内のすべてのファイルをループします
for filename in os.listdir(directory):
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        # ファイルパスを作成します
        file_path = os.path.join(directory, filename)
        
        # Excelファイル内の各シートをループします
        with pd.ExcelFile(file_path) as xls:
            for sheet_name in xls.sheet_names:
                # シートが結合対象のものであれば
                if sheet_name in sheet_names_to_concat:
                    # シートのデータをDataFrameに読み込みます
                    df = pd.read_excel(xls, sheet_name=sheet_name)
                    # そのデータを全体のDataFrameに追加します
                    all_data = pd.concat([all_data, df])
                    print(all_data)

# 最終結果をExcel形式で保存します
all_data.to_excel('sla_raw_concatinated_sgmy.xlsx', index=False)

