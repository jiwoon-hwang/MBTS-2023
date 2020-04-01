import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path ="/Users/jiwoonhwang/Desktop/MBTS/standard_corrected.csv"
standard =pd.read_csv(path, index_col=0)
path ="/Users/jiwoonhwang/Desktop/MBTS/Pooled_pos_con_sub_BLANK_replaced.csv"
samples =pd.read_csv(path, low_memory=False)

###create df for each internal standard
first="cast25_0m_1"
last="Mars_C38_75m_pos3"
Std_Lyso_PC=standard.loc[["LYSO PC (18:1 D7)"],first:last]
Std_Lyso_PE=standard.loc[["Lyso PE (15:0-18:1(d7))"],first:last]
Std_SM=standard.loc[["SM (d18:1-18:1(d9))"],first:last]
Std_Cer=standard.loc[["Ceramide-d7 (C15)"],first:last]
Std_MAG=standard.loc[["MAG"],first:last]
Std_PE=standard.loc[["PE"],first:last]
Std_PG=standard.loc[["PG"],first:last]
Std_PS=standard.loc[["PS"],first:last]
Std_PI=standard.loc[["PI"],first:last]
Std_DAG=standard.loc[["DAG"],first:last]
Std_Pooled=standard.loc[["Pooled"],first:last]

standard=[Std_Lyso_PC,Std_Lyso_PE, Std_SM, Std_Cer, Std_MAG, Std_PE, Std_PG, Std_PS, Std_PI, Std_DAG, Std_Pooled]


# for i in samples.lipid_class.unique():
# 	print i
# 	print samples[samples['lipid_class']==i].species.unique()

#print Std_DAG.index.values

def headandtail(x):
	head=samples[tonormalize].iloc[:,1:12]
	tail=samples[tonormalize].loc[:,"xcms_peakgroup":]
	x=head.join(x)
	x=x.join(tail)
	return x

for std in standard:
	if std.index=='DAG':

		##find highest value
		value=std.max(axis=1)
		#print "This is the highest value: " +str(value)

		##calculate normalizing factor
		std= std.apply(lambda row: row/float(value), axis=1)
		factor= std.iloc[0,:]
		#print factor

		##define categories to normalize
		tonormalize=(samples['lipid_class']=='IP_DAG'
			)&(samples['species']!='PG'
			)&(samples['species']!='PE'
			)&(samples['species']!='PC'
			)&(samples['species']!='PDPT' 
			)

		##apply factor to peaklist
		DAG_norm=samples[tonormalize].loc[:,first:last].apply(lambda row: row/factor, axis=1)
		DAG_norm=headandtail(DAG_norm)
		#print DAG_norm

	elif std.index=='MAG':

		value=std.max(axis=1)
		std= std.apply(lambda row: row/float(value), axis=1)
		factor= std.iloc[0,:]

		tonormalize=(samples['lipid_class']=='IP_MAG'
			)&(samples['species']!='LPG'
			)&(samples['species']!='LPE'
			)&(samples['species']!='LPC'
			)&(samples['species']!='LPA' 
			)&(samples['species']!='CoprostanolEsters'
			)&(samples['species']!='CholesterolEsters'
			)

		MAG_norm=samples[tonormalize].loc[:,first:last].apply(lambda row: row/factor, axis=1)
		MAG_norm=headandtail(MAG_norm)

	elif std.index=='Lyso PE (15:0-18:1(d7))':

		value=std.max(axis=1)
		std= std.apply(lambda row: row/float(value), axis=1)
		factor= std.iloc[0,:]

		tonormalize=(samples['species']=='LPG'
			)|(samples['species']=='LPE'
			)|(samples['species']=='LPA' 
			)

		LysoPE_norm=samples[tonormalize].loc[:,first:last].apply(lambda row: row/factor, axis=1)
		LysoPE_norm=headandtail(LysoPE_norm)
		
	elif std.index=='LYSO PC (18:1 D7)':

		value=std.max(axis=1)
		std= std.apply(lambda row: row/float(value), axis=1)
		factor= std.iloc[0,:]

		tonormalize=(samples['species']=='LPC')

		LysoPC_norm=samples[tonormalize].loc[:,first:last].apply(lambda row: row/factor, axis=1)
		LysoPC_norm=headandtail(LysoPC_norm)

	elif std.index=='PE':

		value=std.max(axis=1)
		std= std.apply(lambda row: row/float(value), axis=1)
		factor= std.iloc[0,:]

		tonormalize=(samples['species']=='PE'
			)|(samples['species']=='PC')

		PE_norm=samples[tonormalize].loc[:,first:last].apply(lambda row: row/factor, axis=1)
		PE_norm=headandtail(PE_norm)

	elif std.index=='PG':

		value=std.max(axis=1)
		std= std.apply(lambda row: row/float(value), axis=1)
		factor= std.iloc[0,:]

		tonormalize=(samples['species']=='PG'
			)|(samples['species']=='PDPT')

		PG_norm=samples[tonormalize].loc[:,first:last].apply(lambda row: row/factor, axis=1)
		PG_norm=headandtail(PG_norm)

	elif std.index=='Pooled':

		value=std.max(axis=1)
		std= std.apply(lambda row: row/float(value), axis=1)
		factor= std.iloc[0,:]

		tonormalize=(samples['lipid_class']=='pigment'
			)|(samples['lipid_class']=='sterol'
			)|(samples['lipid_class'].isna()
			)|(samples['lipid_class']=='astaxanthin'
			)|(samples['species']=='CoprostanolEsters'
			)|(samples['species']=='CholesterolEsters'
			)

		Pooled_norm=samples[tonormalize].loc[:,first:last].apply(lambda row: row/factor, axis=1)
		Pooled_norm=headandtail(Pooled_norm)


final=DAG_norm.append([MAG_norm,LysoPC_norm,LysoPE_norm,PE_norm,PG_norm, Pooled_norm])

final.iloc[:,:10]=final.iloc[:,:10].replace({"0":np.nan,0:np.nan})

boolean=[]
for col in final.columns:
    col_split=col.split("_")
    if len(col_split)>3:
        if col_split[2]== 'BLANK':
            boolean.append(False)
        else: boolean.append(True)
    else: boolean.append(True)
# print (boolean)

final=final.loc[:,boolean]

final=final.fillna('NA')

print final

final.to_csv('Pooled_pos_all_norm_withNA.csv', index=False)


# #load workbook to save new dataframe in
# writer = pd.ExcelWriter('waxester.xlsx', engine='openpyxl')
# if os.path.exists('waxester.xlsx'):
# 	book = load_workbook('waxester.xlsx')
# 	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet, save new dataframe
# df2.to_excel(writer, sheet_name='WaxEster_norm')
# writer.save()
# writer.close()

 
