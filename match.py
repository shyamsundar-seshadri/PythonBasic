'''
    India Ausie
'''
from calculator import add,sub


print('\n\n')
print("#"*20)
print('World Cup Finals')
print("#"*20)
aus_inn1_run = 250
ind_inn1_run = 220
aus_inn2_run = 150
tot_aus_run = add(aus_inn1_run, aus_inn2_run)
print('Aus Innings 1:',aus_inn1_run)
print('India Innings 1:', ind_inn1_run)
print('Aus Innings 2:', aus_inn2_run)
print("Runs Required by India:", add(sub(tot_aus_run , ind_inn1_run),1) )
