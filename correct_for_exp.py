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
df =pd.read_excel(path, sheet_name='standard')

# bre_ext=[("C2", "5m"), ("C2","10m"), ("C2","20m"),("C2", "60m"), ("C4","0m"), ("C4","20m"), (
# 	"C10", "40m"),("C10", "80m"),("C10", "150m"), ("C15", "0m"),("C15", "20m"),("C15", "80m"),(
# 	"C15", "150m"), ("C18","100m"),("C21","40m"),("C21","80m"),("C21","150m"), ("C38","0m"),(
# 	"C38","50m"),("C38","130m"),("C38","200m")]

toomuchstandard=[("C2", "5m"), ("C2","10m"), ("C2","20m"),("C2", "60m"),("C3","20m"), ("C4","5m"), ("C4","10m"),("C10", "20m"),("C10", "100m"),("C15", "0m"),("C15", "20m"),("C15", "80m"),(
	"C15", "150m"),("C18","100m"),("C21","40m"),("C21","80m"),("C21","150m"),("C21", "20m"), ("C21","100m"),("C29","40m"),("C29","100m")]

# bre_ext_dic={
# 	"C2": ("5m", "10m", "20m", "60m") 
# }


for col in df.columns:
	column_split=col.split('_')	
	if len(column_split)>3:
		for samp in toomuchstandard:
			if (column_split[1],column_split[2])==samp:
				df[col]=df[col]/2
			



#if i in ['']:
#	df[i]=df[i]/2


#open file to write in
writer = pd.ExcelWriter('Pooled_pos_bethanie.xlsx', engine='openpyxl')
if os.path.exists('Pooled_pos_bethanie.xlsx'):
	book = load_workbook('Pooled_pos_bethanie.xlsx')
	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet
df.to_excel(writer, sheet_name='standard_corrected_TAG')
writer.save()
writer.close()