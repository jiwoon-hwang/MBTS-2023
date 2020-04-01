import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math
import glob

os.chdir("/Users/jiwoonhwang/Desktop/MBTS")
path=("/Users/jiwoonhwang/Desktop/MBTS/LOB_Peaklist_Pos.csv")
LOB=pd.read_csv(path)
path=("/Users/jiwoonhwang/Desktop/MBTS/order_of_run_actual.xlsx")
order_of_run=pd.read_excel(path, sheet_name="sheet")



df=pd.DataFrame()
wierdTAG=[("C4","20m"), ("C4","60m"), ("C10","40m"), ("C10", "80m"), ("C21", "0m"), ("C21","40m"), ("C21","80m"), ("C25", "100m")]
lst=[]
for col in order_of_run.columns:
	column_split=col.split('_')	
	if len(column_split)>3:
		for WT in wierdTAG:
			if (column_split[1],column_split[2])==WT:
				lst.append(col)

#print lst

df=order_of_run.iloc[:,1:12]
for l in lst:
	df[l]=order_of_run[l]

# df['lipid_class']=LOB['lipid_class']
# df['species']=LOB['species']


writer = pd.ExcelWriter('pooled_pos_con_sub_BLANK.xlsx', engine='openpyxl')
if os.path.exists('pooled_pos_con_sub_BLANK.xlsx'):
	book = load_workbook('pooled_pos_con_sub_BLANK.xlsx')
	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet
df.to_excel(writer, sheet_name='weirdTAGs_standard', index=False)
writer.save()
writer.close()


# all_runs=pd.read_excel(path)

# all_runs=all_runs.fillna(0)

# wrongRT=pd.DataFrame()
# wrongRT= all_runs[all_runs["Original"]=="2d"]

# print wrongRT["Runs"]