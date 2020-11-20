# Run the program in command line
# Converting word file to pdf
# run the program from the file path

import win32com.client
import os,sys

import docx

try:

    word_file = os.path.abspath(sys.argv[1]) # file we want to convert

    pdf_file = os.path.abspath(sys.argv[2]) # user type file name


    

    wdformatpdf = 17 #word's numeric code for pdf

    wordobj = win32com.client.Dispatch('Word.Application')

    docobj = wordobj.Documents.Open(word_file)

    docobj.SaveAs(pdf_file,FileFormat = wdformatpdf)

    wordobj.close()

    docobj.close()


except Exception as e:
    print(e)

