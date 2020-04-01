import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math
import glob

os.chdir("/Users/jiwoonhwang/Desktop/MBTS/metaboanalyst")
path=("/Users/jiwoonhwang/Desktop/MBTS/metaboanalyst/Pooled_pos_all_norm_night_day_depth.csv")
template=pd.read_csv(path)

##INSERT EMPTY ROW 
empty_row=pd.DataFrame(columns=template.columns, index=[0])
template.index=template.index + 1
template=empty_row.append(template)


##NIGHT/DAY
for col in template.columns:
	col_split=col.split("_")
	if len(col_split)>3:
		if col_split[1] == 'C3':
			template.loc[0,col]='night'+"_"+col_split[2]
			
		elif col_split[1] == 'C10':
			template.loc[0,col]='day'+"_"+col_split[2]

		elif col_split[1] == 'C15':
			template.loc[0,col]='day'+"_"+col_split[2]

		elif col_split[1] == 'C21':
			template.loc[0,col]='day'+"_"+col_split[2]

		elif col_split[1] == 'C29':
			template.loc[0,col]='day'+"_"+col_split[2]

		elif col_split[1] == 'C38':
			template.loc[0,col]='day'+"_"+col_split[2]

		elif col_split[1] == 'C2':
			template.loc[0,col]='night'+"_"+col_split[2]

		elif col_split[1] == 'C4':
			template.loc[0,col]='night'+"_"+col_split[2]

		elif col_split[1] == 'C12':
			template.loc[0,col]='night'+"_"+col_split[2]

		elif col_split[1] == 'C18':
			template.loc[0,col]='night'+"_"+col_split[2]

		elif col_split[1] == 'C25':
			template.loc[0,col]='night'+"_"+col_split[2]

		elif col_split[1] == 'C34':
			template.loc[0,col]='night'+"_"+col_split[2]

template.iloc[0,0]="class"

# print template.iloc[:3,:16]

template.to_csv("Pooled_pos_all_norm_night_day_depth.csv", index=False)


