# Author= Jacob Wilson
# Date= 23/09/16

import PyPDF2
from os import listdir, path
from time import time
from warnings import warn
starttime = time()

# Edit this variable to suit your needs
folder_path = r'C:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Concatenate Multiple Folders\Super-folder Location'
# e.g. C:\Users\User\Documents\Location1


def concatenate_pdfs(file_list, output_folder_path, output_filename):
    if path.exists(r'{0}\{1}.pdf'.format(output_folder_path, output_filename)):
        warn('There is already a pdf of name "{0}" at the location "{1}"'.format(output_filename, r'{0}\{1}.pdf'.format(
            output_folder_path, output_filename)))
        return
    new_merger = PyPDF2.PdfFileMerger(strict=False)
    for pdf in file_list:
        new_merger.append(r'{0}'.format(pdf))
    new_merger.addMetadata({u'/Title': u'My title', u'/Version': u'PDF-1.5'
                            })
    #print(new_merger.pages[0].__dict__)
    #new_merger.header.replace(PyPDF2.utils.b_("PDF-1.3"),PyPDF2.utils.b_("PDF-1.5"))
    #PyPDF2.PdfFileWriter()
    new_merger.write(r'{0}\{1}.pdf'.format(output_folder_path, output_filename))


for folder in listdir(r'{0}'.format(folder_path)):
    if path.isdir(r'{0}\{1}'.format(folder_path, folder)):
        files = []
        for file in listdir(r'{0}\{1}'.format(folder_path, folder)):
            if file.lower().endswith('.pdf'):
                files.append(r'{0}\{1}\{2}'.format(folder_path, folder, file))

        files.sort()
        concatenate_pdfs(files, r'{0}\{1}'.format(folder_path, folder), folder)

endtime = time()

print('time taken: {0}s'.format(endtime - starttime))
