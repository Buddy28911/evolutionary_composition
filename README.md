# Evolutionary Composition
## By Danny Noe
### Director: Dr. Lutz Hamel
### CSC 499

<br>

# Introduction

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

To learn about the various command-line arguments use

```
python3 main.py -h -v
```

<br>

# Command-Line Arguments

Evolutionary Composition can be configured in various ways.

<br>

## General Parameters

<br>

- Verbosity: Outputs program's settings. 
<br> Flags: '-v' || '--verbosity'
```
-v
```

- Outport: Sets the outport device for MIDO. If none is given, you will get the (system specific) default port.
<br> Flags: '-o' || '--outport'
```
-o "IAC Driver Bus 1"
```

<br>

## Musical Parameters

<br>

- Key Signature: Sets the key signature for the program. 
Supported key signatures are ["Cb","Gb","Db","Ab","Eb","Bb","F","C","G","D","A","E","B","F#","C#"]
<br> Flags: '-k' || '--key_signature'
```
-k Gb 
```

- Tempo: Sets the tempo (in BPM) for the program. Range: [2,300]
<br> Flags: '-t' || '--tempo'
```
-t 100
```

- Backing Track: Enables a backing track. Turn on the track with True, False for off.
<br> Flags: '-b' || '--back_track'
```
-b t
```

- Arpeggio or Scale: Sets the backing track to play an ascending arpeggio or scale. True for arp, false for scale
<br> Flags: '-a' || '--arp_or_scale'
```
-a f
```

<br>

## Algorithm Parameters

<br>

- Genetic Algorithm: Sets the GA to use. Supported GAs are eaSimple, eaMuPlusLambda, eaMuCommaLambda
<br> Flags: '-ga' || '--genetic_alg'
```
-ga "eaMuPlusLambda"
```

Each GA has its own specific parameters that can be configured.

- eaMuPlusLambda (𝜇 + 𝜆) Parameters: POPSIZE, NGEN, MU, LAMBDA_ CXPB, MUTPB, NGEN
- eaMuCommaLambda (𝜇 , 𝜆) Parameters: POPSIZE, NGEN, MU, LAMBDA_ CXPB, MUTPB, NGEN
- eaSimple (𝜇 , 𝜆) Parameters: POPSIZE, NGEN, CXPB, MUTPB, NGEN

<br>

- Pop size: Sets the number of melodies to generate in the initial population.
<br> Flags: '--popsize'
```
--popsize 10
```

<br>

- Ngen: ngen sets the number of generations the GA will run for.
<br> Flags: '--ngen'
```
--ngen 3
```

<br>

- Mu: sets the number of individuals to select for the next generation.
<br> Flags: '--mu'
```
--mu 3
```

<br>

- Lambda_: sets number of children to produce at each generation.
<br> Flags: '--lambda_'
```
--lambda_ 6
```

<br>

- cxpb: sets the probability that an offspring is produced by crossover.
<br> Flags: '--cxpb'
```
--cxpb 0.7
```

<br>

- mutb: sets the probability that an offspring is produced by mutation.
<br> Flags: '--mutb'
```
--mutb 0.3
```
<b>Note:</b> cxpb + mutpb should = 1.0
