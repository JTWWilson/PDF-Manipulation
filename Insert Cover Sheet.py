#Author= Jacob Wilson
#Date= 27/07/15

import PyPDF2
import os

#edit these variables to suit your needs
coverSheetPath=r'c:\Users\Jacob\Documents\Python\PDF Manipulation\Location1\CoverSheet.pdf'
#eg. c:\Users\User\Documents\Location1\CoverSheet.pdf
fileFolderPath=r'c:\Users\Jacob\Documents\Python\PDF Manipulation\Location2'
#eg c:\Users\User\Documents\Location2
outputFolderPath=r'c:\Users\Jacob\Documents\Python\PDF Manipulation'
#eg.c:\Users\User\Documents\Location3


def concatPDFs(PDF1,PDF2,output): #this takes two PDFs, concatenates them and writes the new file
    newMerger= PyPDF2.PdfFileMerger()
    newMerger.append(r'%s' %(PDF1))
    newMerger.append(r'%s' %(PDF2))
    newMerger.write(r'%s' %(output))

for file in os.listdir(r'%s' %(fileFolderPath)):
    concatPDFs('%s' %(coverSheetPath),
               '%s\%s' %(fileFolderPath,file),
               '%s\\final%s' %(outputFolderPath,file)) #do note that the output is prefixed with 'final' to differentiate
