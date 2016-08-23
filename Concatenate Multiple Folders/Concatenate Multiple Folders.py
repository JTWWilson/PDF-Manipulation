# Author= Jacob Wilson
# Date= 23/09/16

from PyPDF2 import PdfFileMerger
from os import listdir, path
from time import time

starttime = time()

# Edit this variable to suit your needs
folder_path = r'C:\Users\Jacob\Documents\GitHub\PDF-Manipulation\Concatenate Multiple Folders\Super-folder Location'
# e.g. C:\Users\User\Documents\Location1


def concatenate_pdfs(file_list, output_folder_path, output_filename):
    assert not path.exists(r'{0}\{1}.pdf'.format(output_folder_path, output_filename)), \
        'There is already a pdf of name "{0}" at the location "{1}"'\
            .format(output_filename, r'{0}\{1}.pdf'.format(output_folder_path, output_filename))
    new_merger = PdfFileMerger()
    for file in file_list:
        new_merger.append(r'{0}'.format(file))

    new_merger.write(r'{0}\{1}.pdf'.format(output_folder_path, output_filename))


files = []
for folder in listdir(r'{0}'.format(folder_path)):
    # print(folder)
    if path.isdir(r'{0}\{1}'.format(folder_path, folder)):
        for file in listdir(r'{0}\{1}'.format(folder_path, folder)):
            if file.lower().endswith('.pdf'):
                files.append(r'{0}\{1}\{2}'.format(folder_path, folder, file))
                files.sort()
        concatenate_pdfs(files, r'{0}\{1}'.format(folder_path, folder), folder)

endtime = time()

print('time taken: {0}s'.format(endtime - starttime))
