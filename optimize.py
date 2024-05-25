from utils_algorithm import *
from diet_evaluate_optim import evaluation


# 创建适应度类和个体类  
creator.create("FitnessMax", base.Fitness, weights=(1.0,))  # 只关心y1的最大值  
creator.create("Individual", list, fitness=creator.FitnessMax)  
  
# 初始化种群  
toolbox = base.Toolbox()  
toolbox.register("attr_int", rn.randint, 0, 3)  # 假设x1...x141的取值范围是0到10（根据实际情况调整）  
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=x_n)  
toolbox.register("population", tools.initRepeat, list, toolbox.individual)  
  
# 注册评估函数  
toolbox.register("evaluate", evaluation)  
toolbox.register("mate", tools.cxTwoPoint)  
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)  
toolbox.register("select", tools.selNSGA2)  # 如果需要处理多目标，可以使用NSGA-II，但这里我们只关心y1  

# 遗传算法参数  
NGEN = 100  # 迭代次数  
MU = 50     # 种群大小  
CXPB = 0.5  # 交叉概率  
MUTPB = 0.2 # 变异概率  
  
# 运行遗传算法  
pop = toolbox.population(n=MU)  
hof = tools.HallOfFame(1)  # 用于存储最优解  
stats = tools.Statistics(lambda ind: ind.fitness.values)  
stats.register("avg", np.mean, axis=0)  
stats.register("std", np.std, axis=0)  
stats.register("min", np.min, axis=0)  
stats.register("max", np.max, axis=0)  
  
pop, log = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, stats=stats, halloffame=hof, verbose=True)  
  
# 输出最优解  
best = hof[0]
best_y = best.fitness.values
best_x = [int(text) for text in best]
print("Best individual is", best_x)  
print("Fitness:", best_y)