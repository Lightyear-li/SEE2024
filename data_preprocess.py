from utils_imports import *

dict = pd.read_csv('./data/all_composition.csv',index_col=False)

to_preprocess = ['brk','lun','din']
food_count = {'brk':34,'lun':59,'din':49}

for meal in to_preprocess:
    content = pd.read_csv(f'./data/menu/{meal}.csv',index_col=False)

    menu = pd.DataFrame(columns=["id", "Energy_kcal", "Water_g", "Protein_g", "Fat_g", "CHO_g", "Fiber_g", "VA_ug", "VB1_mg", "VB2_mg", "VC_mg", "Ca_mg", "Fe_mg", "Zn_mg", "Ile_mg", "Leu_mg", "Lys_mg", "SAA_mg", "AAA_mg", "Thr_mg", "Trp_mg", "Val_mg", "price", "half"])

    for food_no in range(1,food_count[meal]+1):
        food = [f'{food_no}'] + [0] * 21

        for index, row in content.iterrows():
            if row['id']==f'{meal}_{food_no}':
                comp = row['composition']
                part = row['amount']
                price = row['price']
                half = row['half']
                food[1]+=dict.loc[dict['Id']==comp,'Energy_kcal'].values[0] * part
                food[2]+=dict.loc[dict['Id']==comp,'Water_g'].values[0] * part
                food[3]+=dict.loc[dict['Id']==comp,'Protein_g'].values[0] * part
                food[4]+=dict.loc[dict['Id']==comp,'Fat_g'].values[0] * part
                food[5]+=dict.loc[dict['Id']==comp,'CHO_g'].values[0] * part
                food[6]+=dict.loc[dict['Id']==comp,'Fiber_g'].values[0] * part
                food[7]+=dict.loc[dict['Id']==comp,'VA_ug'].values[0] * part
                food[8]+=dict.loc[dict['Id']==comp,'VB1_mg'].values[0] * part
                food[9]+=dict.loc[dict['Id']==comp,'VB2_mg'].values[0] * part
                food[10]+=dict.loc[dict['Id']==comp,'VC_mg'].values[0] * part
                food[11]+=dict.loc[dict['Id']==comp,'Ca_mg'].values[0] * part
                food[12]+=dict.loc[dict['Id']==comp,'Fe_mg'].values[0] * part
                food[13]+=dict.loc[dict['Id']==comp,'Zn_mg'].values[0] * part
                food[14]+=dict.loc[dict['Id']==comp,'Ile_mg'].values[0] * part
                food[15]+=dict.loc[dict['Id']==comp,'Leu_mg'].values[0] * part
                food[16]+=dict.loc[dict['Id']==comp,'Lys_mg'].values[0] * part
                food[17]+=dict.loc[dict['Id']==comp,'SAA_mg'].values[0] * part
                food[18]+=dict.loc[dict['Id']==comp,'AAA_mg'].values[0] * part
                food[19]+=dict.loc[dict['Id']==comp,'Thr_mg'].values[0] * part
                food[20]+=dict.loc[dict['Id']==comp,'Trp_mg'].values[0] * part
                food[21]+=dict.loc[dict['Id']==comp,'Val_mg'].values[0] * part
        
        food.append(price)
        food.append(half)
            
        menu.loc[len(menu)] = food

    menu.to_csv(f'./data/menu_{meal}.csv',index=False)
                

