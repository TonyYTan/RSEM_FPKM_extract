import sys
import os
from itertools import islice
from unicodedata import name
import pandas as pd

# mydict = {}

# giving directory name and get current directory
dirname = os.getcwd()

# giving file extension
ext = ('genes.results')
counter = 0
files_pd = pd.DataFrame()
for files in os.listdir(dirname):
    if files.endswith(ext):
        mydict = {}
        # print(files)
        c = open(files, 'r')
        # print(c)
        for line in islice(c, 1, None): # c, starting from line 1 (line 0 is the column name), stop line: None, default step: 1
            # print(line)
            a = line.strip().split()
            key = a[0]
            value = a[6] 
            # 可以选择其他列 depends on the column name
            if key in mydict:
                    mydict[key] = mydict[key] + '\t' + value
            else:
                mydict[key] = value
        # for key, value in mydict.items():
        #     print(key + '\t' + value)
        if counter == 0:
            files_pd = pd.DataFrame.from_dict(mydict, orient='index', columns=[files.strip() + "_FPKM"])
            # print(len(mydict))
            # print(files_pd)
            counter += 1
        elif counter > 0:
            files_temp_pd = pd.DataFrame.from_dict(mydict, orient='index', columns=[files.strip() + "_FPKM"])
            files_pd = files_pd.merge(files_temp_pd, left_index = True, right_index = True)
            counter += 1
            # print(files_pd)


files_pd = files_pd.reset_index()
files_pd.rename(columns={ files_pd.columns[0]: "ensembl_ID" }, inplace = True)
files_pd[["ensembl_ID_", "version_num"]] = files_pd.ensembl_ID.str.split(".", n = 1, expand = True)

files_pd = files_pd.set_index('ensembl_ID_')
files_pd = files_pd.drop(['ensembl_ID', 'version_num'], axis=1)
print(files_pd)
files_pd.to_csv("raw_FPKM_genes.csv", sep = '\t', index = True)
