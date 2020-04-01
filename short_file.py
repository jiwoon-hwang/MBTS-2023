import os
import re

os.chdir('/Users/jiwoonhwang/Downloads/mzXML_neg')

cwd= os.getcwd()

#print(cwd)

#print(os.listdir(cwd))
for f in os.listdir(cwd):
	#print(os.path.splitext(f))
		file_name, file_ext = os.path.splitext(f)
		file_split = file_name.split('_')
		if len(file_split) == 3:
			#print file_split
			cast = file_split[0]
			depth = file_split[1]
			run = file_split[2]
			#res = [int(i) for i in cast if i.isdigit()]
			#print(str(res))
			temp = re.findall(r'\d+', cast) 
			res = str(map(int, temp))[1:-1]
			print(res)
			new_name = '{}_C{}_{}_neg{}{}'.format("MARS", res, depth, run, file_ext)
			print(new_name)


		#file_split[1] == 'C3':
			#file_split.append('night')
			#new_name = '_'.join(file_split)
			#new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)