import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Downloads/')
path ="/Users/jiwoonhwang/Desktop/MBTS/pooled_pos_con.xlsx"
df =pd.read_excel(path, sheet_name='DAG_standard')
path="/Users/jiwoonhwang/Downloads/TAG_combined.xlsx"
df1 =pd.read_excel(path)
df2=pd.read_excel(path, sheet_name="Sheet1")

print df1.columns
print df.columns

for col in df.columns:
	df2[col]=df1[col]

print df2.columns

writer = pd.ExcelWriter('TAG_combined.xlsx', engine='openpyxl')
if os.path.exists('TAG_combined.xlsx'):
	book = load_workbook('TAG_combined.xlsx')
	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet
df2.to_excel(writer, sheet_name='order_corrected')
writer.save()
writer.close()