# sway

## How to use sway?
Step 1- clone this repo  
```python
from Algorithms import sway_continous, sway_discrete
# generate initial candidates
init = generate_random_init(XOMO_OSP, 10000)
# call the sway
res = sway_continous.optimize(init, XOMO_OSP.eval)
# print results
for i in res:
  print(i.fitness.values)
```
