import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path ="/Users/jiwoonhwang/Desktop/MBTS/Pooled_pos_bethanie.xlsx"
df =pd.read_excel(path, sheet_name='standard_corrected')
path="/Users/jiwoonhwang/Desktop/MBTS/orderofrun.xlsx"
df1 =pd.read_excel(path)
df2=pd.read_excel(path, sheet_name="Sheet2")



orderofruns=[]
for samp in df1['Sample']:
	column_split=samp.split('_')
	if len(column_split)==3:
		orderofruns.append(column_split)
#print orderofruns

#print orderofruns[0]
organized=[]
for oor in orderofruns:
	for col in df.columns:
		col_split=col.split('_')
		# if col_split[0]=='Mars':
		# 	# print col_split
		# col_spl=[]
		if len(col_split)>3:
		
			if [col_split[0],col_split[1],col_split[2]]==oor:
				organized.append(col)
# print organized
for org in organized:
	df2[org]=df[org]

# print df2.head


		# col_spl.append(col_split[0])
		# col_spl.append(col_split[1])
		# col_spl.append(col_split[2])
		# #print col_spl
		# if col_spl not in orderofruns:
		# 	print col_spl
	
	

# print df2.columns

writer = pd.ExcelWriter('Pooled_pos_bethanie_edit.xlsx', engine='openpyxl')
if os.path.exists('Pooled_pos_bethanie_edit.xlsx'):
	book = load_workbook('Pooled_pos_bethanie_edit.xlsx')
	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet
df2.to_excel(writer, sheet_name='TAG_order_of_run')
writer.save()
writer.close()