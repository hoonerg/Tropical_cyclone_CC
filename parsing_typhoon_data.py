#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


import re
import numpy as np


#open a the file
fileHandler = open('from_1989.txt')
arrayOfTyphoons = list()
currentRow = list()
currentKey = ""
dataIndex = 0;
nameIndex = 0;
dataMatrix = list()
lineMatrix = None
result = None
lineCount = 0
tyPhoonDict = dict()
stackedMatrix = None

for line in fileHandler:
    lineStripped = line.strip()
    lineCount = lineCount + 1
    
    if re.search(r'^66666',lineStripped):
        #dealing with name row
        nameIndex = nameIndex + 1
        dataMatrix_np = np.zeros([1, 6])
        if len(lineStripped.split()) == 7:
            currentKey = str(nameIndex) + "_NULL"
            #print(currentKey)
            tyPhoonDict[currentKey] = dataMatrix_np

        elif len(lineStripped.split()) == 8:
            currentKey = str(nameIndex) + "_"+ lineStripped.split()[6]
            #print(currentKey)
            tyPhoonDict[currentKey] = dataMatrix_np
        elif len(lineStripped.split()) == 9:
            #print(currentKey)
            currentKey = str(nameIndex) + "_" + lineStripped.split()[7]
            tyPhoonDict[currentKey] = dataMatrix_np
         

    else:
        #dealing with data rows
        lineMatrix = np.array([lineStripped.split()[ : 6]])
        lineMatrix = lineMatrix.astype(np.integer)
        stackedMatrix = tyPhoonDict[currentKey]
        result = np.concatenate([stackedMatrix, lineMatrix], axis=0)
        #print(result.shape)
        tyPhoonDict[currentKey] = result

        
        
for name in tyPhoonDict:
    tyPhoonDict[name] = tyPhoonDict[name][1:, :]
    
columns = np.array(["date/time", "Indicator", "grade", "latitude", "longitude", "central_pressure"])

print(tyPhoonDict["1_OWEN"][:])

for k in tyPhoonDict.keys():
    print(tyPhoonDict[k][:])


            


# In[ ]:





# In[ ]:





# In[ ]:




