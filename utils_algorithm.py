from utils_imports import *

def cal_energy_macronutrients(data):
    data['Protein_energy'] = data['Protein_g'] * 4
    data['Fat_energy'] = data['Fat_g'] * 9
    data['CHO_energy'] = data['CHO_g'] * 4
    data['Protein_energy_percentage'] = data['Protein_energy'] / data['Energy_kcal']
    data['Fat_energy_percentage'] = data['Fat_energy'] / data['Energy_kcal']
    data['CHO_energy_percentage'] = data['CHO_energy'] / data['Energy_kcal']
    return data

