# theInfection

##About

A simple environment representing the spread and cure of the infections (negative traits).
Environment with the blob population starting with one infected blob and 3 immuned blob interacts
with the rest blob populations. Colour schemas of blobs are as follows:

red - infected
green - neutral
blue - immuned 

Blobs interact with each other at defined blob sensitive distance. The blob sesnsitivity is defines 
w.r.t to there type i.e infected,immuned.

The features of blob can be defined in features.py file as follows:

'''
#features.py
#-- Setting of window size and blob features-----

window = (1500,1000)        # window size
bg_color = [0, 0,0 ]        # Background color (black default)
blob_sensitive_dist = 150   # min distance to sense other blob
max_speed = 7                   # max speed of blob
no_blob = 80                # population of blob
immun_threshold = 2         # min immunized blob to convert neutral to immunized
infected_thresh = 4	        # min infected blob to convert immunized to infected (loss of immunity)
imm_sensitive = 0.4	        # factor of blob_sensitive_dist to neutralized the other blob
inf_sensitive = 0.6			# factor of blob_sensitive_dist to infect the other blob
#-------------------------------------------------
'''

The race begins with blob population defined as "no_blob" in window with random velocity upto max defines as "max_speed".
Blo Bounces off the wall of windows as defines in Blob.py.

##Conditions of Environment

1) "immun_threshold number" is the number of immuned blobs requiered in neutral blob sensitive radius to turn neutral
blob immune

2) "infected_thresh" number is the number of infected blobs requiered in neutral blob sensitive radius to turn immuned 
blob neutral

3) When infected blob comes in "imm_sensitive" radius of immune blob, it turns neutral

4) When neutral blob comes in "inf_sensitive" radius of infected blob, it turns infected


# The infection


# Changes in population type w.r.t to time/iteration

![alt text](https://github.com/rishi-99/theInfection/blob/master/The_fight_2.png)


# Requierements 
All below modules in python 3.6 and above

1) opencv-python 
'''
pip install opencv-python
'''







