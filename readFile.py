import pandas as pd
import numpy as np
import os
# I think there is a limit to how much I can do with the reading of the text file. Because I feel that as you are preprocessing
# the data, the form you require will vary widely. I have some functions that hopefully illustrates how to do it so you can customise
# them yourself to suit your needs.


'''
Ensure that you are in the root folder of all the fold folders and target files
read_text(fold_name):
    fold_name: this is the name of the fold you want to read ALL patient files of. It will be read into a 2 dimensional
    list. If you would like to retrieve just the first patient instead, you will need to change the line 
    "txt_all.extend(txt[1:])" to "txt_all.append(txt[1:])" and you will be to use "read_text(fold1.txt)[0]" to retrieve
    the relevant patient's data
read_ans(file_name):
    file_name: this is the name of the file you want to read ALL targets of. It will be read into a 2 dimensional
    list. To retrieve the first patient's target: read_ans(ans.csv)[0]
put_single_into_dataframe(txt): This functions takes in 2 dimensional list ie the output of read_text(fold1.txt) 
put_multiple_into_dataframe(txt): Multiple is for using it with the output of read_text after you wanted to change it to append
'''

def read_text(fold_name):
    txt_all = list()
	for f in os.listdir(fold_name): # for each file in the directory
		if f.endswith(".txt"):
			with open(os.path.join(fold_name, f), 'r') as fp: # open each file
				txt = fp.readlines() # read inside the file
			recordid = txt[1].rstrip('\n').split(',')[-1] # get recordid
			txt = [[int(recordid)] + t.rstrip('\n').split(',') for t in txt] # preface each row with the recordid as all patients are 1 file
			txt_all.extend(txt[1:]) # skip the parameter list
    return txt_all

def read_ans(file_name):
    txt_all = list()
    with open(file_name, 'r') as fp: # opens the csv file
        txt = fp.readlines() 
    for i in range(1, len(txt)): # similar to above read_text
        record_id, length_of_stay, hospital_death = txt[i].rstrip('\n').split(',')
        txt_all.append([record_id, length_of_stay, hospital_death])
    return txt_all

def put_multiple_into_dataframe(txt_all):
    df = pd.DataFrame()
    for i in txt_all:
        df2 = pd.DataFrame(i, columns=['recordid', 'time', 'parameter', 'value'])
        df = df.append(df2, ignore_index=True)
    return df

def put_single_into_dataframe(txt_all):
    df = pd.DataFrame(txt_all, columns=['recordid', 'time', 'parameter', 'value'])
    return df