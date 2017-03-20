# sway

## How to use sway?
Step 1- Clone this repo  
Step 2- Define your own problem!  
SWAY accpets the problems defnied in [DEAP](http://deap.readthedocs.io/en/master/index.html)  
The following is a very simple guide to use DEAP  
```python
from deap import base, creator, tools
creator.create('AllToMin', base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0))
creator.create('MyIndividual', array.array, typecode='d', fitness=creator.FitnessMin)

def modelEvaluation(ind):
  decs = ind
  # TODO add the model evaluation here
  # ...
  
  ind.fitness.values = (1,2,3,4)
```


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
