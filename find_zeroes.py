import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path ="/Users/jiwoonhwang/Desktop/MBTS/pooled_pos_con.xlsx"
df =pd.read_excel(path, sheet_name='standard')
    
#count=0
for col in range(df.shape[1]):
	for row in range(df.shape[0]):
		if df.iat[row,col]==0:
			#count+=1
			print(df.columns[col],df.iat[row,3])
#print count

#open file to write in
#writer = pd.ExcelWriter('Peaklist_pooled_pos.xlsx', engine='openpyxl')
#if os.path.exists('Peaklist_pooled_pos.xlsx'):
#	book = load_workbook('Peaklist_pooled_pos.xlsx')
#	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet
#df2.to_excel(writer, sheet_name='standard')
#writer.save()
#writer.close()