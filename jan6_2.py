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
df =pd.read_excel(path, sheet_name="standard_corrected")
df1=pd.read_excel(path, sheet_name="January 6_2")

jan6_2=[("C34","40m"), ("C25","20m"), ("C25","100m"), ("C12","0m"), ("C12", "150m")]

for col in df.columns:
	column_split=col.split('_')	
	if len(column_split)>3:
		for samp in jan6_2:
			if (column_split[1],column_split[2])==samp:
				df1[col]=df[col]

writer = pd.ExcelWriter('Pooled_pos_bethanie.xlsx', engine='openpyxl')
if os.path.exists('Pooled_pos_bethanie.xlsx'):
	book = load_workbook('Pooled_pos_bethanie.xlsx')
	writer.book = book

#df2=df2.fillna('NA')
df1.to_excel(writer, sheet_name='January 6_2')
writer.save()
writer.close()
