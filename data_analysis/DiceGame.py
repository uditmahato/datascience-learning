# Numpy is imported, seed is set
import numpy as np
# Starting step
step = 50

# Roll the dice
dice=np.random.randint(1,7)
# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice>=3 and dice<=5:
    step=step-1
else:
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)