import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math
import glob

os.chdir("/Users/jiwoonhwang/Desktop/MBTS")
path=("/Users/jiwoonhwang/Desktop/MBTS/Runs_reruns_organized.xlsx")
all_runs=pd.read_excel(path)
path=("/Users/jiwoonhwang/Desktop/MBTS/order_of_run_actual.xlsx")
order_of_run=pd.read_excel(path, sheet_name="sheet")

df=pd.DataFrame()


for oor in all_runs['Runs']:
	df[oor]=order_of_run[oor]

print df.head()

writer = pd.ExcelWriter('order_of_run_actual.xlsx', engine='openpyxl')
if os.path.exists('order_of_run_actual.xlsx'):
	book = load_workbook('order_of_run_actual.xlsx')
	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet
df.to_excel(writer, sheet_name='order of time')
writer.save()
writer.close()

# for oor in all_runs['File Name'].values:
# 	if oor not in order_of_run.columns:
# 		print oor

# orderofruns=[]
# for oor in order_of_run.columns:
# 	orderofruns.append(oor)
#print orderofruns

# for oor in orderofruns:
# 	print oor
# print all_runs['File Name']


# print order_of_run.columns

##EDIT CSV FILE
#all_runs=all_runs[~all_runs["File Name"].astype(str).str.startswith("blank")]
#all_runs=all_runs[~all_runs["File Name"].astype(str).str.startswith("F")]
# all_runs=all_runs[~all_runs["File Name"].astype(str).str.endswith("neg1")]
# all_runs=all_runs[~all_runs["File Name"].astype(str).str.endswith("neg2")]
# all_runs=all_runs[~all_runs["File Name"].astype(str).str.endswith("neg3")]
# all_runs.to_csv("all_runs.csv", index=False)

##COMBINE ALL CSV FILES IN DIRECTORY
# extension='csv'
# all_filenames=[i for i in glob.glob('*.{}'.format(extension))]
# all_filenames.sort()
# print all_filenames

##FIND NUMBER OF OCCURANCES IN COLUMN
# print all_runs['File Name'].value_counts()

# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

# combined_csv.to_csv("all_runs.csv", index=False)


