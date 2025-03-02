# PacmanAI
Used A*, Dijkstra's algorithm, Depth First Search, Breadth First Search, and more to find optimal cost path for an AI Pacman Agent.

Code used from MSU CSE 440 and UC Berkley CS 188.

# How to use

In the directory of the files use commands from commands.txt in a linux command line to different mazes and search algorithms.

![image](https://github.com/user-attachments/assets/c2ffb819-6321-4d9f-b09f-4f6f92f86512)

Once completed the program will output stats:

$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
[SearchAgent] using function astar and heuristic manhattanHeuristic
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 210 in 0.0 seconds
Search nodes expanded: 549
Pacman emerges victorious! Score: 300
Average Score: 300.0
Scores:        300.0
Win Rate:      1/1 (1.00)
Record:        Win

