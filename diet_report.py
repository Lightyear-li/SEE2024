from utils_imports import *
from utils_algorithm import *

report = pd.DataFrame(columns=["id", "Energy_kcal", "Water_g", "Protein_g", "Fat_g", "CHO_g", "Fiber_g", "VA_ug", "VB1_mg", "VB2_mg", "VC_mg", "Ca_mg", "Fe_mg", "Zn_mg", "Ile_mg", "Leu_mg", "Lys_mg", "SAA_mg", "AAA_mg", "Thr_mg", "Trp_mg", "Val_mg", "price", "AAS", "Meal_Ratio", "Ratio_error"])

sex = 'male'

if sex=='male':
    ref = ref_male
if sex=='female':
    ref = ref_female

to_preprocess = ['brk','lun','din']

for meal in to_preprocess:
    content = pd.read_csv(f'./data/diet/{sex}_{meal}.csv',index_col=False)
    menu = pd.read_csv(f'./data/menu/menu_{meal}.csv',index_col=False)

    diet = [f'{meal}'] + [0.0] * 25

    for index, row in content.iterrows():
        if row['num']!=0:
            food = row['id']
            num = row['num']
            diet[1]+=menu.loc[menu['id']==food,'Energy_kcal'].values[0] * num
            diet[2]+=menu.loc[menu['id']==food,'Water_g'].values[0] * num
            diet[3]+=menu.loc[menu['id']==food,'Protein_g'].values[0] * num
            diet[4]+=menu.loc[menu['id']==food,'Fat_g'].values[0] * num
            diet[5]+=menu.loc[menu['id']==food,'CHO_g'].values[0] * num
            diet[6]+=menu.loc[menu['id']==food,'Fiber_g'].values[0] * num
            diet[7]+=menu.loc[menu['id']==food,'VA_ug'].values[0] * num
            diet[8]+=menu.loc[menu['id']==food,'VB1_mg'].values[0] * num
            diet[9]+=menu.loc[menu['id']==food,'VB2_mg'].values[0] * num
            diet[10]+=menu.loc[menu['id']==food,'VC_mg'].values[0] * num
            diet[11]+=menu.loc[menu['id']==food,'Ca_mg'].values[0] * num
            diet[12]+=menu.loc[menu['id']==food,'Fe_mg'].values[0] * num
            diet[13]+=menu.loc[menu['id']==food,'Zn_mg'].values[0] * num
            diet[14]+=menu.loc[menu['id']==food,'Ile_mg'].values[0] * num
            diet[15]+=menu.loc[menu['id']==food,'Leu_mg'].values[0] * num
            diet[16]+=menu.loc[menu['id']==food,'Lys_mg'].values[0] * num
            diet[17]+=menu.loc[menu['id']==food,'SAA_mg'].values[0] * num
            diet[18]+=menu.loc[menu['id']==food,'AAA_mg'].values[0] * num
            diet[19]+=menu.loc[menu['id']==food,'Thr_mg'].values[0] * num
            diet[20]+=menu.loc[menu['id']==food,'Trp_mg'].values[0] * num
            diet[21]+=menu.loc[menu['id']==food,'Val_mg'].values[0] * num
            diet[22]+=menu.loc[menu['id']==food,'price'].values[0] * num

    diet[23]=round(min(diet[14]/diet[3]/40, diet[15]/diet[3]/70, diet[16]/diet[3]/55, diet[17]/diet[3]/35, diet[18]/diet[3]/60, diet[19]/diet[3]/40, diet[20]/diet[3]/10, diet[21]/diet[3]/50) * 100, 2)
    report.loc[len(report)] = diet

report.loc[len(report)] = report.apply(lambda x: x.sum())
report.loc[3, 'id'] = 'total'

report.loc[report['id']=='brk', 'Meal_Ratio'] = round(report.loc[report['id']=='brk','Energy_kcal'].values[0] / report.loc[report['id']=='total','Energy_kcal'].values[0] *100, 2)
report.loc[report['id']=='lun', 'Meal_Ratio'] = round(report.loc[report['id']=='lun','Energy_kcal'].values[0] / report.loc[report['id']=='total','Energy_kcal'].values[0] *100, 2)
report.loc[report['id']=='din', 'Meal_Ratio'] = round(report.loc[report['id']=='din','Energy_kcal'].values[0] / report.loc[report['id']=='total','Energy_kcal'].values[0] *100, 2)

report.loc[report['id']=='brk', 'Ratio_error'] = cal_error(report.loc[report['id']=='brk','Meal_Ratio'].values[0], 30)
report.loc[report['id']=='lun', 'Ratio_error'] = cal_error(report.loc[report['id']=='lun','Meal_Ratio'].values[0], 35)
report.loc[report['id']=='din', 'Ratio_error'] = cal_error(report.loc[report['id']=='din','Meal_Ratio'].values[0], 35)

Protein_Percentage = round(report.loc[report['id']=='total','Protein_g'].values[0] * 4 / report.loc[report['id']=='total','Energy_kcal'].values[0], 2)
Fat_Percentage = round(report.loc[report['id']=='total','Fat_g'].values[0] * 9 / report.loc[report['id']=='total','Energy_kcal'].values[0], 2)
CHO_Percentage = round(report.loc[report['id']=='total','CHO_g'].values[0] * 4 / report.loc[report['id']=='total','Energy_kcal'].values[0], 2)

direct = [f'error_%'] + [0] * 25
direct[1] = cal_error(report.loc[report['id']=='total','Energy_kcal'].values[0], ref[0])
direct[3] = cal_error(Protein_Percentage, 0.125)
direct[4] = cal_error(Fat_Percentage, 0.25)
direct[5] = cal_error(CHO_Percentage, 0.55)
direct[7] = cal_error(report.loc[report['id']=='total','VA_ug'].values[0], ref[1])
direct[8] = cal_error(report.loc[report['id']=='total','VB1_mg'].values[0], ref[2])
direct[9] = cal_error(report.loc[report['id']=='total','VB2_mg'].values[0], ref[3])
direct[10] = cal_error(report.loc[report['id']=='total','VC_mg'].values[0], ref[4])
direct[11] = cal_error(report.loc[report['id']=='total','Ca_mg'].values[0], ref[5])
direct[12] = cal_error(report.loc[report['id']=='total','Fe_mg'].values[0], ref[6])
direct[13] = cal_error(report.loc[report['id']=='total','Zn_mg'].values[0], ref[7])

report.loc[len(report)] = direct


dict = pd.read_csv('./data/all_composition.csv',index_col=False)
comps = [0] * 61
types = [False] * 5

for meal in to_preprocess:
    diet = pd.read_csv(f'./data/diet/{sex}_{meal}.csv',index_col=False)
    food = pd.read_csv(f'./data/menu/{meal}.csv',index_col=False)

    for index, row in diet.iterrows():
        if row['num']!=0:
            for indexx, roww in food.iterrows():
                if roww['id']==f'{meal}_{row["id"]}':
                    comp = roww['composition']
                    count = roww['amount'] * row['num']
                    comps[dict.loc[dict['Id']==comp,'Type'].index[0]]+=count
                    types[dict.loc[dict['Id']==comp,'Type'].values[0]-1] = True

count = 0
report.loc[5, 'id'] = ''
report.loc[6, 'id'] = 'Types'
for ii in range(0,5):
    report.loc[7+ii, 'id'] = f'{ii+1}'
    report.loc[7+ii, 'Energy_kcal'] = types[ii]
    if types[ii]==True:
        count+=1
report.loc[6, 'Energy_kcal'] = count
if count==5:
    report.loc[6, 'Water_g'] = 'GOOD'
else:
    report.loc[6, 'Water_g'] = 'BAD'


report.loc[12, 'id'] = ''
report.loc[13, 'id'] = 'Compos'
ii = 0
for index, key in enumerate(comps):
    if key!=0:
        report.loc[14+ii, 'id'] = dict.loc[index, 'Id']
        report.loc[14+ii, 'Energy_kcal'] = key
        ii+=1
report.loc[13, 'Energy_kcal'] = ii
if ii>12:
    report.loc[13, 'Water_g'] = 'GOOD'
else:
    report.loc[13, 'Water_g'] = 'BAD'


report.to_csv(f'./data/report_{sex}.csv',index=False)