# Author= Jacob Wilson
# Date= 06/02/16

from PyPDF2 import PdfFileMerger
from os import listdir
from time import time

starttime = time()

# edit these variables to suit your needs
file_folder_path = r'c:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Concatenate Folder\Input'
# eg c:\Users\User\Documents\Input
output_folder_path = r'c:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Concatenate Folder\Output'
# eg.c:\Users\User\Documents\Output
output_fileName = r'finalFile'
# eg.finalFile


files = []
for file in listdir(r'{0}'.format(file_folder_path)):
    if file.lower().endswith('.pdf'):
        files.append(r'{0}\{1}'.format(file_folder_path, file))
        files.sort()

newMerger = PdfFileMerger()
for file in files:
    newMerger.append(r'{0}'.format(file))

newMerger.write(r'{0}\{1}.pdf'.format(output_folder_path, output_fileName))

endtime = time()

print('time taken: {0}s'.format(endtime - starttime))