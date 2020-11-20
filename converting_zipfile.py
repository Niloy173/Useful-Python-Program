# creating a program which will convert a entire folder to zip file

import os,zipfile

def convert_zip(folder):

    os.path.abspath(folder) # converting into absolute path

    n = 1

    while True:
        
        # creating zip file name
        file_name = os.path.basename(folder)+'_'+str(n)+'.zip'

        #checking if it already exists or not
        if not os.path.exists(file_name):
            break
        n = n+1

    #creating zip file object

    print(f'Creating{file_name}.....')
    zip_file = zipfile.ZipFile(file_name,'w')
        
    # walk around the folder and compress the files in sub folder

    for foldername,subfolder,files in os.walk(folder):

        print(f'Adding files in {foldername}')
        zip_file.write(foldername)

        for file in files:

            new = os.path.basename(folder)+'_'

            if file.startswith(new) and file.endswith('.zip'):

                continue # don't back the zip file if it's already in .zip format
            zip_file.write(os.path.join(foldername,file))

    zip_file.close()

    print("Done")


convert_zip("E:/test")
        
