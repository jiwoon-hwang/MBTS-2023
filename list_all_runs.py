import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math
import glob

os.chdir("/Users/jiwoonhwang/Desktop/MBTS")
path=("/Users/jiwoonhwang/Desktop/MBTS/all_runs.csv")
all_runs=pd.read_csv(path)

all_runs_list=[]
df=pd.DataFrame()

for oor in all_runs['File Name']:
	all_runs_list.append(oor)

order={"0m":0 ,"5m":1, "10m":2, "20m":3,"40m":4,"45m":5,"50m":6,"60m":7,"75m":8,"80m":9,"100m":10, "130m":11, "150m":12, "200m":13, "BLANK":14}

all_runs_list=sorted(all_runs_list)

all_runs_list_split=[]
for run in all_runs_list:
	run_split=run.split("_")
	if len(run_split)>3:
		all_runs_list_split.append(run_split)



#print all_runs_list_split


all_runs_sort=sorted(all_runs_list_split, key=lambda x:(x[1],order[x[2]]))
all_runs_sorted=[]
for a in all_runs_sort:
	a="_".join(a)
	all_runs_sorted.append(a)

for run in all_runs_list:
	run_split=run.split("_")
	if len(run_split)<4:
		all_runs_sorted.append(run)

print all_runs_sorted

# all_runs_list_ab=sorted(all_runs_list)

df['Runs']=all_runs_sorted


df.to_excel('Runs_reruns_organized.xlsx')

