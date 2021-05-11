import pandas as pd

#file_path = "./result_data/prefectures_japan.csv"
file_path = "./result_data/prefectures_japan_value.csv"
df_japan = pd.read_csv(file_path)
df_japan_prefectures_group = df_japan.groupby('prefectures')
df_japan_propety_group = df_japan.groupby('propety')
# print(df_japan_prefectures_group.size())
print(df_japan_prefectures_group.size().sort_values(ascending=False))
print(df_japan_propety_group.size().sort_values(ascending=False))
