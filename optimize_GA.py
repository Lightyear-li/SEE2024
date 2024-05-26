from utils_algorithm import *
from diet_evaluate_optim import evaluation

# 定义问题参数
NGEN = 10    # 迭代次数
MU = 50000     # 种群大小
CXPB = 0.8   # 交叉概率
NELITE = 10  # 精英个数

# 定义遗传算法函数

def generate_individual():
    individual_brk = [0] * brk_len
    non_zero_indices = rn.sample(range(brk_len), rn.randint(2, 6))
    for index in non_zero_indices:
        individual_brk[index] = rn.randint(1, 3)

    individual_lun = [0] * lun_len
    non_zero_indices = rn.sample(range(lun_len), rn.randint(2, 6))
    for index in non_zero_indices:
        individual_lun[index] = rn.randint(1, 3)

    individual_din = [0] * din_len
    non_zero_indices = rn.sample(range(din_len), rn.randint(2, 6))
    for index in non_zero_indices:
        individual_din[index] = rn.randint(1, 3)
    
    individual = individual_brk + individual_lun + individual_din

    return individual

def evaluate_population(population):
    return [evaluation(individual) for individual in population]

def select_elites(population, scores):
    elite_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:NELITE]
    return [population[i] for i in elite_indices]

def crossover(parent1, parent2):
    crossover_point = rn.randint(1, x_n - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    mutated_individual = individual[:]
    indices = rn.sample(range(x_n), k=kk)
    for i in indices:
        if mutated_individual[i]==0:
            if rn.random() < MUTPB:
                mutated_individual[i] = rn.randint(1, 4)
        else:
            mutated_individual[i] = 0
    return mutated_individual

def genetic_algorithm():
    population = [generate_individual() for _ in range(MU)]
    for index in range(NGEN):
        t = time.time()
        scores = evaluate_population(population)
        elites = select_elites(population, scores)
        best_gen = -evaluation(elites[0])[0]
        t = time.time() - t

        for results in elites:
            gen = -evaluation(results)[0]
            print(f'''GEN:{index}  runtime:{t}''')
            print(f'''elites:{results}''')
            print(f'''score:{gen}''')
            if gen<50:
                pd.DataFrame(results).to_csv(f'./data/{prob}_report_{gen}.csv')
        if best_gen>50:
            return 0, 0
        next_generation = elites[:]
        while len(next_generation) < MU:
            parent1, parent2 = rn.choices(population, k=2)
            # child1, child2 = crossover(parent1, parent2)
            # child1 = mutate(child1)
            # child2 = mutate(child2)
            child1 = mutate(parent1)
            child2 = mutate(parent2)
            next_generation.extend([child1, child2])
        population = next_generation

    best_individual = max(population, key=lambda x: evaluation(x))
    best_score = -evaluation(best_individual)
    repeat = False
    return best_individual, best_score

if __name__=='__main__':
    repeat = True
    while(repeat):
        best_solution, best_score = genetic_algorithm()

    print("Best solution:", best_solution)
    print("Best score:", best_score)
