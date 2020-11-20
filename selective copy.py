"""Walks through a folder tree and searches for files with a certain file extension, copies them into new folder
   """

import shutil,os

def selectiove_copy(inputfolder,outputfolder):

    resultfolder = os.path.abspath(outputfolder)

    for foldername,subfoldername,filename in os.walk(inputfolder):

        for files in filename:

            if files.endswith('.jpg'): #try with .jpg or .ext or .pdf or .png

               filepath = os.path.join(os.path.abspath(foldername),files)

               if not os.path.exists(resultfolder):
                   os.makedirs(resultfolder) #not mendatory


               if os.path.dirname(filepath)!=resultfolder: # prevent from same path
                    shutil.copy(filepath,resultfolder)
                    print(f'{filepath} copied to {resultfolder}')



if __name__=='__main__':
    selectiove_copy('E:\Extra','E:\Extra\spam')







