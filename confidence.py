
import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook

#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path ="/Users/jiwoonhwang/Desktop/MBTS/pooled_pos_worksheet.xlsx"
df =pd.read_excel(path)

#find confident compounds
df1 = df.iloc[df.index[df['C3f']!=1]]
df2 = df.iloc[df1.index[df1['C3c']!=1]]

#df2 = df2.fillna('NA')

#export to new spreadsheet	
df2.to_excel('pooled_pos_con.xlsx')