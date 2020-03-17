
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

