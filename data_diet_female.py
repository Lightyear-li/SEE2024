from utils_imports import *

menu = pd.read_csv('./data/menu.csv',index_col=False)

report_female = pd.DataFrame(columns=["id", "Energy_kcal", "Water_g", "Protein_g", "Fat_g", "CHO_g", "Fiber_g", "VA_ug", "VB1_mg", "VB2_mg", "VC_mg", "Ca_mg", "Fe_mg", "Zn_mg", "Ile_mg", "Leu_mg", "Lys_mg", "SAA_mg", "AAA_mg", "Thr_mg", "Trp_mg", "Val_mg", "price", "AAS"])

to_preprocess = ['brk','lun','din']

for meal in to_preprocess:
    content = pd.read_csv(f'./data/diet/female_{meal}.csv',index_col=False)

    diet = [f'{meal}'] + [0] * 23

    for index, row in content.iterrows():
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


    diet[23]=min(diet[14]/diet[3]/40, diet[15]/diet[3]/70, diet[16]/diet[3]/55, diet[17]/diet[3]/35, diet[18]/diet[3]/60, diet[19]/diet[3]/40, diet[20]/diet[3]/10, diet[21]/diet[3]/50)
    report_female.loc[len(report_female)] = diet

report_female.loc[len(report_female)] = report_female.apply(lambda x: x.sum())
report_female.loc[3, 'id'] = 'total'

report_female.loc[5, 'id'] = ''
report_female.loc[6, 'id'] = 'Energy_Percentage'
report_female.loc[7, 'id'] = 'brk'
report_female.loc[7, 'Energy_kcal'] = report_female.loc[report_female['id']=='brk','Energy_kcal'].values[0] / report_female.loc[report_female['id']=='total','Energy_kcal'].values[0]
report_female.loc[8, 'id'] = 'lun'
report_female.loc[8, 'Energy_kcal'] = report_female.loc[report_female['id']=='lun','Energy_kcal'].values[0] / report_female.loc[report_female['id']=='total','Energy_kcal'].values[0]
report_female.loc[9, 'id'] = 'din'
report_female.loc[9, 'Energy_kcal'] = report_female.loc[report_female['id']=='din','Energy_kcal'].values[0] / report_female.loc[report_female['id']=='total','Energy_kcal'].values[0]

report_female.loc[10, 'id'] = ''
report_female.loc[11, 'id'] = 'Main_Percentage'
report_female.loc[12, 'id'] = 'Protein'
report_female.loc[12, 'Energy_kcal'] = report_female.loc[report_female['id']=='total','Protein_g'].values[0] * 4 / report_female.loc[report_female['id']=='total','Energy_kcal'].values[0]
report_female.loc[13, 'id'] = 'Fat'
report_female.loc[13, 'Energy_kcal'] = report_female.loc[report_female['id']=='total','Fat_g'].values[0] * 9 / report_female.loc[report_female['id']=='total','Energy_kcal'].values[0]
report_female.loc[14, 'id'] = 'CHO'
report_female.loc[14, 'Energy_kcal'] = report_female.loc[report_female['id']=='total','CHO_g'].values[0] *4 / report_female.loc[report_female['id']=='total','Energy_kcal'].values[0]

report_female.loc[15, 'id'] = ''
report_female.loc[16, 'id'] = 'AAS'
report_female.loc[17, 'id'] = 'brk'
report_female.loc[17, 'Energy_kcal'] = report_female.loc[report_female['id']=='brk','AAS'].values[0] * 100
report_female.loc[18, 'id'] = 'lun'
report_female.loc[18, 'Energy_kcal'] = report_female.loc[report_female['id']=='lun','AAS'].values[0] * 100
report_female.loc[19, 'id'] = 'din'
report_female.loc[19, 'Energy_kcal'] = report_female.loc[report_female['id']=='din','AAS'].values[0] * 100



report_female.to_csv('./data/report_female.csv',index=False)
