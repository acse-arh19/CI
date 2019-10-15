import os
import numpy as np
import matplotlib.pyplot as plt

initial_state = np.load(os.sep.join((os.getcwd(),'tests', 'pile_64x64_init.npy')))
final_state = np.load(os.sep.join((os.getcwd(),'tests', 'pile_64x64_final.npy')))
# print(initial_state)
def sandpile (initial_state):
    while np.amax(initial_state>=4):
        sand_fall = np.where(initial_state >= 4)
        for i in range(len(sand_fall[0])):
            a = sand_fall[0][i]
            b = sand_fall[1][i]
            initial_state [a][b] -= 4
            if a != 0 :
                initial_state [a-1][b] += 1 
            if a != initial_state.shape[0]-1:
                initial_state [a+1][b] += 1 
            if b != 0 :
                initial_state [a][b-1] += 1 
            if b != initial_state.shape[0]-1 :
                initial_state [a][b+1] += 1 
    return initial_state

result = sandpile(initial_state) 
print(result == final_state)   
plt.imshow(result)
plt.colorbar()
plt.show()      

