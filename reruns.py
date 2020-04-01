import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/rerun')
path ="/Users/jiwoonhwang/Desktop/MBTS/rerun/worksheet.xlsx"
df =pd.read_excel(path)

rerun=[("C25","0m"), ("C25","150m"), ("C29","0m"), ("C29","150m"),("C34","0m"),("C34","150m")]
colm=[]
for col in df.columns:
	column_split=col.split('_')	
	if len(column_split)>3:
		for samp in rerun:
			if (column_split[1],column_split[2])==samp:
				colm.append(col)
# print colm
print df.loc[10,colm]