import cv2
import numpy as np
from  random import *
from features import *
from Blob import blob
import os



if "__main__" == __name__:

	if not os.path.isdir('media'):
		os.mkdir('media')
	stats_ = 'media/'+ stats
	video_ = 'media/'+ video

	with open(stats_, 'w') as f:
		f.write('not_infected\tinfected\timmnuned\n')
	blobs=  []
	for x in range(no_blob):
		blobs.append(blob(6,1, (randint(0,window[0]),randint(0,window[1])),(randint(1,max_speed),randint(1,max_speed)),window))
	for blob_ in blobs[:initial_infected]:
		blob_.infected=True
	for blob_ in blobs[initial_infected:initial_infected+initial_immuned]:
		blob_.immunizer=True



	out_ = cv2.VideoWriter(video_, cv2.VideoWriter_fourcc(*'DIVX'), 15, window)
	while True:

		# color = [213, 193,62 ]
		main_matrix = np.array( [[bg_color]*window[0]]*window[1], np.uint8)
		# main_matrix = np.zeros((window[0],window[1]),np.uint8)

		for Blob in blobs:
			immunized_count = []
			infected_count = []


			for other in blobs:
				if Blob !=other:
					if 0 < Blob-other  < blob_sensitive_dist:

							if other.infected:
								if Blob - other <= blob_sensitive_dist * inf_sensitive:
									infected_count.append(other)
							if not  other.infected:
								if other.immunizer:
									if Blob - other <= blob_sensitive_dist * imm_sensitive:
										immunized_count.append(other)


							blob_color = Blob.color
							ratio = (Blob - other) / blob_sensitive_dist
							brightB =  bg_color[0]*(ratio) + blob_color[0]*(1-ratio)
							brightG =  bg_color[1]*(ratio) + blob_color[1]*(1-ratio)
							brightR =  bg_color[2]*(ratio) + blob_color[2]*(1-ratio)
							cv2.line(main_matrix, (Blob.x,Blob.y), (other.x,other.y), (brightB,brightG ,brightR), 2)

			# if 0 < len(immunized_count) < immun_threshold:
			# 		Blob.infected=False
			# elif len(immunized_count) >= immun_threshold:
			# 		Blob.immunizer = True
			# 		Blob.infected =  False
			#
			# elif len(infected_count) > 0 :
			# 	if Blob.immunizer:
			# 		if len(infected_count) >= infected_thresh:
			# 			for x in infected_count:
			# 				x.infected=True
			# 			Blob.immunizer = False
			# 			Blob.infected = True
			# 	else:
			# 			Blob.infected = True


			if len(infected_count) > 0 :
				if Blob.immunizer:
					if len(infected_count) >= infected_thresh:
						for x in infected_count:
							x.infected=True
						Blob.immunizer = False
						Blob.infected = True
				else:
						Blob.infected = True

			if 0 < len(immunized_count) < immun_threshold:
					Blob.infected=False
			if len(immunized_count) >= immun_threshold:
					Blob.immunizer = True
					Blob.infected =  False




		infected = 0
		not_infected = 0
		immnuned = 0


		for Blob in blobs:
			if Blob.infected:
				infected+=1
			else:
				if Blob.immunizer:
					immnuned+=1
					not_infected += 1
				else:
					not_infected+=1

			blob_color = Blob.color
			cv2.circle(main_matrix, Blob.position, Blob.radius, (blob_color[0], blob_color[1], blob_color[2]), -1)
			Blob.update()


		font = cv2.FONT_HERSHEY_SIMPLEX

		fontScale = 0.6
		color = (255, 255, 255)
		thickness = 1

		cv2.putText(main_matrix, "Population - {}".format(no_blob), (10,20), font, fontScale,color, thickness, cv2.LINE_AA, False)
		cv2.putText(main_matrix, "Infected - {}".format(infected), (10,40), font, fontScale,color, thickness, cv2.LINE_AA, False)
		cv2.putText(main_matrix, "Not Infected - {}".format(not_infected), (10,60), font, fontScale,color, thickness, cv2.LINE_AA, False)
		cv2.putText(main_matrix, "Immunised - {}".format(immnuned), (10,80), font, fontScale,color, thickness, cv2.LINE_AA, False)
		cv2.putText(main_matrix, "Immunising dist - {}".format(blob_sensitive_dist*imm_sensitive), (10,100), font, fontScale,color, thickness, cv2.LINE_AA, False)
		cv2.putText(main_matrix, "Infecting dist - {}".format(blob_sensitive_dist*inf_sensitive), (10,120), font, fontScale,color, thickness, cv2.LINE_AA, False)

		with open(stats_,'a') as f:
			f.write(f'{not_infected}\t{infected}\t{immnuned}\n')

		out_.write(main_matrix)
		print('Infected =',infected,', Not_infected =',not_infected,', Immuned =',immnuned,end='\r')

		if infected  == no_blob or not_infected==no_blob:
			break

		if show_frames:
			cv2.imshow("image", main_matrix)
			if cv2.waitKey(80) & 0xFF == ord('q'):
				break

	out_.release()