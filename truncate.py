
import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/rerun')
path ="/Users/jiwoonhwang/Desktop/MBTS/rerun/Peaklist_Pooled_Pos.xlsx"
df =pd.read_excel(path)

#for i in df['peakgroup_mz']:
#	dec = float('%.3f'%(i))
#	print dec
#	round (i,3)
#print round(df['peakgroup_mz'],3)

##TRUNCATE TO THIRD DECIMAL POINT
# def third(x):
# 	x = round(x,3)
# 	return float(x)
# def third_dec(x):
# 	x=float('%.3f'%(x))
# 	return x
# def third_dec_math(x):
# 	x=math.trunc(1000*x)/1000
# 	return x
# def my_solution(x):
# 	x=int(x*1000)
# 	x=float(x)
# 	x=x/1000
# 	return x

# df['mz']=df['mz'].apply(my_solution)
#print df['peakgroup_mz'][2737]
# standard_index=[]
# for i in [386.325, 711.567, 759.588, 755.557, 847.604, 610.540, 829.799]:
# 	print df.index[df['mz'].between(i-0.0005, i+0.0005)]
df2= df.iloc[[4856,5500,5448,6542,3497,6371],:]
print df2

#writer = pd.ExcelWriter('Peaklist_pooled_pos.xlsx', engine='openpyxl')
#if os.path.exists('Peaklist_pooled_pos.xlsx'):
#	book = load_workbook('Peaklist_pooled_pos.xlsx')
#	writer.book = book

#df2=df2.fillna('NA')
#df2.to_excel(writer, sheet_name='standard')
#writer.save()
#writer.close()


