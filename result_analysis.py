from utils_algorithm import *
from result_report import analysis

mark = '32.5'

file = f'./data/{prob}_report_{mark}.csv'

content = pd.read_csv(file,index_col=False)

diet = content['0'].tolist()

brk = pd.DataFrame(diet[:brk_len],columns=['num'])
lun = pd.DataFrame(diet[brk_len:lun_pos],columns=['num'])
din = pd.DataFrame(diet[lun_pos:],columns=['num'])

brk['id'] = range(1,brk_len+1)
lun['id'] = range(1,lun_len+1)
din['id'] = range(1,din_len+1)

brk = brk.reindex(columns=['id','num'])
lun = lun.reindex(columns=['id','num'])
din = din.reindex(columns=['id','num'])

brk.to_csv(f'./data/report/brk_{prob}_{mark}.csv',index=False)
lun.to_csv(f'./data/report/lun_{prob}_{mark}.csv',index=False)
din.to_csv(f'./data/report/din_{prob}_{mark}.csv',index=False)

content_path = file[:-4]

analysis(mark)