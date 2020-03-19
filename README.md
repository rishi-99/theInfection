# theInfection

## About

A simple environment representing the spread and cure of the infections (negative traits).
Environment with the blob population starting with one infected blob and 3 immuned blob interacts
with the rest blob populations. Colour schemas of blobs are as follows:

- red blob - infected
- green blob- neutral
- blue blob- immuned 


Blobs interact with each other at defined blob sensitive distance. The blob sesnsitivity is defines 
w.r.t to there type i.e infected,immuned.

The features of blob can be defined in features.py file as follows:

```python

#features.py
#-- Setting of window size and blob features-----

window = (1500,1000)        # window size
bg_color = [0,0,0]          # Background color (black default)
blob_sensitive_dist = 150   # min distance to sense other blob
max_speed = 7               # max speed of blob
no_blob = 80                # population of blob
immun_threshold = 2         # min immunized blob to convert neutral to immunized
infected_thresh = 4	    # min infected blob to convert immunized to infected (loss of immunity)
imm_sensitive = 0.4	    # factor of blob_sensitive_dist to neutralized the other blob
inf_sensitive = 0.6	    # factor of blob_sensitive_dist to infect the other blob
#-------------------------------------------------
```

The race begins with blob population defined as "no_blob" in "window" with random velocity upto max defined as "max_speed".
Blob Bounces off the wall of window.



[![Simulation of infection and cure in a population](https://github.com/rishi-99/theInfection/blob/master/media/theInfected.gif)](https://github.com/rishi-99/theInfection/blob/master/media/theInfection.avi)



## Conditions of Environment

- "immun_threshold number" is the number of immuned blobs required in neutral blob sensitive radius to turn neutral
blob immune

- "infected_thresh" number is the number of infected blobs required in immuned blob sensitive radius to turn immuned 
blob neutral

- When infected blob comes in "imm_sensitive" radius of immune blob, it turns neutral

- When neutral blob comes in "inf_sensitive" radius of infected blob, it turns infected




# Changes in population type w.r.t time/iteration

![Population stats](https://github.com/rishi-99/theInfection/blob/master/media/graph.png)


# Requirements 
All below modules in python 3.6 and above

- opencv-python 

```python

pip install opencv-python
```
- Numpy
```python

pip install numpy
```

## Execution 

Run 'funbox.py' with python3. Features of environment can be changed in 'feature.py'.

# Improvements and further idea

- Add more blob features like health, blob multiplication and blob death.
- Add food and poison based interaction
- Add blob size increament and decrement based on food and energy consumption
- Add re-enforced learning using Q-table

### Please feel free to contribute, improve, enrich and evolve this project.







