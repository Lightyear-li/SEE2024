from utils_imports import *

flag = 0

ref_male = [2400,800,1.4,1.4,100,800,12,12.5]
ref_female = [1900,700,1.2,1.2,100,800,20,7.5]

prob = 'Price'

sex='female'
if sex=='male':
    ref = ref_male
if sex=='female':
    ref = ref_female

mode='origin'
if mode=='new':
    menu_folder = 'menu_new'
    diet_folder = 'diet_new'
    brk_len = 14
    lun_len = 10
    din_len = 11
    lun_pos = 24
    x_n=35
    kk=4
    MUTPB = 0.4
if mode=='origin':
    menu_folder = 'menu_origin'
    diet_folder = 'diet_origin'
    brk_len = 33
    lun_len = 59
    din_len = 49
    lun_pos = 92
    x_n=141
    kk=14
    MUTPB = 0.1 


mapping_brk = [1,2,5,12,13,14,15,16,17,18,19,23,26,28]
mapping_lun = [6,10,13,19,28,35,39,44,48,54]
mapping_din = [9,11,12,14,15,24,29,30,32,41,43]

dict = pd.read_csv('./data/all_composition.csv',index_col=False)
comp_brk = pd.read_csv(f'./data/{menu_folder}/brk.csv',index_col=False).drop('half',axis=1).drop('price',axis=1)
comp_lun = pd.read_csv(f'./data/{menu_folder}/lun.csv',index_col=False).drop('half',axis=1).drop('price',axis=1)
comp_din = pd.read_csv(f'./data/{menu_folder}/din.csv',index_col=False).drop('half',axis=1).drop('price',axis=1)
menu_brk = pd.read_csv(f'./data/{menu_folder}/menu_brk.csv',index_col=False).drop('id',axis=1).drop('half',axis=1).to_numpy()
menu_lun = pd.read_csv(f'./data/{menu_folder}/menu_lun.csv',index_col=False).drop('id',axis=1).drop('half',axis=1).to_numpy()
menu_din = pd.read_csv(f'./data/{menu_folder}/menu_din.csv',index_col=False).drop('id',axis=1).drop('half',axis=1).to_numpy()

def cal_error(num, standard):
    ans = round((num - standard) /standard * 100, 2)
    return ans

def normalize(col):
    return (col - col.min()) / (col.max() - col.min())