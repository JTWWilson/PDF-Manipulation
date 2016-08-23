#Author= Jacob Wilson
#Date= 06/02/16

import PyPDF2
import os

"""

"""

#edit these variables to suit your needs
fileFolderPath=r'c:\Users\Jacob\Documents\Python\PDF Manipulation\Folder Location'
#eg c:\Users\User\Documents\Location1
outputFolderPath=r'c:\Users\Jacob\Documents\Python\PDF Manipulation\End Result'
#eg.c:\Users\User\Documents\Location2
outputFileName=r'finalFile'
#eg.finalFile


files=[]
for file in os.listdir(r'%s' %fileFolderPath):
    if file.lower().endswith('.pdf'):
        files.append(fileFolderPath+r'/' +file)
        files.sort()

newMerger=PyPDF2.PdfFileMerger()
for file in files:
    newMerger.append(r'%s' %(file))

newMerger.write(r'%s%s.pdf' %(outputFolderPath,outputFileName))
