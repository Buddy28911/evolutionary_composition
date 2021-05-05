# Evolutionary Composition
## By Danny
### Director: Dr. Lutz Hamel
### CSC 499

<br>

# General Description
Evolutionary Composition is my senior capstone project. 
The project's goal is to see what type of music a program can create using genetic algorithms and human curation.
Specifically, the program will use human curation to create and evolve themes to the user's liking. 
First, the program generates a batch of melodies. 
Then, each of these tunes is played for the user. The user rates each melody on a scale from 0 to 5. 
An elitist selection algorithm picks the highest-scoring pieces for the next generation of music. 
The next population is created through mating and mutation.
A cross-over function takes two parent melodies and returns two children. 
The first child contains [[First half of parent2's measures], [Second half of parent1's measures]].
The second child contains [[First half of parent1's measures], [Second half of parent2's measures]].
The mutation function mutates a parent melody by randomly pitch-shifting each note in the melody. The pitch-shifted melody is returned as the child.
The algorithm repeats until the desired number of generations is satisfied.

<br>

# Dependencies
The Evolutionary Composition program runs on Python 3.
## The project's dependencies are
- DEAP
- Numpy
- MIDO
- python-rtmidi

<br>

# Use

To run the program with no command-line args use

```
python3 main.py
```

