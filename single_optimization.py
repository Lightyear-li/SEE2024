from utils_imports import *
from diet_evaluate import *


prob = pulp.LpProblem("Max_ASS", pulp.LpMaximize)

x = [pulp.LpVariable(f'x{i}', lowBound=0, upBound=10, cat='Integer') for i in range(1, 141)]

# [Energy_error, Protein_error, Fat_error, CHO_error, VA_error, VB1_error, VB2_error, VC_error, Ca_error, Fe_error, Zn_error, Ratio_error_brk, Ratio_error_lun, Ratio_error_din, AAS_report, Price_report, Type_report, Comps_report] = evaluation('male',x[:33],x[33:92],x[92:])

prob += evaluation(x)[14]

prob += evaluation(x)[0]<10
prob += evaluation(x)[1]<20
prob += evaluation(x)[2]<20
prob += evaluation(x)[3]<13
prob += evaluation(x)[4]<30
prob += evaluation(x)[5]<30
prob += evaluation(x)[6]<30
prob += evaluation(x)[7]<30
prob += evaluation(x)[8]<30
prob += evaluation(x)[9]<30
prob += evaluation(x)[10]<30
prob += evaluation(x)[11]<16.7
prob += evaluation(x)[12]<14.3
prob += evaluation(x)[13]<14.3
prob += evaluation(x)[16]>=0.5
prob += evaluation(x)[17]>=0.5

prob.solve()

print("Optimal values:")
for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Maximum y1 value:", pulp.value(prob.objective))
