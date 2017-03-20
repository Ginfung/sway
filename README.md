# sway

## How to use sway?
Step 1- Clone this repo  
Step 2- Define your own problem!  
SWAY accpets the problems defnied in [DEAP](http://deap.readthedocs.io/en/master/index.html)  
The following is a very simple guide to use DEAP  

After import the DEAP module, you should define the objective space and decision space.  
Here we defined 4D minimization objectives and the list as decision space  
_For details on [typecode here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.typename.html)_

```python
from deap import base, creator, tools
creator.create('AllToMin', base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0))
creator.create('MyIndividual', array.array, typecode='d', fitness=creator.FitnessMin)

# This is the definition of model evaluation
def modelEvaluation(ind):
  decs = ind  # now we can treat decs as the list
  # TODO add the model evaluation here...
  ind.fitness.values = (1,2,3,4)

rand_ind = MyIndividual([1,2,3,4,5,6])
```
Step 3- Enjoy the sway to serach for optimum

```python
from Algorithms import sway_continous, sway_discrete
init = ... # TODO list of initial candidates
res = sway_continous.optimize(init, modelEvaluation)
for i in res:
  print(i.fitness.values)
```
