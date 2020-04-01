import os

os.chdir('/Users/jiwoonhwang/Downloads/mzXML_neg')

cwd= os.getcwd()

#print(cwd)

#print(os.listdir(cwd))
for f in os.listdir(cwd):
	#print(os.path.splitext(f))
		file_name, file_ext = os.path.splitext(f)
		file_split = file_name.split('_')
		if file_split[1] == 'C3':
			file_split.append('night')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C10':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C15':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C21':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C29':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C38':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C4':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C12':
			file_split.append('night')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C18':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C25':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		elif file_split[1] == 'C34':
			file_split.append('day')
			new_name = '_'.join(file_split)
			new_name = '{}{}'.format(new_name,file_ext)
			#print(new_name)

			os.rename(f,new_name)

		else:
			print(file_split)
			
		
	

