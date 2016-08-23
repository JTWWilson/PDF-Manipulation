#Author= Jacob Wilson
#Date= 23/09/16

from PyPDF2 import PdfFileMerger
from os import listdir, path
from time import time

starttime = time()

#edit this variable to suit your needs
folderpath=r'C:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Folder Location'
#eg C:\Users\User\Documents\Location1


def concatenateFiles(files, outputfolderpath, outputfilename):
    newMerger = PdfFileMerger()
    for file in files:
        newMerger.append(r'%s' %(file))

    newMerger.write(r'%s\%s.pdf' %(outputfolderpath, outputfilename))


files = []
for folder in listdir(r'%s' %folderpath):
    # print(folder)
    if path.isdir(r'{0}\{1}'.format(folderpath, folder)):
        for file in listdir(r'{0}\{1}'.format(folderpath, folder)):
            if file.lower().endswith('.pdf'):
                files.append(r'{0}\{1}\{2}'.format(folderpath, folder, file))
                files.sort()
                concatenateFiles(files, r'{0}\{1}'.format(folderpath, folder), folder)

endtime = time()

print('time taken: ', endtime - starttime)