'''
    India Ausie
'''
from calculator import add,sub
import sys

print('\n\n')
print("#"*20)
print('World Cup Finals')
print("#"*20)
def get_scores():
    aus_inn1_run = int(sys.argv[1]) ##250
    ind_inn1_run = int(sys.argv[2]) ##220
    aus_inn2_run = int(sys.argv[3]) ##150
    return aus_inn1_run, ind_inn1_run, aus_inn2_run

def find_target():
    tot_aus_run = add(aus_inn1_run, aus_inn2_run)
    return add(sub(tot_aus_run , ind_inn1_run),1)

if __name__ == "__main__":
    print('Aus Innings 1:',aus_inn1_run)
    print('India Innings 1:', ind_inn1_run)
    print('Aus Innings 2:', aus_inn2_run)
    print("Runs Required by India:", add(sub(tot_aus_run , ind_inn1_run),1) )
