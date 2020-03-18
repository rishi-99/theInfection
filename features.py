
#-- Setting of window size and blob features-----

window = (1500,1000)        # window size
initial_infected = 1      # Initial population with infected blobs
initial_immuned = 4         # Initial population with immuned blobs
show_frames = False          # show frames (press 'q' to stop)
bg_color = [0, 0,0 ]        # Background color (black default)
blob_sensitive_dist = 150   # min distance to sense other blob
max_speed = 7                   # max speed of blob
no_blob = 70                # population of blob
immun_threshold = 1         # min immunized blob to convert neutral to immunized
infected_thresh = 4	        # min infected blob to convert immunized to infected (loss of immunity)
imm_sensitive = 0.4	        # factor of blob_sensitive_dist to neutralized the other blob
inf_sensitive = 0.6			# factor of blob_sensitive_dist to infect the other blob
stats = 'stats.txt'
video = 'theInfection.avi'
#-------------------------------------------------

