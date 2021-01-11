# boltzmann-tsp

Modifications to a project originally implemented by [Alex Goodman](https://github.com/wagoodman) to solve [the traveling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) with a [Boltzmann machine.](https://en.wikipedia.org/wiki/Boltzmann_machine) The code is by no means an optimal way to solve TSP and approximates the solution using a form of [simulated annealing.](https://en.wikipedia.org/wiki/Simulated_annealing) My motivation for modifying Goodman's work was to learn more about Boltzmann machines and in particular their application to search algorithms.

[Original Repo - Alex Goodman](https://github.com/wagoodman/boltzmann-tsp)

## Resources

Some useful links if you're interested in better understanding the ML theory behind this project:

- [Boltzmann Machines - Wikipedia](https://en.wikipedia.org/wiki/Boltzmann_machine)
- [Boltzmann Machines - Geoffrey Hinton](https://www.cs.toronto.edu/~hinton/csc321/readings/boltz321.pdf)
- [Deep Learning Textbook Chapter 20 - Ian Goodfellow et al](https://www.deeplearningbook.org/contents/generative_models.html)

## Example Output:

(Using `python 2.7` and `numpy 1.16.6`)

```bash
$ python main.py

Distance Matrix
   [[ 0 10 20  5 18]
    [10  0 15 32 10]
    [20 15  0 25 16]
    [ 5 32 25  0 35]
    [18 10 16 35  0]]

Shortest paths (Distance=66):
    [0, 1, 4, 2, 3, 0]
    [0, 3, 2, 4, 1, 0]
    [1, 0, 3, 2, 4, 1]
    [1, 4, 2, 3, 0, 1]
    [2, 3, 0, 1, 4, 2]
    [2, 4, 1, 0, 3, 2]
    [3, 0, 1, 4, 2, 3]
    [3, 2, 4, 1, 0, 3]
    [4, 1, 0, 3, 2, 4]
    [4, 2, 3, 0, 1, 4]

Longest paths (Distance=120):
    [0, 2, 1, 3, 4, 0]

Running...
Temp 23056391.522026777 Current Distance 103
Temp 12615457.77083898 Current Distance 103
Temp 6972355.066782521 Current Distance 101
Temp 3739052.4771777885 Current Distance 101
Temp 2005135.0358926603 Current Distance 120
Temp 1086151.724241316 Current Distance 120
Temp 600298.1116796107 Current Distance 120
Temp 335126.10878495063 Current Distance 120
Temp 185218.6630911663 Current Distance 120
Temp 102367.29475259413 Current Distance 120
Temp 56576.712411570465 Current Distance 120
Temp 30956.324000622582 Current Distance 120
Temp 17109.04878882948 Current Distance 120
Temp 9267.716392897706 Current Distance 120
Temp 5020.183658326051 Current Distance 120
Temp 2719.3585663279046 Current Distance 120
Temp 1458.3055920666202 Current Distance 120
Temp 789.9423754214947 Current Distance 120
Temp 415.19093786913663 Current Distance 73
Temp 209.62404568239614 Current Distance 81
Temp 101.66585315791902 Current Distance 100
Temp 45.497829335271604 Current Distance 113
Temp 18.6004305246931 Current Distance 83
Temp 6.877130438023689 Current Distance 66
Temp 2.5172521554712 Current Distance 66
Temp 0.9307027273153596 Current Distance 66
Temp 0.32724364749274104 Current Distance 66
Temp 0.11391126045361505 Current Distance 66
Boltzmann paths (Distance=66):
    [0, 1, 4, 2, 3]

Score (out of 1, higher is better): 1.00
```
