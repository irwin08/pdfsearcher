import PyPDF2
import re
import os

folder_path = "testfolder/"
search_term = "normal"

for name,subfolders,subfiles in os.walk(folder_path):
    for f in subfiles:
        if not 'pdf' in f:
            continue
        pdf = PyPDF2.PdfFileReader((name+'/'+f))
        TotalPages = pdf.getNumPages()

        for i in range(0,TotalPages):
            page = pdf.getPage(i)
            text = page.extractText()

            search_result = re.search(search_term, text)

            if search_result:
                print('Match found in file ', f, ' on page ', i)
        
