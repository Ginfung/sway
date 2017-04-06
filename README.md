# SWAY - The Sampling WAY
 
## What is SWAY?
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

## How to use SWAY?
* Clone this repo
* Define your own problem!
* Create the initial candidate pool.
* Use SWAY 

In the following example, we create our own problem `Networking` with 4-dimension objectives `QoS` and use SWAY to search for optimum.



SWAY accpets the problems defnied in [DEAP](http://deap.readthedocs.io/en/master/index.html)  


```python
from Algorithms import sway_continous, sway_discrete
from deap import base, creator, tools

creator.create('Qos', base.Fitness, weights=(-1.0, -1.0, -1.0, -1.0))  # note-a
creator.create('Networking', array.array, typecode='d', fitness=creator.Qos)  # note-b

def modelEvaluation(ind):
  ind.fitness.values = (1.1, 2.2, 3.3, 4.4) # note-c

init = ... # note-d

res = sway_continous.optimize(init, modelEvaluation)

for i in res:
  print(i.fitness.values)
```

a)  _[what is Fitneess? weights](http://deap.readthedocs.io/en/master/tutorials/basic/part1.html)_ 
b) _[what is typecode?](https://docs.scipy.org/doc/numpy/reference/generated/numpy.typename.html)_  
c) The objective of individual is assigned "in-place".
The decision of the _ind_ can be accessed by `ind[0], ind[1],...`  
d) Creating the candidates pool and put all into a list. A candidate can be created by `Networking([1,2,3,4,5,6])`
