import pprint
import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook

#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path ="/Users/jiwoonhwang/Desktop/MBTS/Pooled_pos_bethanie.xlsx"

df =pd.read_excel(path, sheet_name='Pooled_pos_con_sub_BLANK')

#REPLACE ZERO VALUES WITH NAN
# df1=df.replace(0,np.NaN)


##FIND AVERAGE OF TRIPLICATES
# df2 = pd.DataFrame()
# df2 = df1.iloc[:,0:12]
# df2['pos1']=df1['MARS_C15_BLANK_pos1']
# df2['pos2']=df1['MARS_C15_BLANK_pos2']
# df2['pos3']=df1['MARS_C15_BLANK_pos3']

# choose=df2.loc[:,['pos1','pos2','pos3']]
# df2['average']=choose.mean(axis=1)

##WRITE TO NEW DATAFRAME
df3=pd.DataFrame()
df3 = df.iloc[:,0:12]
count=0
for col in df.columns:
	count += 1
	if col == 'cast25_0m_1':
		start=count
		print 'start is:'+ str(start)
	if col=='Mars_C38_75m_pos3':
		end=count
		print 'end is:'+ str(end)

#df2=pd.read_excel(path, sheet_name='BLANK_average')

df4=df.iloc[:,start-1:end]

##REPLACE MINUS VALUES WITH ZERO
df4[df4<0]=0
for col in df4.columns:
	df3[col]=df4[col]

##SUBTRACT BLANK FROM ALL VALUES
# for col in df4.columns:
# 	df3[col]=df4[col]-df2['average']
# print df3.head



#CREATE NEW WORKSHEET WITH AVERAGES
writer = pd.ExcelWriter('Pooled_pos_bethanie.xlsx', engine='openpyxl')
if os.path.exists('Pooled_pos_bethanie.xlsx'):
	book = load_workbook('Pooled_pos_bethanie.xlsx')
	writer.book = book

df3=df3.fillna(0) 
df3.to_excel(writer, sheet_name='Pooled_pos_con_sub_BLANK')
writer.save()
writer.close()


# for col in df.columns:
# 	column_split=col.split('_')
# 	if column_split==4:
# 		if (column_split[1], column_split[2])=('C15','BLANK'):



# countlist = []
# count = 0
# for col in df.columns:
# 	count += 1
# 	column_split=col.split('_')	
# 	if len(column_split)==4:
# 		if column_split[1]==cst:
# 			if column_split[2]==depth:								
# 				countlist.append(count)
# 				cast = column_split[1]
# print countlist
# print cast
# 				#print cast
# 			#print dep
# if len(countlist)!=0:			
# 	start = countlist[0]
# 	end = countlist[-1]	
# 	choose = df1.iloc[:,start-1:end]
# 	choose_aver = choose.mean(axis=1)

# 	#df1.insert(int(end),"average_"+cast+"_"+depth,choose_aver, True)

# 	x= "average_"+cast+"_"+depth
# 	df2[x]= choose_aver