# sway

## How to use sway?
Step 1- Clone this repo  
Step 2- Define your own problem!  
SWAY accpets the problems defnied in [DEAP](http://deap.readthedocs.io/en/master/index.html)  
The following is a very simple guide to use DEAP  
```python
from deap import base, creator, tools

# After import the DEAP module, you should define the objective space and decision space.
# e.g. here we have 4D minization objectives and the array as decision space
creator.create('AllToMin', base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0))
creator.create('MyIndividual', array.array, typecode='d', fitness=creator.FitnessMin)

# This is the definition of model evaluation
def modelEvaluation(ind):
  decs = ind
  # TODO add the model evaluation here...
  ind.fitness.values = (1,2,3,4)

# This demostrate how to create an individual
def random_pop():
  return MyIndividual([1,2,3,4,5,6])
```


```python
from Algorithms import sway_continous, sway_discrete
# generate initial candidates
init = ... # 
res = sway_continous.optimize(init, XOMO_OSP.eval)
# print results
for i in res:
  print(i.fitness.values)
```
