from utils_imports import *
from utils_algorithm import *

content = pd.read_csv('./data/menu.csv',index_col=False)

content = cal_energy_macronutrients(content)

content.to_csv('./data/1.csv',index=False)