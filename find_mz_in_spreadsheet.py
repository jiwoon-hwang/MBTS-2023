import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path ="/Users/jiwoonhwang/Desktop/MBTS/Peaklist_pooled_pos.xlsx"
df =pd.read_excel(path)

standard_index=[]
for i in [386.325, 711.567, 759.588, 755.557, 847.604, 610.540, 829.799]:
 	x= df.index[df['mz'].between(i-0.0005, i+0.0005)]
	standard_index.append(x)
print standard_index
df1 = df.iloc[[4864, 5493, 5442, 6529, 3511],:]
print df1
#df2=df.loc[[4864, 5493, 5442, 6529, 3511],:]
#print df2

writer = pd.ExcelWriter('pooled_pos_con.xlsx', engine='openpyxl')
if os.path.exists('pooled_pos_con.xlsx'):
	book = load_workbook('pooled_pos_con.xlsx')
	writer.book = book

#df2=df2.fillna('NA')
df1.to_excel(writer, sheet_name='copy')
writer.save()
writer.close()
