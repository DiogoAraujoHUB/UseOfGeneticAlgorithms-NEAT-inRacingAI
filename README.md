## Project Details
This project was inspired by the video made by the youtuber “Code Bullet”, which can be found referenced in the README, using Python and NEAT. It was created for the "Vida Artificial" class for FCUL.

Made by: Diogo Araújo - 60997

Video Link: https://www.youtube.com/watch?v=r428O_CMcpI&list=WL&index=2&t=4s

More info about this project can be found in the associated report found in the project files.

## Project Summary
The referenced video details the youtuber’s experience with creating an Artificial Intelligence (AI) capable of traversing a racetrack by using a reinforcement algorithm, more specifically QLearning. During the video, the youtuber showcases the results obtained by the algorithm as well as the process which he took to create it. While highlighting its execution, it brought me to the question of if there were better alternatives to the algorithm that was being used. 

Fortunately, during one of the lectures for this class we discussed the use of Genetic Algorithms (GA) and their possibilities for video games. This brought me to the idea of utilizing this algorithm in search of a faster, and better performing, algorithm for the applied context. This brings us to the aim of this project, which is to use a genetic algorithm in order complete a map (track) without any issues.

With this, I am aiming to create an AI using a Genetic Algorithm (GA) which can complete a lap on a racing track without any issues.

## Genetic Algorithm (GA)
A Genetic Algorithm (GA) is an artificial intelligence which is inspired by the process of natural selection. They are commonly used to generate high-quality solutions to optimization and search problems by relying on biologically inspired operators such as mutation and crossover.

![image](https://github.com/DiogoAraujoHUB/UseOfGeneticAlgorithms-NEAT-inRacingAI/assets/61624282/c6d4ea86-38fd-426b-8c62-61253125e98e)

## NEAT Algorithm (NEAT)
The actual algorithm implemented for the AI of the racing game was the NeuroEvolution of Augmenting Topologies (NEAT). It is a genetic algorithm used in the generation of evolving artificial neural networks (neuroevolution technique). It alters both the weighting parameters and structures of networks, attempting to find a balance between the fitness of evolved solutions and their diversity. 

![image](https://github.com/DiogoAraujoHUB/UseOfGeneticAlgorithms-NEAT-inRacingAI/assets/61624282/78b4fb98-782a-458c-a1a6-95296a5a4d4f)

## Implementation of the Algorithm
Distance was used as a reward in order to stop cars from staying in the same place and not moving (if the time spent alive was a reward) or from simply turning around and reaching the finish line (if reaching the finish line was a reward). After each generation, we evolve our cars with the cars that have the highest fitness value as these will most likely survive and reproduce. On the other hand, cars with a low fitness value will eventually go extinct. 

When a car reproduces, it will not just duplicate itself onto a child car. This child car will be quite like its parent but not the same. Any car that is quite similar forms a species and if a species does not see any improvements after a few generations then it goes extinct as they are most likely dead ends. 

Using these principles, we create an algorithm in which the best cars survive and reproduce whereas the worst cars go extinct. Due to these extinctions, the model is forced to experiment with variations in order to find an improving species. Summarizing, the cars that go the most distance and are therefore rewarded persist and are replicated, although not fullyprevent the population from becoming too similar to each other.

![image](https://github.com/DiogoAraujoHUB/UseOfGeneticAlgorithms-NEAT-inRacingAI/assets/61624282/35ecda48-0f2c-47a1-9f2e-f0baea14765c)

## Running the Algorithm
In this section, we can see an image of the algorithm being executed in a simple track. This algorithm can be ran on multiple different tracks however, which are present in the Images folder.

![image](https://github.com/DiogoAraujoHUB/UseOfGeneticAlgorithms-NEAT-inRacingAI/assets/61624282/27b2530c-7dc2-43fc-bd4b-3deeaa953091)

