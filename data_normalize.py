from utils_imports import *
from utils_algorithm import *

df = pd.read_csv(f'./data/menu.csv',index_col=False)

for index, col_name in enumerate(df.columns):
    if index not in [0,22,23]:
        df[col_name] = df[col_name].transform(normalize)


df.to_csv(f'./data/menu_normalize.csv',index=False)