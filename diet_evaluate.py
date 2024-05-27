from utils_algorithm import *


def evaluation(data):
    start_time = time.time()
    report = pd.DataFrame(columns=["id", "Energy_kcal", "Water_g", "Protein_g", "Fat_g", "CHO_g", "Fiber_g", "VA_ug", "VB1_mg", "VB2_mg", "VC_mg", "Ca_mg", "Fe_mg", "Zn_mg", "Ile_mg", "Leu_mg", "Lys_mg", "SAA_mg", "AAA_mg", "Thr_mg", "Trp_mg", "Val_mg", "price", "AAS", "Meal_Ratio", "Ratio_error"])
    
    brk=data[:33]
    lun=data[33:92]
    din=data[92:]
    
    if sex=='male':
        ref = ref_male
    if sex=='female':
        ref = ref_female

    to_preprocess = ['brk','lun','din']
    to_content = [brk,lun,din]

    for index, meal in enumerate(to_preprocess):
        content = to_content[index]
        menu = pd.read_csv(f'./data/menu/menu_{meal}.csv',index_col=False)

        diet = [f'{meal}'] + [0.0] * 25

        for indexx, num in enumerate(content):
            if num!=0:
                food = indexx + 1
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

    Protein_Ratio_brk = round(report.loc[report['id']=='brk','Protein_g'].values[0] / report.loc[report['id']=='total','Protein_g'].values[0], 2)
    Protein_Ratio_lun = round(report.loc[report['id']=='lun','Protein_g'].values[0] / report.loc[report['id']=='total','Protein_g'].values[0], 2)
    Protein_Ratio_din = round(report.loc[report['id']=='din','Protein_g'].values[0] / report.loc[report['id']=='total','Protein_g'].values[0], 2)

    Protein_Percentage = round(report.loc[report['id']=='total','Protein_g'].values[0] * 4 / report.loc[report['id']=='total','Energy_kcal'].values[0], 2)
    Fat_Percentage = round(report.loc[report['id']=='total','Fat_g'].values[0] * 9 / report.loc[report['id']=='total','Energy_kcal'].values[0], 2)
    CHO_Percentage = round(report.loc[report['id']=='total','CHO_g'].values[0] * 4 / report.loc[report['id']=='total','Energy_kcal'].values[0], 2)

    Energy_error = abs(cal_error(report.loc[report['id']=='total','Energy_kcal'].values[0], ref[0]))
    Protein_error = abs(cal_error(Protein_Percentage, 0.125))
    Fat_error = abs(cal_error(Fat_Percentage, 0.25))
    CHO_error = abs(cal_error(CHO_Percentage, 0.575))
    VA_error = abs(cal_error(report.loc[report['id']=='total','VA_ug'].values[0], ref[1]))
    VB1_error = abs(cal_error(report.loc[report['id']=='total','VB1_mg'].values[0], ref[2]))
    VB2_error = abs(cal_error(report.loc[report['id']=='total','VB2_mg'].values[0], ref[3]))
    VC_error = abs(cal_error(report.loc[report['id']=='total','VC_mg'].values[0], ref[4]))
    Ca_error = abs(cal_error(report.loc[report['id']=='total','Ca_mg'].values[0], ref[5]))
    Fe_error = abs(cal_error(report.loc[report['id']=='total','Fe_mg'].values[0], ref[6]))
    Zn_error = abs(cal_error(report.loc[report['id']=='total','Zn_mg'].values[0], ref[7]))

    Ratio_error_brk = abs(cal_error(report.loc[report['id']=='brk','Meal_Ratio'].values[0], 30))
    Ratio_error_lun = abs(cal_error(report.loc[report['id']=='lun','Meal_Ratio'].values[0], 35))
    Ratio_error_din = abs(cal_error(report.loc[report['id']=='din','Meal_Ratio'].values[0], 35))

    AAS_report = (report.loc[report['id']=='brk', 'AAS'].values[0] * Protein_Ratio_brk + report.loc[report['id']=='lun', 'AAS'].values[0] * Protein_Ratio_lun + report.loc[report['id']=='din', 'AAS'].values[0] * Protein_Ratio_din)
    Price_report = report.loc[report['id']=='total', 'price'].values[0]


    dict = pd.read_csv('./data/all_composition.csv',index_col=False)
    comps = [0] * 61
    types = [False] * 5

    for index,meal in enumerate(to_preprocess):
        diet = to_content[index]
        food = pd.read_csv(f'./data/menu/{meal}.csv',index_col=False)

        for indexx, num in enumerate(diet):
            if num!=0:
                for indexxx, roww in food.iterrows():
                    if roww['id']==f'{indexx+1}':
                        comp = roww['composition']
                        count = roww['amount'] * num
                        comps[dict.loc[dict['Id']==comp,'Type'].index[0]]+=count
                        types[dict.loc[dict['Id']==comp,'Type'].values[0]-1] = True

    count = 0
    for ii in range(0,5):
        if types[ii]==True:
            count+=1
    Type_report = int(count==5)

    ii = 0
    for index, key in enumerate(comps):
        if key!=0:
            ii+=1
    Comps_report = int(ii>=12)

    runtime = time.time() - start_time

    if Comps_report==False or Type_report==False or Energy_error>10 or Protein_error>20 or Fat_error>20 or CHO_error>13 or VA_error>30 or VB1_error>30 or VB2_error>30 or VC_error>30 or Ca_error>30 or Fe_error>30 or Zn_error>30 or Ratio_error_brk>16.7 or Ratio_error_lun>14.3 or Ratio_error_din>14.3:
        AAS_report = 0

    if flag:
        print(Energy_error, Protein_error, Fat_error, CHO_error, VA_error, VB1_error, VB2_error, VC_error, Ca_error, Fe_error, Zn_error, Ratio_error_brk, Ratio_error_lun, Ratio_error_din, AAS_report, Price_report, Type_report, Comps_report, runtime)
    else:
        # print(daily[0])
        # print(Energy_error, Protein_error, Fat_error, CHO_error, VA_error, VB1_error, VB2_error, VC_error, Ca_error, Fe_error, Zn_error, Ratio_error_brk, Ratio_error_lun, Ratio_error_din, AAS_report, Price_report, Type_report, Comps_report, runtime)
        return [AAS_report]

if __name__=='__main__':
    flag = 1
    brk = pd.read_csv(f'./data/{diet_folder}/{sex}_brk.csv',index_col=False)
    brk = brk['num'].tolist()
    lun = pd.read_csv(f'./data/{diet_folder}/{sex}_lun.csv',index_col=False)
    lun = lun['num'].tolist()
    din = pd.read_csv(f'./data/{diet_folder}/{sex}_din.csv',index_col=False)
    din = din['num'].tolist()

    data = brk + lun + din

    evaluation(data)