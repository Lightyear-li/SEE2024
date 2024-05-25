from utils_imports import *

ref_male = [2400,800,1.4,1.4,100,800,12,12.5]
ref_female = [1900,700,1.2,1.2,100,800,20,7.5]

def cal_energy_macronutrients(data):
    data['Protein_energy'] = data['Protein_g'] * 4
    data['Fat_energy'] = data['Fat_g'] * 9
    data['CHO_energy'] = data['CHO_g'] * 4
    data['Protein_energy_percentage'] = data['Protein_energy'] / data['Energy_kcal']
    data['Fat_energy_percentage'] = data['Fat_energy'] / data['Energy_kcal']
    data['CHO_energy_percentage'] = data['CHO_energy'] / data['Energy_kcal']
    return data

def cal_error(num, standard):
    ans = round((num - standard) /standard * 100, 2)
    return ans