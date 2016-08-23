# Author = Jacob Wilson
# Date = 10/11/15

from PyPDF2 import PdfFileMerger
from os import listdir
from time import time

starttime = time()

# Edit these variables to suit your needs
cover_sheet_path = r'c:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Insert Sheets\Sheets\Cover Sheet.pdf'
# e.g. r'c:\Users\User\Documents\Cover Sheet.pdf'
back_sheet_path = r'c:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Insert Sheets\Sheets\Back Sheet.pdf'
# e.g. r'c:\Users\User\Documents\Back Sheet.pdf'
file_folder_path = r'c:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Insert Sheets\Input'
# e.g. r'c:\Users\User\Documents\Input'
output_folder_path = r'c:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Insert Sheets\Output'
# e.g. r'c:\Users\User\Documents\Output'


def concatenate_pdfs(files, output):  # This takes a list of PDFs, concatenates them and writes the new file
    new_merger = PdfFileMerger()
    for i in files:
        newmerger.append(i)
    new_merger.write(r'{0}'.format(output))


def cover_and_back__sheet(cover_sheet_path, back_sheet_path, file_folder_path, output_folder_path):
    for file in listdir(file_folder_path):
        concatenate_pdfs(['{}'.format(cover_sheet_path),
                          '{0}\{1}'.format(file_folder_path, file),
                          '{0}'.format(back_sheet_path)],
                         '{0}\\final{1}'.format(output_folder_path,
                                                file))  # Do note that the output is prefixed with 'final'

def cover_sheet(cover_sheet_path, file_folder_path, output_folder_path):
    for file in listdir(file_folder_path):
        concatenate_pdfs(['{}'.format(cover_sheet_path),
                          '{0}\{1}'.format(file_folder_path, file)],
                         '{0}\\final{1}'.format(output_folder_path,
                                                file))  # Do note that the output is prefixed with 'final'

endtime = time()

print('time taken: {0}s'.format(endtime - starttime))