from utils_imports import *

to_preprocess = ['brk','lun','din']

for meal in to_preprocess:
    content = pd.read_csv(f'./data/menu/{meal}.csv',index_col=False)

    content['id'] = content['id'].apply(lambda text: f'{meal}_'+str(text))
    content['amount'] = content['amount'] / 100.0

    for index, row in content.iterrows():
        if row['half'] == True:
            id_half = row['id']
            content.loc[index, 'price'] = content.loc[index, 'price'] / 2.0
            content.loc[content['id'] == id_half, 'amount'] = content.loc[content['id'] == id_half, 'amount'] / 2.0

    content.to_csv(f'./data/menu/{meal}.csv',index=False)