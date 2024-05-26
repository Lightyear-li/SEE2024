from utils_algorithm import *

dict = pd.read_csv('./data/all_composition.csv',index_col=False)

to_preprocess = ['brk','lun','din']
food_count = {'brk':33,'lun':59,'din':49}

for meal in to_preprocess:
    content = pd.read_csv(f'./data/{menu_folder}/{meal}.csv',index_col=False)
    content['type'] = 0
    content['pos'] = 0
    for index, row in content.iterrows():
        comp = row['composition']
        content.type[index] = dict.loc[dict['Id']==comp, 'Type'].values[0]
        content.pos[index] = dict.loc[dict['Id']==comp, 'Type'].index[0]

    content.to_csv(f'./data/{menu_folder}/{meal}.csv',index=False)