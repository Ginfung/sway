# SWAY - The Sampling WAY
 
## What is Sway?
SWAY, the Sampling WAY, is baseline optimizer for multi-objective optimization problems, especially for the search-based software engineering problems.
SWAY does not have the crossover and mutation in the standard evolutionary algorithm. Instead, it samples from a large candidate pool.

## Reference
```
@article{chen2016sampling,
  title={Is" Sampling" better than" Evolution" for Search-based Software Engineering?},
  author={Chen, Jianfeng and Nair, Vivek and Krishna, Rahul and Menzies, Tim},
  journal={arXiv preprint arXiv:1608.07617},
  year={2016}
}
```

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

# To create an individual is easy!
rand_ind = MyIndividual([1,2,3,4,5,6])

# Define your own evaluation function
def modelEvaluation(ind):
  decs = ind  # now we can treat decs as the list
  ind.fitness.values = (1.1, 2.2, 3.3, 4.4) # change (1.1, 2.2, 3.3, 4.4) here
```
Step 3- Enjoy the sway to serach for optimum

```python
from Algorithms import sway_continous, sway_discrete
init = ... # TODO list of initial candidates
res = sway_continous.optimize(init, modelEvaluation)
for i in res:
  print(i.fitness.values)
```
