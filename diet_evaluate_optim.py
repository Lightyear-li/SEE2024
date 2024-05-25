from utils_algorithm import *

def evaluation(data):
    start_time = time.time()

    data = [int(text) for text in data]
    
    brk=np.array(data[:brk_len])[:,np.newaxis]
    lun=np.array(data[brk_len:lun_len])[:,np.newaxis]
    din=np.array(data[lun_len:])[:,np.newaxis]

    to_preprocess = ['brk','lun','din']
    to_diet = [brk,lun,din]
    to_menu = [menu_brk,menu_lun,menu_din]
    to_food = [comp_brk,comp_lun,comp_din]
    to_mapp = [mapping_brk,mapping_lun,mapping_din]
    report = np.empty((3,25))

    comps = [0] * 61
    types = [False] * 5

    for index, meal in enumerate(to_preprocess):
        diet = to_diet[index]
        menu = to_menu[index]
        # food = to_food[index]
        # mapp = to_mapp[index]

        ans = diet * menu
        ans = np.around(np.sum(ans,axis=0), 2)

        AAS = round(min(ans[13]/ans[2]/40, ans[14]/ans[2]/70, ans[15]/ans[2]/55, ans[16]/ans[2]/35, ans[17]/ans[2]/60, ans[18]/ans[2]/40, ans[19]/ans[2]/10, ans[20]/ans[2]/50) * 100, 2)

        report[index,0:22] = ans
        report[index,22] = AAS

        # diet = diet.flatten().tolist()
        # for indexx, num in enumerate(diet):
        #     if num!=0:
        #         for indexxx, roww in food.iterrows():
        #             if roww['id']==f'{meal}_{indexx+1}':
        #             # if roww['id']==f'{meal}_{mapp[indexx]}':#因为mapping也是从0开始的
        #                 comp = roww['composition']
        #                 count = roww['amount'] * num
        #                 comps[dict.loc[dict['Id']==comp,'Type'].index[0]]+=count
        #                 types[dict.loc[dict['Id']==comp,'Type'].values[0]-1] = True

    daily = np.around(np.sum(report,axis=0), 2)

    Ratio_error_brk = abs(cal_error(round(report[0,0] / daily[0] * 100, 2), 30))
    Ratio_error_lun = abs(cal_error(round(report[1,0] / daily[0] * 100, 2), 35))
    Ratio_error_din = abs(cal_error(round(report[2,0] / daily[0] * 100, 2), 35))

    Protein_error = abs(cal_error(round(daily[2] *4 / daily[0], 2), 0.125))
    Fat_error = abs(cal_error(round(daily[3] *9 / daily[0], 2), 0.25))
    CHO_error = abs(cal_error(round(daily[4] *4 / daily[0], 2), 0.575))

    Energy_error = abs(cal_error(daily[0], ref[0]))
    VA_error = abs(cal_error(daily[6], ref[1]))
    VB1_error = abs(cal_error(daily[7], ref[2]))
    VB2_error = abs(cal_error(daily[8], ref[3]))
    VC_error = abs(cal_error(daily[9], ref[4]))
    Ca_error = abs(cal_error(daily[10], ref[5]))
    Fe_error = abs(cal_error(daily[11], ref[6]))
    Zn_error = abs(cal_error(daily[12], ref[7]))

    AAS_report = round((report[0,22]*report[0,2] + report[1,22]*report[1,2] + report[2,22]*report[2,2]) / daily[2], 2)
    Price_report = daily[21]

    # count = 5 - types.count(False)
    # Type_report = count==5
    Type_report = True

    # count = 61 - comps.count(0)
    # Comps_report = count>=12
    Comps_report = True

    runtime = round(time.time() - start_time, 6)

    # if Comps_report==False or Type_report==False or Energy_error>10 or Protein_error>20 or Fat_error>20 or CHO_error>13 or VA_error>30 or VB1_error>30 or VB2_error>30 or VC_error>30 or Ca_error>30 or Fe_error>30 or Zn_error>30 or Ratio_error_brk>16.7 or Ratio_error_lun>14.3 or Ratio_error_din>14.3:
    if Comps_report==False or Type_report==False or Energy_error>10 :#or Protein_error>20 or Fat_error>20  or CHO_error>13 :
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